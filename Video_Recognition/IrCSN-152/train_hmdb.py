import sys
import time
import os
import numpy as np
import torch
import torch.cuda as cuda
import torch.nn as nn
import torchvision
import requests

from model import VideoLearner 
from action_recognition.dataset import VideoRecord, VideoDataset
from common.gpu import system_info
from common.data import data_path, download

system_info()
sys.path.append("../")

# Number of consecutive frames used as input to the DNN. Recommended: 32 for high accuracy, 8 for inference speed.
MODEL_INPUT_SIZE = 32

# Config
BATCH_SIZE = 2
EPOCHS = 10
LR = 0.0001

DATA_ROOT = os.path.join(str(data_path()), "hmdb51")
VIDEO_DIR = os.path.join('D:/dataset/HMDB51/')

print(DATA_ROOT, '\n', VIDEO_DIR)

# /home/neuralworks/s_min/ircsn-152/ircsn-152/data/hmdb51/hmdb51_train_split_1.txt 
# /home/neuralworks/s_min/ircsn-152/ircsn-152/data/hmdb51/hmdb51_test_split_1.txt
TRAIN_SPLIT = os.path.join(DATA_ROOT, "hmdb51_train_split_1.txt")
TEST_SPLIT = os.path.join(DATA_ROOT, "hmdb51_test_split_1.txt")
print('TRAIN_SPLIT', TRAIN_SPLIT, '\nTEST_SPLIT', TEST_SPLIT) # TRAIN, TEST 절대 경로 반환됨


data = VideoDataset(
    VIDEO_DIR,
    train_split_file=TRAIN_SPLIT,
    test_split_file=TEST_SPLIT,
    batch_size=BATCH_SIZE,
    sample_length=MODEL_INPUT_SIZE,
    video_ext="avi",
)

print(
    f"Training dataset: {len(data.train_ds)} | Training DataLoader: {data.train_dl} \
    \nTesting dataset: {len(data.test_ds)} | Testing DataLoader: {data.test_dl}" ) # hmdb - 3570, 1530

print(f"""\
sample_length: {data.sample_length}
sample_step: {data.sample_step}
temporal_jitter: {data.temporal_jitter}
temporal_jitter_step: {data.temporal_jitter_step}
random_shift: {data.random_shift}
""")


learner = VideoLearner(data, num_classes=51)
print(learner.model.fc)

learner.fit(lr=LR, epochs=EPOCHS)

ret = learner.evaluate()

