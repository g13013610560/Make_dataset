import cv2
import os


path = 'E:/frame test/fs_real/test/'
dirs = os.listdir(path)
print(dirs)
for dir in dirs:
    dir_path = path + dir + '/'
    files = os.listdir(dir_path)
    for file in files :
        frame_path = dir_path +file
        frame = cv2.imread(frame_path)
        height, width,_ = frame.shape
        if not height == width:
            print(dir)
            break