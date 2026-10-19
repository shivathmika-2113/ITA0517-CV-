
import cv2
from pathlib import Path

folder = Path(__file__).resolve().parent
video_path = str(folder / "video.mp4")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.mp4")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 25

    delay = max(1, int(1000 / fps))

    # Read and display each frame once
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video - Press Q to Exit", frame)

        key = cv2.waitKey(delay) & 0xFF
        if key == ord('q') or cv2.getWindowProperty(
            "Video - Press Q to Exit",
            cv2.WND_PROP_VISIBLE
        ) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Video finished. No replay.")

