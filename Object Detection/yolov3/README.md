

## YOLO v3
- github : https://github.com/ultralytics/yolov3

## 1. 파일 리스트
- Data
    - images/ : 실제 이미지 파일들
    - labels/ : 이미지 파일의 bounding box 및 class
    - splitdata.py를 통해 분리
        - train.txt
        - test.txt

- Model info
    - weights/ : 학습 가중치 저장 모델
    - classes.names
    - custom.data
    - yolov3-spp.cfg
    
- Module
    - utils/
    - models.py

- Test
    - result : 추론 결과 파일들

- python module
    - train.py
    - test.py
    - detect.py

## 2. train.txt, test.txt 생성
- splitdata.py를 통한 train.txt, test.txt 생성
- custom.data 파일 내용 수정

## 3. 모델 학습 및 추론
- 기본적으로 train.py + 인자를 통한 옵션 셋팅
    - --cfg : config 파일
    - --data : custom.data, custom_classes 파일 (하나로 합쳐도 됨)
    - --weights : last.pt
    - train.txt 및 해당 .txt에 기록된 image 경로들 필요 (labels 폴더도 마찬가지)
    - **주의사항) images 폴더와 labels 폴더의 이름이 같아야 됨.**
        - ex) images_200/ 밑에 png 파일들 존재 ==> labels_200/ 있어야 함 

## 3-1. 학습 명령어
- python train.py --epochs 100 --weights weights/last.pt --batch-size 8  --cfg yolov3-spp.cfg --data custom.data --nosave
- 기존에 있는 모델 집어넣으면 이어서 학습 가능

## 3-2. 추론 명령어
- python test.py --cfg yolov3-spp.cfg --batch-size 3 --data custom.data --weights weights/last.pt

## 4. Detect KAMP x-ray reader detection
- python train.py --epochs 100 --weights weights/KAMP_X-ray_model.pt --batch-size 8  --cfg yolov3-spp.cfg --data custom.data --nosave

- python test.py --cfg yolov3-spp.cfg --batch-size 3 --data custom.data --weights weights/KAMP_X-ray_model.pt

