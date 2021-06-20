# SSD: Single Shot MultiBox Object Detector, in PyTorch

## Source 원본 링크
- https://github.com/amdegroot/ssd.pytorch
- 원본 소스를 바탕으로 수정해보고 싶을 시 아래 issue목록을 참조
- 소스코드에 있는 Path는 절대 Path가 많음. 현재 코드는 VOC2012 에 최적화 되어있음, 유의하면서 수정필요
<hr>

## Dataset 준비
- Train/validation Data + Test Data 다운로드
    - 압축같은 폴더에 풀기
- https://pjreddie.com/projects/pascal-voc-dataset-mirror/


### Directory Structure
```
┌─SSD (Single Shot MultiBox Object Detector)
├─VOCdevkit
│  ├── VOC2012
│  │  ├─ Annotations : 2007_000027.xml... , 22263개
│  │  ├─ ImageSets  # 
│  │  │  ├ Action  # jumping_test.txt ..., 44개
│  │  │  ├ Layout  # train.txt, val.txt, trainval.txt, test.txt, 4개
│  │  │  ├ Main  # bird.txt ... , 84개
│  │  │  └ Segmentation  
│  │  ├─ JPEGImages  # 2007_000027.jpg ... , 33260개
│  │  ├─ SegmentationClass  # 
│  │  └─ SegmentationObject  #
└────────────────────
```

## Weights 준비
- mkdir weights
- wget https://s3.amazonaws.com/amdegroot-models/vgg16_reducedfc.pth

<hr>

## Issue 목록
- 해당 Issue들은, 원본 링크에 Issue들을 뒤져가며 해결한 방법을 적어놓음.

### 1. train.py - index issue
- 오류내용 : 1. layers/modules/multibox_loss.py In line 97, loss_c[pos]=0, the shape of mask [32,8732] ar index 0 not match the shape of the indexed tensor [270424,1] at index 0 issue
- 문제점 및 해결방안
    - pytorch 구버전 문법
    - https://github.com/amdegroot/ssd.pytorch/issues/421#issuecomment-545861899

### 2. train.py - stopiteration issue
- 오류내용 : 한 epoch이 다 돈 후에 raise stopiteration 발생
- 문제점 및 해결방안
    - dataloader 과정에서의 1epoch 데이터를 다 꺼내와서 다시 채워줘야 하는 .
    - try-except로 해결
    - https://github.com/amdegroot/ssd.pytorch/issues/393

### 3. ssd.py -> detect 
- 오류내용 : autograd non-static ~ 
- 문제점 및 해결방안
    - forward 방식 수정
    - https://github.com/amdegroot/ssd.pytorch/issues/444

### 4. eval.py - dataset problem
- 오류내용 : No such file or directory: 'VOCdevkit/VOC2012/Annotations/2008_000001
- 문제점 및 해결방안
    - voc2007은 test.txt / voc2012는 val.txt 가 맞음.
    - val.txt 로 수정

### 5. eval.py - imageset-val.txt 
- 오류내용 : FileNotFoundError: [Errno 2] No such file or directory: 'val.txt'
- 문제점 및 해결방안
    - https://github.com/amdegroot/ssd.pytorch/issues/350
    - imgsetpath = os.path.join(args.voc_root, 'VOC2007', 'ImageSets', 'Main', '{}.txt') 로 수정

<hr>

## Training
- python train.py

## Evaluation
- python eval.py