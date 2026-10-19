
import cv2
from pathlib import Path

# Get the folder where this Python program is saved
folder = Path(__file__).resolve().parent

# Read the input image
image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check image.jpg")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(image, (15, 15), 0)

    # Save the output image
    output_path = folder / "blur.jpg"
    success = cv2.imwrite(str(output_path), blur)

    if success:
        print("Blurred image saved successfully!")
        print(output_path)
    else:
        print("Failed to save the image.")

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blur Image", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
