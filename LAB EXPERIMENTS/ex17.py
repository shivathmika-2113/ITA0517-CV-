
import cv2
from pathlib import Path

folder = (
    Path.home() / "OneDrive" / "Desktop"
    / "Computer Vision" / "ImageProcessing"
)

image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check image.jpg")
else:
    # Copy the original image
    watermarked = image.copy()

    # Add watermark text
    cv2.putText(
        watermarked,
        "SHIVATHMIKA V",
        (20, image.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )

    # Save output
    cv2.imwrite(
        str(folder / "watermarked.jpg"), watermarked
    )
    print("Output saved as watermarked.jpg")

    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", watermarked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
