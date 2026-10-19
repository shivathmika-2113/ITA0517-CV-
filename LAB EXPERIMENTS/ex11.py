
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

# Read input image
image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check image.jpg")
else:
    # Rotate image by 180 degrees
    rotated = cv2.rotate(
        image, cv2.ROTATE_180
    )

    # Save the output image
    output_path = folder / "rotated180.jpg"
    success = cv2.imwrite(str(output_path), rotated)

    if success:
        print("Rotated image saved successfully!")
        print("Saved at:", output_path)
    else:
        print("Failed to save the image.")

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated 180 Degrees", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
