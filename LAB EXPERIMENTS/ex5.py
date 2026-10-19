
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

folder = Path(__file__).resolve().parent
image = cv2.imread(str(folder / "image.jpg"))

if image is None:
    print("Image not found! Check image.jpg")
else:
    colors = ('b', 'g', 'r')
    labels = ('Blue', 'Green', 'Red')

    for color, label in zip(colors, labels):
        histogram = cv2.calcHist(
            [image], [colors.index(color)], None, [256], [0, 256]
        )
        plt.plot(histogram, color=color, label=label)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.legend()
    plt.savefig(str(folder / "color_histogram.png"))
    print("Histogram saved as color_histogram.png")
    plt.show()
