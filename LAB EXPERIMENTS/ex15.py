
import cv2
import numpy as np
from pathlib import Path

# Folder path
folder = (
    Path.home()
    / "OneDrive"
    / "Desktop"
    / "Computer Vision"
    / "ImageProcessing"
)

# Read input image
image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check image.jpg")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to float32
    gray = np.float32(gray)

    # Apply Harris corner detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Dilate corner response for visibility
    corners = cv2.dilate(corners, None)

    # Mark detected corners in red
    result = image.copy()
    result[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Save output image
    output_path = folder / "harris_corners.jpg"
    success = cv2.imwrite(str(output_path), result)

    if success:
        print("Corner detection output saved!")
        print("Saved at:", output_path)
    else:
        print("Failed to save the image.")

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Harris Corner Detection", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
