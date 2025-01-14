import random
import os
import subprocess
import sys

def split_data_set(image_dir):

    f_val = open("test.txt", 'w')
    f_train = open("train.txt", 'w')
    
    path, dirs, files = next(os.walk(image_dir))
    data_size = len(files)

    ind = 0
    data_test_size = int(0.2 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)
    
    for f in os.listdir(image_dir):
        if(f.split(".jp")[1] == "g"):
            ind += 1
            
            if ind in test_array:
                f_val.write(image_dir+'/'+f+'\n')
            else:
                f_train.write(image_dir+'/'+f+'\n')

# 유동적 변경 필요!!
image_dir="images/images_200"

split_data_set(image_dir)
