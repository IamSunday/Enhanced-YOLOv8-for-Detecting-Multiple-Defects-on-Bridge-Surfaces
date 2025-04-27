# Enhanced YOLOv8 for Detecting Multiple Defects on Bridge Surfaces

This repo contains the official **PyTorch** code for YOLOv8-Steel-Detection .
#Project Structure
Enhanced-YOLOv8-for-Detecting-Multiple-Defects-on-Bridge-Surfaces/
├── README.md              # Project documentation

├── environment.yml        # Conda environment dependencies

├── ultralytics/data/      # Directory for raw and processed datasets

├── ultralytics/cfg/models # Model architecture 

Please refer to https://docs.ultralytics.com/zh/models/yolov8/ for the detailed project structure

#Installation

git clone https://github.com/IamSunday/Enhanced-YOLOv8-for-Detecting-Multiple-Defects-on-Bridge-Surfaces.git cd Enhanced-YOLOv8-for-Detecting-Multiple-Defects-on-Bridge-Surfaces

#Usage

##Step 1: Prepare the Dataset

The bridge multi-defect data set for this experiment can be obtained from https://www.scidb.cn/en/s/fE3Uj2.

##Step 2: Model Training

python mytrain.py

## Dependencies

- Python 3.11
- torch == 2.3.1
- CUDA == 12.1
- torchvision == 0.18.1
- ultralytics == 8.3.33
- numpy == 1.26.3
- matplotlib == 3.9.0
- opencv-python == 4.10.0.84
- scipy == 1.13.1
- tqdm == 4.65.2
- ultralytics == 8.0.227
