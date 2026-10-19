
import cv2
from pathlib import Path

# Correct folder path
folder = (
    Path.home()
    / "OneDrive"
    / "Desktop"
    / "Computer Vision"
    / "ImageProcessing"
)

print("Folder exists:", folder.exists())

# Read input image
image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check image.jpg inside ImageProcessing.")
else:
    # Increase image size
    bigger = cv2.resize(
        image,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_LINEAR
    )

    # Decrease image size
    smaller = cv2.resize(
        image,
        None,
        fx=0.5,
        fy=0.5,
        interpolation=cv2.INTER_AREA
    )

    # Save output images
    cv2.imwrite(str(folder / "bigger.jpg"), bigger)
    cv2.imwrite(str(folder / "smaller.jpg"), smaller)

    print("Bigger image saved as bigger.jpg")
    print("Smaller image saved as smaller.jpg")

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
