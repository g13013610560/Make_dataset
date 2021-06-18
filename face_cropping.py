from face_utils import norm_crop, FaceDetector
import os
import torch
import cv2
import shutil

# /data/data1/00DeepFakeDatasets/02FF++/ff++/FaceShifter/c40/val/
# /data/data1/04GuFei/FaceShifter/c40/val/

#路径
path = '/data/data1/00DeepFakeDatasets/02FF++/ff++/FaceShifter/c40/val/'
save_path_dir = '/data/data1/04GuFei/FaceShifter/c40/val/'

#裁剪工具
face_detector = FaceDetector()
face_detector.load_checkpoint("RetinaFace-Resnet50-fixed.pth")
torch.set_grad_enabled(False)
scale=1.4


dirs = os.listdir(path)
print(dirs)
for dir in dirs:
    dir_path = path + dir + '/'

    save_path = save_path_dir + dir + '/'
    is_exists = os.path.exists(save_path)
    if not is_exists:
        os.makedirs(save_path)
        print('path of %s is build' % save_path)
    else:
        shutil.rmtree(save_path)
        os.makedirs(save_path)
        print('path of %s already exist and rebuild' % save_path)

    files = os.listdir(dir_path)
    for file in files :
        frame_path = dir_path +file
        frame = cv2.imread(frame_path)
        height, width,_ = frame.shape
        boxes, landms = face_detector.detect(frame)
        areas = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])
        if areas.shape == torch.Size([0]):
          continue
        order = areas.argmax()
        boxes = boxes[order]
        l, t, r, b = boxes.tolist()
        h = b - t
        w = r - l
        maxl = int(max(h, w) * scale)
        centerx = (t + b) / 2
        centery = (l + r) / 2
        startx = centerx - maxl // 2
        starty = centery - maxl // 2
        if maxl > height:
            maxl = height
        if maxl > width:
            maxl = width
        if startx <= 0:
            startx = 0
        if startx + maxl >= height:
            startx = height - maxl
        if starty <= 0:
            starty = 0
        if starty + maxl >= width:
            starty = width - maxl
        startx, starty = int(startx), int(starty)
        face = frame[startx:startx + maxl, starty:starty + maxl, :]
        cv2.imwrite(save_path + file, face)
        # print(file + 'has been cropped')




