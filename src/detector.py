from ultralytics import YOLO


class VehicleDetector:
    def __init__(
        self,
        model_path="models/yolo26n.pt",
        confidence=0.4
    ):
        """
        Load the pretrained YOLO model.
        """

        self.model = YOLO(model_path)
        self.confidence = confidence

        # COCO vehicle class IDs
        self.vehicle_classes = {
            2: "car",
            3: "motorcycle",
            5: "bus",
            7: "truck"
        }

    def detect(self, frame):
        """
        Detect and track vehicles in one video frame.

        Returns:
            List of vehicle detections with tracking IDs.
        """

        results = self.model.track(
            frame,
            conf=self.confidence,
            persist=True,
            verbose=False
        )

        detections = []

        result = results[0]

        if result.boxes is None:
            return detections

        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            if class_id not in self.vehicle_classes:
                continue

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0].tolist()
            )

            class_name = self.vehicle_classes[class_id]

            # Tracking ID may not exist for every detection
            if box.id is not None:
                tracking_id = int(box.id[0])
            else:
                tracking_id = -1

            detections.append({
                "tracking_id": tracking_id,
                "class_name": class_name,
                "confidence": confidence,
                "box": (x1, y1, x2, y2)
            })

        return detections