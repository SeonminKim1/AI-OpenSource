

## ■ YOLO v5
- Github : https://github.com/ultralytics/yolov5
- Dataset: https://public.roboflow.com/
- Ref : https://www.youtube.com/watch?v=T0DO1C8uYP8&list=PL-xmlFOn6TULrmwkXjRCDAas0ixd_NtyK&index=10

## ■ 0. YOLO v5 Directory Structure

```
┌YOLO-v5 Directory Structure
│
├─models # YOLO v5 models module
│  ├─ yolo.py
│  └─ .... py
│
├─utils # YOLO v5 utils module
│  ├─ loss, metrics.py 
│  ├─ torch_utils.py
│  └─ .... py
│
├────────────────────
├─data (own github version)
│  ├─plant_data (proj name)
│  │  ├─images
│  │  │  ├─ plant_train.png
│  │  │  └─ ....._train.png
│  │  ├─labels
│  │  │  ├─ plant_label.txt
│  │  │  └─ ....._label.txt
│  │  ├─test_images (pred image)
│  │  │  ├─ plant_test.png
│  │  │  └─ ....._test.png
│  │  │  
│  │  ├─plantdata_file_classification.py 
│  │  ├─data.yaml # (made by plantdata_file_classification.py)
│  │  ├─train.txt # (made by plantdata_file_classification.py)
│  │  └─val.txt # (made by plantdata_file_classification.py)
│
├────────────────────
├─runs (train and test result) 
│  ├─train (train.py result)
│  │  └─weights.pt / hyp.yaml / opt.yaml / etc..
│  ├─detect (detect.py result)
│  │  └─test_images_result.png
├─weights (default weights)
│  └─yolov5s.pt
│  
├────────────────────
├─train.py
├─detect.py
├─test.py
├─requirements.txt
│  
└────────────────────
```

<hr>

### ■ 1. Environment Setting
    - pip install -r requirements.txt

### ■ 2. Folder:data setting
- xxx_data 
    - images (전체 이미지 파일들)
    - labels (전체 box라벨 파일들)
    - test_images (test 이미지 파일들)
    - xxx_file_classification.py (train.txt, val.txt 생성용)
    - data.yaml (made by xxx_file_classification.py)
    - train.txt (made by xxx_file_classification.py)
    - val.txt (xxx_file_classification.py)

### ■ 3. train.txt, val.txt, data.yaml 생성
    - python xxx_file_classification.py
        - train.txt, val.txt 생성
        - data.yaml 파일 내용 수정

### ■ 3-1. data.yaml 체크
- names : class names / - 형태 or  [' '] 둘다 가능 
- nc : 30 (num_classes라는 뜻)

- 학습, 검증 데이터 이미지 파일 경로
    - train: plant_data/train.txt 
    - val: plant_data/val.txt

### ■ 4. 모델 학습 (model, weights)
- 기본적으로 train.py + 인자를 통한 옵션 셋팅
- img, batch, epochs, data : data.yaml 파일
- config(cfg) 사항은 models/의 yolov5s.yaml , yolov5m.yaml, yolov5l.yaml, yolov5x.yaml 중 선택
- 가중치는 weights/yolov5s.pt, yolov5m.pt, yolov5l.pt, yolov5x.yaml 중 선택 (download)

<hr>

### ■ Case 1. Detect Plant
- train 명령어
    - python train.py --img 416 --batch 16 --epochs 100 --data ./data/plant_data/data.yaml --cfg ./models/yolov5s.yaml --weights ./weights/yolov5s.pt --name result_plant

- test 명령어
    - python detect.py --weights ./runs/train/plant_yolo5_result/weights/best.pt --img 416 --conf 0.5 --source ./plant_data/test_images/ --name plant


### ■ Case 2. Detect Gun 
- train 명령어
    - python train.py --img 416 --batch 16 --epochs 50 --data ./data/gun_data/data.yaml --cfg ./models/yolov5s.yaml --weights ./weights/yolov5s.pt --name result_gun

- test 명령어
    - python detect.py --weights ./runs/train/gun_yolo_result12/weights/best.pt --img 416 --conf 0.5 --source ./data/gun_data/test_images/ --name gun

### ■ Case 3. Detect Mask vs NO-mask
- train 명령어
    - python train.py --img 416 --batch 16 --epochs 100 --data ./data/mask_data/data.yaml --cfg ./models/yolov5s.yaml --weights ./weights/yolov5s.pt --name result_mask_nonmask

- test 명령어
    - python detect.py --weights ./runs/train/mask_yolo5_result/weights/best.pt --img 416 --conf 0.5 --source ./data/mask_data/test_images/ --name mask

    
### ■ Case 4. Detect tomato diseases leaf
- train 명령어
    - python train.py --img 416 --batch 2 --epochs 100 --data ./data/tomato_1/data.yaml --cfg ./models/yolov5s.yaml --weights ./weights/yolov5s.pt --name result_tomato_disease

- test 명령어
    - python detect.py --weights ./runs/train/tomato_1_yolov5/weights/best.pt --img 416 --conf 0.5 --source ./data/tomato_1/test_images/ --name tomato