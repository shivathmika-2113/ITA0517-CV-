
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
    height, width = image.shape[:2]

    # Four source points
    points1 = np.float32([
        [0, 0],
        [width - 1, 0],
        [0, height - 1],
        [width - 1, height - 1]
    ])

    # Four destination points
    points2 = np.float32([
        [50, 50],
        [width - 50, 0],
        [0, height - 50],
        [width - 1, height - 1]
    ])

    # Calculate perspective matrix
    matrix = cv2.getPerspectiveTransform(
        points1, points2
    )

    # Apply perspective transformation
    transformed = cv2.warpPerspective(
        image, matrix, (width, height)
    )

    # Save output image
    output_path = folder / "perspective.jpg"
    success = cv2.imwrite(str(output_path), transformed)

    if success:
        print("Perspective image saved successfully!")
        print("Saved at:", output_path)
    else:
        print("Failed to save the image.")

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformation", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
