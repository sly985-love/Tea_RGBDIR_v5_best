
#####################################################################################################################################################

# python train.py --name 3_best_all_1_apre  --weights  /home/ps/rgbd/result/yolov5_best_27/a_best/weights/best.pt  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_best_all_1_apre/weights/best.pt --device 1;

# python train.py --name 3_yolov5s_apre --weights  /home/ps/rgbd/result/yolov5_best_27/a_yolov5s/weights/best.pt --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_yolov5s_apre/weights/best.pt --device 1;



# python train.py --name 3a_best_all_1_aprel --weights  /home/ps/rgbd/result/yolov5_best_27/a_a1_best/weights/best.pt --data data/tea3_fusion/c2d_ir_depth.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_fusion/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3a_best_all_1_aprel/weights/best.pt --device 1;

# python train.py --name 3a_yolov5s_aprel --weights  /home/ps/rgbd/result/yolov5_best_27/a_a1_yolov5s/weights/best.pt --data data/tea3_fusion/c2d_ir_depth.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_fusion/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3a_yolov5s_aprel/weights/best.pt --device 1;


#####################################################################################################################################################

# python train.py --name 3_best_all_1_aprep  --weights  /home/ps/rgbd/result/yolov5_best_27/ap_best/weights/best.pt  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_best_all_1_aprep/weights/best.pt --device 1;

# python train.py --name 3_yolov5s_aprep --weights  /home/ps/rgbd/result/yolov5_best_27/ap_yolov5s/weights/best.pt --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_yolov5s_aprep/weights/best.pt --device 1;


# python train.py --name 3_best_all_1_apreo  --weights  /home/ps/rgbd/result/yolov5_best_27/ao_best/weights/best.pt  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_best_all_1_apreo/weights/best.pt --device 1;

# python train.py --name 3_yolov5s_apreo --weights  /home/ps/rgbd/result/yolov5_best_27/ao_yolov5s/weights/best.pt --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3_yolov5s_apreo/weights/best.pt --device 1;




# python train.py --name 3a_best_all_1_aprelp --weights  /home/ps/rgbd/result/yolov5_best_27/ap_a1_best/weights/best.pt --data data/tea3_fusion/c2d_ir_depth.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_fusion/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3a_best_all_1_aprelp/weights/best.pt --device 1;

# python train.py --name 3a_yolov5s_aprelp --weights  /home/ps/rgbd/result/yolov5_best_27/ap_a1_yolov5s/weights/best.pt --data data/tea3_fusion/c2d_ir_depth.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_fusion/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3a_yolov5s_aprelp/weights/best.pt --device 1;

# python train.py --name 3a_best_all_1_aprelo --weights  /home/ps/rgbd/result/yolov5_best_27/ao_a1_best/weights/best.pt --data data/tea3_fusion/c2d_ir_depth.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3a_best_all_1_aprelo/weights/best.pt --device 1;

# python train.py --name 3a_yolov5s_aprelo --weights  /home/ps/rgbd/result/yolov5_best_27/ao_a1_yolov5s/weights/best.pt --data data/tea3_fusion/c2d_ir_depth.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/3a_yolov5s_aprelo/weights/best.pt --device 1;

# mim install mmengine
# mim install "mmcv>=2.0.0"

# nv top
# ctrl shift P



# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#