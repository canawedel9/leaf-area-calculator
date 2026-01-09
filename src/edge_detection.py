import cv2
import matplotlib.pyplot as plt
import numpy as np

# Part1
# Load & Preprocess
image = cv2.imread('data/raw/leaf2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
print('✅ Image loaded & preprocessed!')
print(f'Original shape: {image.shape}')
print(f'Grayscale shape: {gray.shape}')



# Part2
# Canny edge detection
edges_low = cv2.Canny(blurred, 15, 80)  #very sensitive
edges_medium = cv2.Canny(blurred, 50, 150)  #balanced
edges_high = cv2.Canny(blurred, 100, 150)  #weak edges

# Display results
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].imshow(gray, cmap='gray')
axes[0, 0].set_title('Original Grayscale')
axes[0, 0].axis('off')

axes[0, 1].imshow(edges_low, cmap='gray')
axes[0, 1].set_title('Canny Edges: Low Thresholds (15, 80) ⭐ BEST')
axes[0, 1].axis('off')

axes[1, 0].imshow(edges_medium, cmap='gray')
axes[1, 0].set_title('Canny Edges: Medium Thresholds (50, 150)')

axes[1, 1].imshow(edges_high, cmap='gray')
axes[1, 1].set_title('Canny Edges: High Thresholds (100, 150)')
axes[1, 1].axis('off')

plt.tight_layout()
plt.savefig('results/08_canny_edge_detection.png', dpi=150)
plt.show()
print('✅ Canny Edge detection complete!')



# Part3 
# Sobel edge detection (X and Y gradients)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)  # X directions
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)  # Y directions
sobel_combined = np.sqrt(sobelx**2 + sobely**2)
sobel_combined = np.uint8(sobel_combined)

# Laplacian edge detection
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# Canny for comparison
canny = cv2.Canny(blurred, 15, 80)


# Display Sobel and Laplacian results
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].imshow(gray, cmap='gray')
axes[0, 0].set_title('Original')
axes[0, 0].axis('off')

axes[0, 1].imshow(sobel_combined, cmap='gray')
axes[0, 1].set_title('Sobel Edge Detection')
axes[0, 1].axis('off')

axes[1, 0].imshow(laplacian, cmap='gray')
axes[1, 0].set_title('Laplacian Edge Detection')
axes[1, 0].axis('off')

axes[1, 1].imshow(canny, cmap='gray')
axes[1, 1].set_title('Canny Edge Detection (Best!) ⭐')
axes[1, 1].axis('off')

plt.tight_layout()
plt.savefig('results/09_edge_detection_comparison.png', dpi=150)
plt.show()
print('✅ Edge Detection Comparison complete!')



# Part4
# Edge Detection Pipeline
def detect_edges(image_path, blur_kernel=5, canny_low=15, canny_high=80):
    """ Complete edge detection pipeline
    Parameters:
    - image_path: path to image
    - blur_kernel: size of Gaussian blur (odd number)
    - canny_low: lower threshold for Canny
    - canny_high: upper threshold for Canny
    Returns:
    - edges: binary edge image
    """
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading {image_path}")
        return None
    
    # Convert to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (blur_kernel, blur_kernel), 0)

    # Canny Edge Detection using Tuned Values
    edges = cv2.Canny(blurred, canny_low, canny_high)
    
    print(f'✅ Edges detected for {image_path}')
    print(f' Edge pixels: {np.sum(edges > 0)}')
    print(f' Total pixels: {edges.size}')

    # Display results
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Original')
    axes[0].axis('off')

    axes[1].imshow(gray, cmap='gray')
    axes[1].set_title('Grayscale')
    axes[1].axis('off')

    axes[2].imshow(edges, cmap='gray')
    axes[2].set_title('Edges Detected')
    axes[2].axis('off')

    plt.tight_layout()
    plt.savefig('results/10_edge_detection_pipeline.png', dpi=150)
    plt.show()

# Test on my image Leaf2
detect_edges('data/raw/leaf2.jpg')
