import cv2


def read_video(video_path):
    """
    Open a video file and display its frames.

    Args:
        video_path (str): Path to the video file.
    """

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video: {video_path}")
        return

    print("Video opened successfully.")
    print("Press Q to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Video ended or frame could not be read.")
            break

        cv2.imshow("ITMS - Video Test", frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    read_video("data/sample_traffic.mp4")