## YOLO V5 - 이미지 train valid split 코드

from glob import glob

# get image list
img_list = glob('images/*.jpg')

from sklearn.model_selection import train_test_split

train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=7)
print(len(train_img_list), len(val_img_list))


with open('train.txt', 'w') as f:
    f.write('\ndata/plant_data/'.join(train_img_list)+'\n')

with open('val.txt', 'w') as f:
    f.write('\ndata/plant_data/'.join(val_img_list)+'\n')

import yaml

with open('data.yaml', 'r') as f:
    data = yaml.load(f)

data['train'] = 'data/plant_data/train.txt'
data['val'] = 'data/plant_data/val.txt'

with open('data.yaml', 'w') as f:
    yaml.dump(data, f)

print(data)
