# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:15:49 2023

@author: minni
"""

import os
os.mkdir('CS')
with open(os.path.join('CS','homework.txt'),'w') as file:
    file.write('4112029009_顏逸仙\n')
with open(os.path.join("CS", "homework.txt"), "r") as file:
    file_content = file.read()
    print('文件内容:', file_content)

import os
import time

file_size=os.path.getsize(os.path.join('CS','homework.txt'))
print(f'文件大小:{file_size}字節')

modification_time=os.path.getmtime(os.path.join('CS','homework.txt'))
print(f'最後修改時間:{modification_time}')

formatted_time=time.ctime(modification_time)
print(f'最後修改時間(人類可讀格式):{formatted_time}')

import os
if os.path.exists('homework.txt'):
    os.remove('homework.txt')
    
import os
import shutil
shutil.rmtree('CS')
