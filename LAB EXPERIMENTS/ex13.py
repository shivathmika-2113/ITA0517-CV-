
import cv2
import numpy as np
from pathlib import Path

# Correct folder path
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
    height, width = image.shape[:2]

    # Select three points from the original image
    points1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    # Define corresponding destination points
    points2 = np.float32([
        [10, 100],
        [200, 50],
        [100, 250]
    ])

    # Calculate affine transformation matrix
    matrix = cv2.getAffineTransform(points1, points2)

    # Apply affine transformation
    transformed = cv2.warpAffine(
        image, matrix, (width, height)
    )

    # Save output image
    output_path = folder / "affine.jpg"
    success = cv2.imwrite(str(output_path), transformed)

    if success:
        print("Affine image saved successfully!")
        print("Saved at:", output_path)
    else:
        print("Failed to save the image.")

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformation", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
