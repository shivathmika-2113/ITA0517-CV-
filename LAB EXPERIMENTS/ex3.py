
import cv2
from pathlib import Path

# Get the folder where this Python program is saved
folder = Path(__file__).resolve().parent

# Read the input image
image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check image.jpg")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Save the output image
    output_path = folder / "edges.jpg"
    success = cv2.imwrite(str(output_path), edges)

    if success:
        print("Edge image saved successfully!")
        print(output_path)
    else:
        print("Failed to save the image.")

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Detection", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
