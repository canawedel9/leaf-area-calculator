#day2
#part2
import cv2
import matplotlib.pyplot as plt
import numpy as np

#Load an image
image_path = 'data/raw/leaf2.jpg'
image = cv2.imread(image_path)

#Check if image loaded successfully
if image is None:
    print(f"❌ Error: Could not load {image_path}")
    print("Make sure file exists!")
else:
    print(f"✅ Image uploaded successfully!")
    print(f"Shape: {image.shape}")
    print(f"Height: {image.shape[0]} pixels")
    print(f"Width: {image.shape[1]} pixels")
    print(f"Channels: {image.shape[2]}")
    print(f"Data type: {image.dtype}")
    print(f"Size: {image.size} total values")

#Display image using matplotlib (converts BGR to RGB)
plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Leaf Image')
plt.axis('off')
plt.tight_layout()
plt.savefig('results/01_original_image.png')
plt.show()

#part3
#Convert to different color spaces
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Display all versions
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].imshow(rgb)
axes[0, 0].set_title('Original_(RGB)')
axes[0, 0].axis('off')

axes[0, 1].imshow(gray, cmap='gray')
axes[0, 1].set_title('Grayscale')
axes[0, 1].axis('off')

axes[1, 0].imshow(hsv)
axes[1, 0].set_title('HSV Color Space')
axes[1, 0].axis('off')

#Show individual RGB channels
red_channel = image[:, :, 2]
axes[1, 1].imshow(red_channel, cmap='Reds')
axes[1, 1].set_title('Red Channel Only')
axes[1, 1].axis('off')

plt.tight_layout()
plt.savefig('results/02_color_conversion.png', dpi=150)
plt.show()


#part4
#Load multiple images
images = []
for i in range(1, 4):
    img = cv2.imread(f'data/raw/leaf{i}.jpg')
    if img is not None:
        images.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

#Display in grid
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for idx, img in enumerate(images):
    axes[idx].imshow(img)
    axes[idx].set_title(f'Leaf {idx+1}')
    axes[idx].axis('off')

plt.tight_layout()
plt.savefig('results/03_multiple_images.png', dpi=150)
plt.show()


#part5
#Load image
image = cv2.imread('data/raw/Leaf2.jpg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Resize to specific dimensions
resized_small = cv2.resize(rgb, (300, 300))
resized_large = cv2.resize(rgb, (800, 800))

#Resize by percentage
width, height = rgb.shape[1], rgb.shape[0]
resized_half = cv2.resize(rgb, (width//2, height//2))

#Crop a region 0% (top-left to bottom-right)
cropped = rgb[0:height, 0:width]

#Display results
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0, 0].imshow(rgb)
axes[0, 0].set_title(f'Original {width}x{height}')
axes[0, 0].axis('off')

axes[0, 1].imshow(resized_small)
axes[0, 1].set_title('Resized 300x300')
axes[0, 1].axis('off')

axes[0, 2].imshow(resized_large)
axes[0, 2].set_title('Resized 800x800')
axes[0, 2].axis('off')

axes[1, 0].imshow(resized_half)
axes[1, 0].set_title('50% Size')
axes[1, 0].axis('off')

axes[1, 1].imshow(cropped)
axes[1, 1].set_title('Cropped Region')
axes[1, 1].axis('off')

axes[1, 2].axis('off')
plt.tight_layout()
plt.savefig('results/04_resize_crop.png', dpi=150)
plt.show()


#part 6
#Rotation n Flipping
height, width = rgb.shape[:2]
center = (width // 2, height // 2)

#rotate 45 degrees
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_45 = cv2.warpAffine(rgb, rotation_matrix, (width, height))

#rotate 90 degrees
rotated_90 = cv2.rotate(rgb, cv2.ROTATE_90_CLOCKWISE)

#flipping
flipped_horizontal = cv2.flip(rgb, 1)
flipped_vertical = cv2.flip(rgb, 0)
flipped_both = cv2.flip(rgb, -1)

#Display results
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0, 0].imshow(rgb)
axes[0, 0].set_title('Original')
axes[0, 0].axis('off')

axes[0, 1].imshow(rotated_45)
axes[0, 1].set_title('Rotated 45°')
axes[0, 1].axis('off')

axes[0, 2].imshow(rotated_90)
axes[0, 2].set_title('Rotated 90°')
axes[0, 2].axis('off')

axes[1, 0].imshow(flipped_horizontal)
axes[1, 0].set_title('Flipped Horizontal')
axes[1, 0].axis('off')

axes[1, 1].imshow(flipped_vertical)
axes[1, 1].set_title('Flipped Vertical')
axes[1, 1].axis('off')

axes[1, 2].imshow(flipped_both)
axes[1, 2].set_title('Flipped Both')
axes[1, 2].axis('off')

plt.tight_layout()
plt.savefig('results/05_rotations_flipping.png', dpi=150)
plt.show()


#part 7
#Adjust brightness and contrast
brightened = cv2.convertScaleAbs(rgb, alpha=1.2, beta=50)
darkened = cv2.convertScaleAbs(rgb, alpha=1.0, beta=-50)
high_contrast = cv2.convertScaleAbs(rgb, alpha=1.5, beta=0)
low_contrast = cv2.convertScaleAbs(rgb, alpha=0.5, beta=0)
adjusted = cv2.convertScaleAbs(rgb, alpha=1.3, beta=30)

#Display results
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0, 0].imshow(rgb)
axes[0, 0].set_title('Original')
axes[0, 0].axis('off')

axes[0, 1].imshow(brightened)
axes[0, 1].set_title('Brighter (+50)')
axes[0, 1].axis('off')

axes[0, 2].imshow(darkened)
axes[0, 2].set_title('Darker (-50)')
axes[0, 2].axis('off')

axes[1, 0].imshow(high_contrast)
axes[1, 0].set_title('High Contrast (x1.5)')
axes[1, 0].axis('off')

axes[1, 1].imshow(low_contrast)
axes[1, 1].set_title('Low Contrast (x0.5)')
axes[1, 1].axis('off')

axes[1, 2].imshow(adjusted)
axes[1, 2].set_title('Adjusted (x1.3, +30)')
axes[1, 2].axis('off')

plt.tight_layout()
plt.savefig('results/06_brightness_contrast.png', dpi=150)
plt.show()


#part 8
#Universal color detection

#Conver BGR image to Lab color space
lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
l, a, b = cv2.split(lab)

#'a' channel for green-red leaf
#Replacing old gray verision
_, thresh_otsu = cv2.threshold(a, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#Safety check: leaf is white (255), background is black (0)
if np.mean(thresh_otsu) > 127:
    thresh_otsu = cv2.bitwise_not(thresh_otsu)

#(optional) keep other thresholds for comparison
_, thresh_binary_inv = cv2.threshold(a, 127, 255, cv2.THRESH_BINARY_INV)

#Display results
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

#Original image
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original')

#Manual Threshold (Binary INV)
axes[1].imshow(thresh_binary_inv, cmap='gray')
axes[1].set_title('Manual (127)')

# Otsu's Threshold
axes[2].imshow(thresh_otsu, cmap='gray')
axes[2].set_title("Otsu's Method")

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.savefig('results/07_thresholding.png', dpi=150)
plt.show()


'''
#Previous code, dont run
#Convert to grayscale first
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#simple threshold
_, thresh_binary = cv2.threshold(gray, 127, 355, cv2.THRESH_BINARY)
_, thresh_binary_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

#Adaptive threshold
thresh_adaptive_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#Otsu's method (automatic threshold selection)
_, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Display results
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0, 0].imshow(gray, cmap='gray')
axes[0, 0].set_title('Original Grayscale')
axes[0, 0].axis('off')

axes[0, 1].imshow(thresh_binary, cmap='gray')
axes[0, 1].set_title('Binary Thershold (127)')
axes[0, 1].axis('off')

axes[0, 2].imshow(thresh_binary_inv, cmap='gray')
axes[0, 2].set_title('Binary Inverse')
axes[0, 2].axis('off')

axes[1, 0].imshow(thresh_adaptive_mean, cmap='gray')
axes[1, 0].set_title("Adaptive Threshold")
axes[1, 0].axis('off')

axes[1, 1].imshow(thresh_otsu, cmap='gray')
axes[1, 1].set_title("Otsu's Threshold")
axes[1, 1].axis('off')

axes[1, 2].axis('off')
plt.tight_layout()
plt.savefig('results/07_thresholding.png', dpi=150)
plt.show()
print(f'✅ All images saved to results/ folder!.')
'''