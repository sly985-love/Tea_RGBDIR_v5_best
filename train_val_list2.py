
#####################################################################################################################################################

# python train.py --name 3_best_all_1  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_best_all_1/weights/best.pt --device 1;

# python train.py --name 3_best_all_2  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_best_all_2/weights/best.pt --device 1;

# python train.py --name 3_yolov5s  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_yolov5s/weights/best.pt --device 1;

# python train.py --name 3_noFocus  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/noFocus.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_noFocus/weights/best.pt --device 1;

# python train.py --name 3_bh  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/bh.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_bh/weights/best.pt --device 1;

# python train.py --name 3_DSconv  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/DSconv.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_DSconv/weights/best.pt --device 1;

# python train.py --name 3_fpn  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/fpn.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_fpn/weights/best.pt --device 1;



# python train.py --name 3a_best_all_1  --data data/tea3_fusion/c2d_ir_depth.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3a_best_all_1/weights/best.pt --device 1;

# python train.py --name 3a_best_all_2  --data data/tea3_fusion/c2d_ir_depth.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3a_best_all_2/weights/best.pt --device 1;

# python train.py --name 3a_yolov5s  --data data/tea3_fusion/c2d_ir_depth.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3a_yolov5s/weights/best.pt --device 1;



# mim install mmengine
# mim install "mmcv>=2.0.0"

# nv top
# ctrl shift P



# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#