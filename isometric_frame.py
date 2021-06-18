# -*- coding:utf8 -*-
import cv2
import os
import shutil


def get_frame_from_video(read_path, save_path, video_name, interval):
    """
    Args:
        video_name:输入视频名字
        interval: 保存图片的帧率间隔
    Returns:
    """

    # 保存图片的路径
    save_path = save_path + video_name.split(".")[0]
    is_exists = os.path.exists(save_path)
    if not is_exists:
        os.makedirs(save_path)
        print('path of %s is build' % save_path)
    else:
        shutil.rmtree(save_path)
        os.makedirs(save_path)
        print('path of %s already exist and rebuild' % save_path)

    # 开始读视频
    video_capture = cv2.VideoCapture(read_path)
    i = 0
    j = 0

    while True:
        success, frame = video_capture.read()
        i += 1
        if i % interval == 0:
            # 保存图片
            j += 1
            save_name = str(j) + '_' + str(i) + '.png'
            if frame is not None :
                cv2.imwrite(save_path + '/' + save_name, frame)
                # print('image of %s is saved' % save_name)
            else:
                break
        if not success:
            print('video is all read')
            break


if __name__ == '__main__':
    # 视频文件名字
    path = 'E:/frame test/videos/'
    save_path = 'E:/frame test/frames/'
    interval = 5

    files = os.listdir(path)
    print(files)
    for file in files :
        video_name = file
        # print(video_name)
        read_path = path + video_name
        get_frame_from_video(read_path, save_path, video_name, interval)

    # /data/data1/00DeepFakeDatasets/02FF++/videos/FaceShifter/raw/train
    # /data/data1/00DeepFakeDatasets/02FF++/ff++/FaceShifter/raw/train/