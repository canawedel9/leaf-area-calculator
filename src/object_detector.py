# -----------------------------------------------------
#   part 9 - Final Measurement (Pixels to Real Unit)
# -----------------------------------------------------
import cv2
import matplotlib.pyplot as plt
import pytesseract
from contour_detection import leaf_contour, filtered_contours
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image
image_path = 'data/raw/leaf2.jpg'
image = cv2.imread(image_path)
if image is None:
    print(f"❌ Error loading {image_path}")
else:
    print(f'✅ Loaded image: {image_path}')

# ----------------------------------------
# 1. ID the ruler using bottom-zone logic

ruler_contour = None
img_height = image.shape[0]

for cnt in filtered_contours:
    M = cv2.moments(cnt)
    if M['m00'] != 0:
        cy = int(M['m01'] / M['m00'])

        # If object's center is in the bottom 40%, its the ruler
        if cy > (img_height * 0.6):
            ruler_contour = cnt 
            break

# ---------------------------------------------
# 2. Perform calculation if both objects found
if ruler_contour is not None and leaf_contour is not None:
    # Get ruler position to crop it
    rx, ry, rw, rh = cv2.boundingRect(ruler_contour)
    ruler_roi = image[ry:ry+rh, rx:rx+rw]               #focus on ruler

    # Preprocess crop for OCR (maake it grayscale and clear)
    gray_ruler = cv2.cvtColor(ruler_roi, cv2.COLOR_BGR2GRAY)
    _, thresh_ruler = cv2.threshold(gray_ruler, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # AI looks for digit on the ruler
    d = pytesseract.image_to_data(thresh_ruler, config='--psm 11 digits', output_type=pytesseract.Output.DICT)

    # Store detected numbers and their X coordinates
    nodes = []
    for i in range (len(d['text'])):
        if d['text'] [i].strip().isdigit():
            nodes.append({'val': int(d['text'][i]), 'x': d['left'][i]})
    
    # Calculate PPCM based on the numbers the AI "sees"
    if len(nodes) >= 2:
        nodes = sorted(nodes, key=lambda x: x['x'])
        pixel_dist = nodes[1]['x'] - nodes[0] ['x']
        val_diff = nodes[1] ['val'] - nodes[0] ['val']

        if val_diff == 0: val_diff = 1
        pixels_per_cm = pixel_dist / val_diff
        print(f"✅ OCR Scale: {pixels_per_cm:.2f} px/cm (Based on {nodes[0] ['val']} to {nodes[1] ['val']})")
    else:
        # Fallbacl if AI cant read the numbers clearly
        print("⚠️ OCR failed. Falling back to default 3.5cm width")
        pixels_per_cm = rw / 3.5

    # Calculate final area
    # divide by (pixels_per_cm squared) coz area is 2D
    leaf_pixel_area = cv2.contourArea(leaf_contour)
    leaf_real_area_cm2 = leaf_pixel_area / (pixels_per_cm**2)

    #-----------------------------
    # 3. Print output to terminal

    print('📊 FINAL MEASUREMENT RESULTS')
    print('='*40)
    print(f'Scale Factor: {pixels_per_cm:.2f} px/cm')
    print(f'Leaf Area: {leaf_pixel_area:.0f} px²')
    print(f'Converted Area: {leaf_real_area_cm2:.2f} cm²')

    #-----------------------------
    # 4. Final Visual Output
    plt.figure(figsize=(10, 8))
    result_img = image.copy()

    # Label the leaf with its real area
    lx, ly, lw, lh = cv2.boundingRect(leaf_contour)
    cv2.putText(result_img, f"{leaf_real_area_cm2:.2f} cm2", (lx, ly-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
    plt.title(f'Final Result: {leaf_real_area_cm2:.2f} cm²')
    plt.axis('off')

    # Save the final result
    plt.savefig('results/14_final_measurement.png', dpi=150)
    plt.show()

else:
    print("❌ Error: Could not find both leaf and ruler. Check your contours.")

print('✅ Part 9 complete: Final measurement saved!')