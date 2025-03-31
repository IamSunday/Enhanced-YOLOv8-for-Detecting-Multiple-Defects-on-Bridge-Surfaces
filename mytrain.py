from ultralytics import YOLO
if __name__ == '__main__':

    model = YOLO("yolov8-CBAM.yaml")
    # model = YOLO("yolov8-GAM.yaml")
    # model = YOLO("yolov8-CA.yaml")
    # model = YOLO("yolov8-SE.yaml")
    # model = YOLO("yolov8n.pt")
    # model.load('yolov8n.pt')
    # Use the model
    results = model.train(data='F:/deep-learning-model/yolov8/ultralytics/data/qiaoliang.yaml',epochs=200,name='CBAM+WIoU')  
