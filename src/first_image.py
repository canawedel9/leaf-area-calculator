import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create simple image form scratch (100x100, all black)
height, width = 100, 100
image = np.zeros((height, width, 3), dtype=np.uint8)

# Draw green rectangle as leaf, BGR format: blue, green, red
cv2.rectangle(image, (20, 20), (80, 80), (0, 255, 0), -1)

# Display
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("First CV Image - A Green Square")
plt.axis("off")
plt.savefig('results/first_image.png')
plt.show()

print("Image created and saved!")
print(f"Image shape: {image.shape}") # (100, 100, 3) = height, width, channels 