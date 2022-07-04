'''
Author: Rane wang_ran20121
Date: 2022-07-04 19:12:57
LastEditors: Rane wang_ran20121
LastEditTime: 2022-07-04 20:15:59
FilePath: /10_coco_label_tool/03_change_type3.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import json
from tqdm import tqdm
import argparse


if __name__ == '__main__':
    label_txt = \
    "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Fanyingshi/ip142_data/train_v4_change_type3/ip142_train_v2_addtype3_4/label_ori.txt"
    save_txt = \
    "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Fanyingshi/ip142_data/train_v4_change_type3/ip142_train_v2_addtype3_4/label_change_type3.txt"
    
    chnage_type = "3.0000"
    
    
    if os.path.exists(save_txt):
        os.remove(save_txt)
    with open(save_txt, "a") as sf:
        with open(label_txt, "r") as rf:
            _line = "start..."
            while len(_line) > 5:
                _line = rf.readline()
                line = _line[:-1]
                line = line.split(" ")
                
                count_type = 0
                more_type_inx = []
                for inx in range(len(line)-1, 0, -5):  # 最后那个type默认是需要的
                    if line[inx] == chnage_type:
                        count_type += 1
                    if count_type > 1:
                        more_type_inx.append(inx)
                        count_type -= 1
                for m_inx in more_type_inx:
                    for pinx in range(m_inx, m_inx-5, -1):
                        line.pop(pinx)
                
                info = ''
                for l in range(len(line)):
                    if l  == len(line)-1:
                        info += line[l] + "\r"
                    else:
                        info += line[l] + " "
                sf.write(info)

    print("finish!")



