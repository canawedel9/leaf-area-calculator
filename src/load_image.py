import cv2
import matplotlib.pyplot as plt

# load image
image_path = 'data/raw/leaf1.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {image_path}")
    print("Make sure the file exists!")
else:
    print(f"Success! Image loaded.")
    print(f"Image shape: {image.shape}")
    print(f"Height: {image.shape[0]} pixels")
    print(f"Width: {image.shape[1]} pixels")
    print(f"Channels: {image.shape[2]} (BGR)")

# Display
plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("First Real Leaf Image")
plt.axis("off")
plt.tight_layout()
plt.savefig('results/loaded_leaf.png')
plt.show()

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10, 8))
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Version")
plt.axis("off")
plt.tight_layout()
plt.savefig('results/loaded_leaf_gray.png')
plt.show()
