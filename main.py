import os
import sys
import json

def get_label_featurelist_dict(path):
    with open(path) as f:
        lines = f.readlines()
        label_img_dict = dict()
        current_label = ''
        img_list = []
        i = 0
        class_num = 0

        test = []
        for line in lines:
            i = i + 1
            label = line.strip().split('/')[1]
            test.append(label)
            if label != current_label:
                class_num = class_num + 1
                if len(img_list) > 0:
                    label_img_dict[current_label] = img_list
                    img_list = []
                current_label = label
                img_list.append(line.strip())
                if i == len(lines):
                    label_img_dict[current_label] = img_list
            else:
                img_list.append(line.strip())
                if i == len(lines):
                    label_img_dict[current_label] = img_list
        return label_img_dict


if __name__ == '__main__':
    path = '/workspace/data/face-idcard-1M/face-idcard-1M-mtcnn-aligned-112x112/aligned_imgs/white_glass_img.lst' 
    img_list = []
    img_label = []

    img_dict = get_label_featurelist_dict(path)
    for key in img_dict:
        for i in range(len(img_dict[key])):
            img_list.append(img_dict[key][i])
            img_label.append(key)

    save_path = './white_glass_img.json'
    with open(save_path, 'w') as f2:
        save_dict = dict()
        save_dict['path'] = img_list
        save_dict['id'] = img_label
        json.dump(save_dict, f2)

        print('all: %d' % len(img_list))
