import csv
import os
from datetime import datetime


class TrafficCounter:
    def __init__(self, output_path="outputs/traffic_log.csv"):
        """
        Initialize traffic counter and CSV logging.
        """

        self.total_frames = 0
        self.total_vehicle_detections = 0

        # Store unique tracking IDs
        self.unique_vehicle_ids = set()

        self.output_path = output_path

        os.makedirs(
            os.path.dirname(self.output_path),
            exist_ok=True
        )

        with open(
            self.output_path,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)

            writer.writerow([
                "timestamp",
                "frame_number",
                "visible_vehicle_count",
                "unique_vehicle_count"
            ])

    def update(self, detections):
        """
        Update traffic statistics using current detections.
        """

        current_vehicle_count = len(detections)

        self.total_frames += 1
        self.total_vehicle_detections += current_vehicle_count

        # Add tracking IDs to the set
        for detection in detections:
            tracking_id = detection.get("tracking_id", -1)

            if tracking_id != -1:
                self.unique_vehicle_ids.add(tracking_id)

        unique_vehicle_count = len(self.unique_vehicle_ids)

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open(
            self.output_path,
            mode="a",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)

            writer.writerow([
                timestamp,
                self.total_frames,
                current_vehicle_count,
                unique_vehicle_count
            ])

        return current_vehicle_count

    def get_average_vehicle_count(self):
        """
        Calculate average visible vehicles per frame.
        """

        if self.total_frames == 0:
            return 0

        return (
            self.total_vehicle_detections
            / self.total_frames
        )

    def get_unique_vehicle_count(self):
        """
        Return the number of unique tracking IDs observed.
        """

        return len(self.unique_vehicle_ids)