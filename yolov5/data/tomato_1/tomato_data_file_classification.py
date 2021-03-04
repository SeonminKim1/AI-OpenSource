
from glob import glob

# get image list
img_list = glob('images/*.png')

from sklearn.model_selection import train_test_split

train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=7)
print(len(train_img_list), len(val_img_list))

with open('train.txt', 'w+') as f:
    f.write('\ndata/tomato_1/'.join(train_img_list)+'\n')

with open('val.txt', 'w+') as f:
    f.write('\ndata/tomato_1/'.join(val_img_list)+'\n')

import yaml

with open('data.yaml', 'r') as f:
    data = yaml.load(f)

data['train'] = 'data/tomato_1/train.txt'
data['val'] = 'data/tomato_1/val.txt'

with open('data.yaml', 'w') as f:
    yaml.dump(data, f)

print(data)
