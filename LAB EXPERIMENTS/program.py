
import cv2
from pathlib import Path

# Get the folder where this Python program is saved
folder = Path(__file__).resolve().parent

# Read the image
image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check whether image.jpg is in this folder.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the output in the same folder
    output_path = folder / "grayscale.jpg"
    success = cv2.imwrite(str(output_path), gray)

    if success:
        print("Image saved successfully at:")
        print(output_path)
    else:
        print("Image could not be saved.")

    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
