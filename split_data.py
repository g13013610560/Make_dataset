import json
import shutil

path = "E:/Dataset/manipulated_sequences/FaceShifter/c40/videos/"
path_dict = []

# with open("D:/PycharmProjects/Make_dataset/test.json",'r') as load_test:
#     load_dict = json.load(load_test)
#     print(load_dict)
#     print(len(load_dict))
#     for i in range(len(load_dict)):
#         # print(load_dict[i])
#         path_temp = path + str(load_dict[i][0]) + "_" + str(load_dict[i][1]) + ".mp4"
#         path_dict.append(path_temp)
#     print(path_dict)

# with open("D:/PycharmProjects/Make_dataset/train.json",'r') as load_test:
#     load_dict = json.load(load_test)
#     print(load_dict)
#     print(len(load_dict))
#     for i in range(len(load_dict)):
#         # print(load_dict[i])
#         path_temp = path + str(load_dict[i][0]) + "_" + str(load_dict[i][1]) + ".mp4"
#         path_dict.append(path_temp)
#     print(path_dict)


with open("D:/PycharmProjects/Make_dataset/val.json",'r') as load_test:
    load_dict = json.load(load_test)
    print(load_dict)
    print(len(load_dict))
    for i in range(len(load_dict)):
        # print(load_dict[i])
        path_temp = path + str(load_dict[i][1]) + "_" + str(load_dict[i][0]) + ".mp4"
        path_dict.append(path_temp)
    print(path_dict)



filepath = "E:/Dataset/manipulated_sequences/FaceShifter/c40/val"
for files in path_dict:
    shutil.move(files, filepath)