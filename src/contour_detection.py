# Part5
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load and preprocess image
image = cv2.imread('data/raw/leaf2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold to create binary image (REQUIRED for contour!)
_, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

# Note: THRESH_BINARY_INV makes object white, background black


# Find contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # compress contour points
print(f'✅ Found {len(contours)} contours!')

# Draw all contours on original image
image_with_contours = image.copy()
cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 3)  # -1 = draw ALL contours. (0, 255, 0) = green. 3 = thickness

# Display fig
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(binary, cmap='gray')
axes[1].set_title(f'Binary Threshold')
axes[1].axis('off')

axes[2].imshow(cv2.cvtColor(image_with_contours, cv2.COLOR_BGR2RGB))
axes[2].set_title(f'Contours Detected: {len(contours)}')
axes[2].axis('off')

plt.tight_layout()
plt.savefig('results/11_contours_basic.png', dpi=150)
plt.show()
print('✅ Contour Detection complete!')



# --- Part 6: Analyzing Contours ---

# Filter contours by size (remove noise)
min_area = 5000 
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

print(f'Total contours: {len(contours)}')
print(f'After filtering (area > {min_area}): {len(filtered_contours)}')
print('\n📊 Contour Analysis (Leaf vs Ruler with Centroids):')
print('='*60)

image_analyzed = image.copy()
img_height = image.shape[0] 
leaf_count = 0

for i, contour in enumerate(filtered_contours):
    # 1. Calculate basic properties
    area = cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(contour)
    
    # 2. Calculate Centroid (The Middle Point)
    M = cv2.moments(contour)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    else:
        cx, cy = 0, 0

    # 3. Position Logic: Top 60% = Leaf, Bottom 40% = Ruler
    if cy > (img_height * 0.6):
        label_text = "RULER"
        color = (255, 0, 0) # Blue
        print(f'📏 Object {i+1}: Ruler at Centroid ({cx}, {cy})')
    else:
        leaf_count += 1
        label_text = f"LEAF #{leaf_count}: {area:.0f}px"
        color = (0, 255, 0) # Green
        print(f'🍃 Object {i+1}: Leaf at Centroid ({cx}, {cy}) | Area: {area:.0f} px²')

    # 4. Draw Annotations
    # Draw the green/blue outline
    cv2.drawContours(image_analyzed, [contour], -1, color, 3)
    
    # Draw the Centroid point (Red dot)
    cv2.circle(image_analyzed, (cx, cy), 10, (0, 0, 255), -1) 
    
    # Draw a bounding box (Cyan)
    cv2.rectangle(image_analyzed, (x, y), (x+w, y+h), (255, 255, 0), 2)
    
    # Add text label above the object
    cv2.putText(image_analyzed, label_text, (x, y-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

# Display plot
plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(image_analyzed, cv2.COLOR_BGR2RGB))
plt.title(f'Final Analysis: {leaf_count} Leaf and Ruler Identified with Centroids')
plt.axis('off')
plt.tight_layout()

# Save the final result
plt.savefig('results/12_contour_analysis.png', dpi=150)
plt.show()

print('\n✅ Part 6 complete: Centroids are now marked with red dots!')



'''
# Filter contours by area
min_area = 50000  # minimum area threshold
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
print(f'Total contours: {len(contours)}')
print(f'Area after filtering (area > {min_area} px): {len(filtered_contours)}')
print('\n📊 Contour Analysis')
print('='*60)

# Analyze each contour
image_analyzed = image.copy()
for i, contour in enumerate(filtered_contours):
    # Calculate properties
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)

    # Bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)

    # Centroid (center point)
    M = cv2.moments(contour)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    else:
        cx, cy = 0, 0
    
    # Aspect ratio
    aspect_ratio = float(w) / h if h != 0 else 0

    # Print info
    print(f'\nContour {i+1}:')
    print(f' Area: {area:.0f} pixels')
    print(f' Perimeter: {perimeter:.0f} pixels')
    print(f' Bounding Box: {w}x{h} pixels')
    print(f' Center: ({cx}, {cy})')
    print(f' Aspect ratio: {aspect_ratio:.2f}')

    # Draw on image
    cv2.drawContours(image_analyzed, [contour], -1, (0, 255, 0), 2)  # green contour
    cv2.rectangle(image_analyzed, (x, y), (x + w, y + h), (255, 0, 0), 2)  # blue bounding box
    cv2.circle(image_analyzed, (cx, cy), 5, (0, 0, 255), -1)  # red centroid

    # Add text label
    label = f'#{i+1}: {area:.0f}px²'
    cv2.putText(image_analyzed, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

# Display plot
plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(image_analyzed, cv2.COLOR_BGR2RGB))
plt.title(f'Contour Analysis: {len(filtered_contours)} objects found')
plt.axis('off')

plt.tight_layout()
plt.savefig('results/12_contour_analysis.png', dpi=150)
plt.show()
print('\n✅ Contour analysis complete!')
'''



# Part 7 Contour Approximation
# Get the upper object (leaf) on the image
image_height = image.shape[0]
leaf_contour = None
for cnt in filtered_contours:
    M = cv2.moments(cnt)
    if M['m00'] != 0:
        cy = int(M['m01'] / M['m00'])
        if cy < (img_height * 0.6):         # Target top area
            leaf_contour = cnt
            break

# Different approximation levels
epsilon_values = [0.001, 0.01, 0.05, 0.1]

#  Percentage of perimeter
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for idx, epsilon_factor in enumerate (epsilon_values):
    epsilon = epsilon_factor * cv2.arcLength(leaf_contour, True)
    approx = cv2.approxPolyDP(leaf_contour, epsilon, True)

    # Draw approximation
    img_copy = image.copy()
    cv2.drawContours(img_copy, [approx], -1, (0, 255, 0), 3)

    # Draw corner points
    for point in approx:
        cv2.circle(img_copy, tuple(point[0]), 5, (255, 0, 0), -1)
    
    # Display
    row = idx // 2
    col = idx % 2
    axes[row, col].imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
    axes[row, col].set_title(f'ε={epsilon_factor} ({len(approx)} points)')
    axes[row, col].axis('off')
plt.tight_layout()
plt.savefig('results/13_contour_approximation.png', dpi=150)
plt.show()
print(f'Original contour: (len(largest_contour)) points')
print(f'Approximated: (len(approx)) points')



# Part 8 - Convex Hull & Defect

# Convez hull (like rubber band around the object)
hull = cv2.convexHull(leaf_contour)

# Convexity defects (where object is "dented")
hull_indices = cv2.convexHull(leaf_contour, returnPoints=False)
defects = cv2.convexityDefects(leaf_contour, hull_indices)

# Draw
img_hull = image.copy()
cv2.drawContours(img_hull, [leaf_contour], -1, (0, 255, 0), 2)
cv2.drawContours(img_hull, [hull], -1, (255, 0, 0), 2)                 # Mark defect points

if defects is not None:
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        far = tuple(leaf_contour[f] [0])
        cv2.circle(img_hull, far, 5, (0, 0, 255), -1)
    
# Display
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].axis('off')
axes[1].imshow(cv2.cvtColor(img_hull, cv2.COLOR_BGR2RGB))

axes[1].axis('off')
axes[1].set_title('Green-Contour, Blue-Hull, Red-Defects')
plt.show()
print('✅ Conves hull analysis complete')