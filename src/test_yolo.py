from ultralytics import YOLO


# Load a small pretrained YOLO model
model = YOLO("models/yolo26n.pt")

print("YOLO model loaded successfully.")