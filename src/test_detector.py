import cv2

from detector import VehicleDetector


def main():
    video_path = "data/sample_traffic.mp4"

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    detector = VehicleDetector()

    print("Vehicle detection started.")
    print("Press Q to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Video ended.")
            break

        detections = detector.detect(frame)

        for detection in detections:
            x1, y1, x2, y2 = detection["box"]
            class_name = detection["class_name"]
            confidence = detection["confidence"]

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Prepare label
            label = f"{class_name} {confidence:.2f}"

            # Draw label
            cv2.putText(
                frame,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Display number of detected vehicles
        cv2.putText(
            frame,
            f"Vehicles: {len(detections)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

        cv2.imshow("ITMS - Vehicle Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()