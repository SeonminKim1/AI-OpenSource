
## Pytorch YoloV4
- https://github.com/WongKinYiu/PyTorch_YOLOv4

## mish_cuda 
- https://github.com/thomasbrandon/mish-cuda // 다운로드후 setup.py 실행
- https://github.com/WongKinYiu/PyTorch_YOLOv4/issues/78 // 관련 설치 링크

## Train
- python train.py --batch-size 16 --img 416 416 --data kamp12.yaml --cfg cfg/yolov4.cfg --weights weights/yolov4.weights --name yolov4-kamp12

## Test
- python test.py --img 416 --conf 0.001 --batch 8 --data kamp12.yaml --cfg cfg/yolov4.cfg --weights runs/exp6_yolov4-kamp12/weights/best_yolov4-kamp12.pt --names yolov4-kamp12-test

```
┌YOLO V4 구조
│
├─core # YOLO V4 모듈
│  ├─backbone.py # backbone 모듈 (darknet53, cspdarknet53, darknet53_tiny, cspdarknet53_tiny)
│  ├─common.py # conv 함수 모듈 (convlotuional, mish, residual_block, route_group, upsample)
│  ├─config.py # config 사전 정의 파일들 (anchorbox, classes, train path, test_path, input_size ...)
│  ├─dataset.py # auto data augmentation 관련 
│  ├─utils.py # etc utils (load freeze layers, load_weights, load_config, get_anchor, image_preprocess, draw_bbox, bbox_iou, bbox_giou, bbox_ciou, NMS, freeze_all, unfreeze_all ...)
│  ├─yolov4.py # YOLO 모델 객체 생성 모듈 - YOLO v3, v4, tiny_v3, tiny_v4, decode_tf, decode_tflite, decode_trt, compute_loss ... 
│  
├────────────────────
├─data
│  ├─anchors # 
│  |  ├─baseline_anchors.txt
│  |  ├─baseline_tiny_anchors.txt
│  |  ├─yolov3_anchors.txt
│  |  ├─yolov4_anchors.txt
│  ├─classes # 
│  |  ├─**kamp12.names**
│  ├─dataset # 
│  |  ├─**kamp_images # kamp 이미지 (200장)**
│  |  |  ├─1.jpg, 2.jpg, 3.jpg ... 
│  |  |  ├─ ... 
│  |  ├─**kamp_labels # kamp 정답 파일(200개)**
│  |  |  ├─1.txt, 2.txt, 3.txt ... 
│  |  |  ├─ ... 
│  |  ├─**train.txt # splitdata.py로 분리된 train.txt (이미지 path)**
│  |  ├─**test.txt # splitdata.py로 분리된 test.txt (이미지 path)**
│
├─**splitdata.py # train, test set 분할** (kamp_images를 8:2 로 분할)**
├─**yolov4.weights # yolo weights 파일**
│  
├────────────────────
├─**checkpoints  # model storage**
│  |  ├─
│  |  ├─
│ 
├────────────────────
├─mAP  # mAP Score
│  ├─extra
│  |  ├─intersect-gt-and-pred.py
│  |  ├─remove_space.py
│  ├─main.py
│
├────────────────────
├─scripts  # etc file
│  ├─voc # voc data
│  |  ├─voc_covert.py / voc_make_names.py / get_voc2012.sh
│  ├─coco_annotation.py / coco_convert.py / google_utils.py / voc_annotation.py # 
│  
├────────────────────
├─train.py # train code
├─detect.py # experiment code
├─evaluate.py # test code
├─benchmarks.py
│
├────────────────────
├─save_model.py # weights(checkpoint) to tensorflow pb model
├─convert_tflite.py # pb to tflite
│
├────────────────────
├─requirements.txt
├─requirements-gpu.txt
│
└────────────────────

```
