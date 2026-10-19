
import cv2
from pathlib import Path

folder = Path(__file__).resolve().parent
image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check image.jpg")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    erosion = cv2.erode(binary, kernel, iterations=1)

    cv2.imwrite(str(folder / "erosion.jpg"), erosion)
    print("Erosion output saved as erosion.jpg")

    cv2.imshow("Original Image", image)
    cv2.imshow("Erosion", erosion)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
