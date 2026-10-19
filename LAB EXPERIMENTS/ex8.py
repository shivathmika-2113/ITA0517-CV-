
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

if not folder.exists():
    print("ImageProcessing folder not found!")
else:
    # Read the input image
    image = cv2.imread(str(folder / "image.jpg"))

    if image is None:
        print("Image not found! Check the image filename.")
    else:
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Convert to binary image
        _, binary = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )

        # Create kernel
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT, (5, 5)
        )

        # Apply dilation
        dilation = cv2.dilate(
            binary, kernel, iterations=1
        )

        # Save the output image
        output_path = folder / "dilation.jpg"
        success = cv2.imwrite(str(output_path), dilation)

        if success:
            print("Dilation image saved successfully!")
            print("Saved at:", output_path)
        else:
            print("Failed to save the image.")

        # Display images
        cv2.imshow("Original Image", image)
        cv2.imshow("Dilation Image", dilation)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
