from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=3,
    imgsz=416,
    batch=8,
    patience=5,
    name="yaku_nawi"
)