## YOLO V5 - 이미지 train valid split 코드

from glob import glob

# get image list
train_img_list = glob('train/images/*.jpg')
valid_img_list = glob('valid/images/*.jpg')

print(len(train_img_list), len(valid_img_list))

with open('train.txt', 'w') as f:
    f.write('\ndata/mask_data/'.join(train_img_list)+'\n')

with open('val.txt', 'w') as f:
    f.write('\ndata/mask_data/'.join(valid_img_list)+'\n')

import yaml

with open('data.yaml', 'r') as f:
    data = yaml.load(f)

data['train'] = 'data/mask_data/train.txt'
data['val'] = 'data/mask_data/val.txt'

with open('data.yaml', 'w') as f:
    yaml.dump(data, f)

print(data)
