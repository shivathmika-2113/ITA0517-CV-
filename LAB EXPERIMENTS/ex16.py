
import cv2
import numpy as np
from pathlib import Path

folder = (
    Path.home() / "OneDrive" / "Desktop"
    / "Computer Vision" / "ImageProcessing"
)

image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check image.jpg")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Sobel edge detection
    sobel_x = cv2.Sobel(
        gray, cv2.CV_64F, 1, 0, ksize=3
    )
    sobel_y = cv2.Sobel(
        gray, cv2.CV_64F, 0, 1, ksize=3
    )

    # Combine X and Y edges
    magnitude = cv2.magnitude(sobel_x, sobel_y)
    output = cv2.convertScaleAbs(magnitude)

    # Save output
    cv2.imwrite(str(folder / "sobel.jpg"), output)
    print("Output saved as sobel.jpg")

    cv2.imshow("Original Image", image)
    cv2.imshow("Sobel Edge Detection", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
