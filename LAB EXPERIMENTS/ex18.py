
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
    height, width = image.shape[:2]

    # Select a region that fits the image
    roi_width = width // 4
    roi_height = height // 4

    if roi_width == 0 or roi_height == 0:
        print("Image is too small.")
    else:
        x, y = width // 4, height // 4

        # Crop and copy the region
        roi = image[y:y + roi_height, x:x + roi_width]
        result = image.copy()

        # Paste the region at a different location
        paste_x = width - roi_width
        paste_y = height - roi_height

        result[
            paste_y:paste_y + roi_height,
            paste_x:paste_x + roi_width
        ] = roi

        # Save output
        cv2.imwrite(str(folder / "roi_copy_paste.jpg"), result)
        cv2.imwrite(str(folder / "cropped_roi.jpg"), roi)

        print("Saved roi_copy_paste.jpg")
        print("Saved cropped_roi.jpg")

        cv2.imshow("Original Image", image)
        cv2.imshow("Cropped ROI", roi)
        cv2.imshow("ROI Copy and Paste", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
