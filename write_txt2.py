# print("sss")
import os

# # train val test

import os
# c2d_o c2d_ir_depth_o
# r"/home/ps/rgbd/data/data_RGBDIR_tea2/DataSet/c2d_ir_depth_addWeighted/train"

with open("train.txt", "w") as f:
    path = r"/home/ps/rgbd/data/data_RGBDIR_tea/DataSet/c2dup/train"
    for foldName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if ".png" in filename:
                line = str(os.path.join(foldName, filename))
                line = line + '\n'
                f.write(line)
with open("test.txt", "w") as f:
    path = r"/home/ps/rgbd/data/data_RGBDIR_tea/DataSet/c2dup/test"
    for foldName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            # filename=filename.split(".")[0]
            if ".png" in filename:
                line = str(os.path.join(foldName, filename))
                line = line + '\n'
                f.write(line)
with open("val.txt", "w") as f:
    path = r"/home/ps/rgbd/data/data_RGBDIR_tea/DataSet/c2dup/val"
    for foldName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            # filename=filename.split(".")[0]
            if ".png" in filename:
                line = str(os.path.join(foldName, filename))
                line = line + '\n'
                f.write(line)
# C:\Users\shuailuyu\AllTea\apple\DataSet\depth \infrared   jpg png
# train val test                                                                                train val test
# \c2d_depth_add c2d_depth_addWeighted c2d_depth_subtract c2d_ir_add c2d_ir_addWeighted \c2d_ir_depth_addWeighted
# \c2d_ir_subtract \rgba_depth \rgba_ir \rgba_ir_depth
