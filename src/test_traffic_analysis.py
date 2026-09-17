import cv2
import time

from signal_simulator import SignalSimulator
from detector import VehicleDetector
from traffic_counter import TrafficCounter
from congestion import estimate_congestion
from dashboard import draw_dashboard


def main():
    video_path = "data/sample_traffic.mp4"

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    detector = VehicleDetector()
    counter = TrafficCounter()
    signal_simulator = SignalSimulator()

    previous_time = time.time()

    print("Traffic analysis started.")
    print("Press Q to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Video ended.")
            break

        # Detect and track vehicles
        detections = detector.detect(frame)

        # Count visible vehicles
        vehicle_count = counter.update(detections)

        # Estimate congestion
        congestion_level = estimate_congestion(
            vehicle_count
        )

        # Calculate recommended signal timing
        signal_info = signal_simulator.get_signal_status(
            congestion_level
        )

        green_time = signal_info["green_time"]

        # Calculate FPS
        current_time = time.time()
        elapsed_time = current_time - previous_time

        if elapsed_time > 0:
            fps = 1 / elapsed_time
        else:
            fps = 0

        previous_time = current_time

        # Draw vehicle detections
        for detection in detections:
            x1, y1, x2, y2 = detection["box"]

            tracking_id = detection["tracking_id"]
            class_name = detection["class_name"]
            confidence = detection["confidence"]

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            label = (
                f"ID: {tracking_id} "
                f"{class_name} {confidence:.2f}"
            )

            cv2.putText(
                frame,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Draw dashboard
        frame = draw_dashboard(
            frame,
            vehicle_count,
            congestion_level,
            green_time,
            fps,
            counter.total_frames
        )

        cv2.imshow(
            "ITMS - Traffic Analysis",
            frame
        )

        # Press Q to stop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Final statistics
    average_count = counter.get_average_vehicle_count()
    unique_vehicle_count = counter.get_unique_vehicle_count()

    print("\nTraffic analysis completed.")
    print(f"Processed frames: {counter.total_frames}")

    print(
        f"Average visible vehicle count: "
        f"{average_count:.2f}"
    )

    print(
        f"Unique vehicles observed: "
        f"{unique_vehicle_count}"
    )


if __name__ == "__main__":
    main()