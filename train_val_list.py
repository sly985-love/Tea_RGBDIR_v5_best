
#####################################################################################################################################################


# python train.py --name 3a_yolov5s_improve  --data data/tea3_fusion/c2d_ir_depth_aw.yaml  --cfg models/axiaorong/yolov5s_improve.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth_aw.yaml    --weights /home/ps/rgbd/result/YOLOv5_improve/3a_yolov5s_improve/weights/best.pt --device 1;






# python train.py --name 3_yolov5s  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_yolov5s/weights/best.pt --device 1;

# python train.py --name 3_BH  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/BH.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_BH/weights/best.pt --device 1;

# python train.py --name 3_c3shnuted  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/c3shnuted.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_c3shnuted/weights/best.pt --device 1;

# python train.py --name 3_DSconv  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/DSconv.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_DSconv/weights/best.pt --device 1;

# python train.py --name 3_DSconv1  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/DSconv1.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_DSconv1/weights/best.pt --device 1;

# python train.py --name 3_DSconv2  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/DSconv2.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_DSconv2/weights/best.pt --device 1;


# python train.py --name 3_fpn  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/fpn.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_fpn/weights/best.pt --device 1;

# python train.py --name 3_fpna  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/fpna.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_fpna/weights/best.pt --device 1;

# python train.py --name 3_yolov5s_improve  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s_improve.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_yolov5s_improve/weights/best.pt --device 1;

# python train.py --name 3a_yolov5s  --data data/tea3_fusion/c2d_ir_depth_aw.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3a_yolov5s/weights/best.pt --device 1;

# python train.py --name 3a_yolov5s_improve  --data data/tea3_fusion/c2d_ir_depth_aw.yaml  --cfg models/axiaorong/yolov5s_improve.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3a_yolov5s_improve/weights/best.pt --device 1;


# mim install mmengine
# mim install "mmcv>=2.0.0"

# nv top
# ctrl shift P



# python train.py --name 3_yolov5s_26  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_yolov5s_262/weights/best.pt --device 1;

# python train.py --name 3_noFocus  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/noFocus.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_noFocus/weights/best.pt --device 1;

# python train.py --name 3_best_1  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_best_1/weights/best.pt --device 1;

# python train.py --name 3_best_2  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_best_2/weights/best.pt --device 1;

# python train.py --name 3a_yolov5s_26  --data data/tea3_fusion/c2d_ir_depth_aw.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth_aw.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3a_yolov5s_262/weights/best.pt --device 1;

# python train.py --name 3a_yolov5s_26_1  --data data/tea3_fusion/c2d_ir_depth_aw.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth_aw.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3a_yolov5s_26_1/weights/best.pt --device 1;

# python train.py --name 3a_best_1  --data data/tea3_fusion/c2d_ir_depth_aw.yaml  --cfg models/axiaorong/best.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth_aw.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3a_best_1/weights/best.pt --device 1;

# python train.py --name 3a_best_2  --data data/tea3_fusion/c2d_ir_depth_aw.yaml  --cfg models/axiaorong/best.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_fusion/c2d_ir_depth_aw.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3a_best_2/weights/best.pt --device 1;



# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# python train.py --name 3_best_dsconv  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_dsconv.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_best_dsconv/weights/best.pt --device 1;

# python train.py --name 3_best_c3shunted  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_c3shunted.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_best_c3shunted/weights/best.pt --device 1;

# python train.py --name 3_best_a  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_a.yaml  --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_best_a/weights/best.pt --device 1;

# python train.py --name 3_yolov5s_improve_27  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s_improve.yaml  --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_yolov5s_improve_27/weights/best.pt --device 1;

# hpy batchsize adamw

# python train.py --name 3_best_a_dsconv_l  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_a_dsconv.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_best_a_dsconv_l/weights/best.pt --device 1;

# python train.py --name 3_best_a_dsconv_m  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_a_dsconv.yaml   --epochs 2000  --batch-size 4   --device 1  --hyp  data/hyps/hyp.scratch-med.yaml;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_best_a_dsconv_m/weights/best.pt --device 1;

# python train.py --name 3_best_a_dsconv_h  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_a_dsconv.yaml   --epochs 2000  --batch-size 4   --device 1  --hyp  data/hyps/hyp.scratch-high.yaml;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_best_a_dsconv_h/weights/best.pt --device 1;


# python train.py --name 3_best_a_dsconv_8l  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_a_dsconv.yaml   --epochs 2000  --batch-size 8   --device 1;
# python val.py --data data/tea3_single/c2d.yaml    --weights /home/ps/rgbd/result/yolov5s_best/3_best_a_dsconv_8l/weights/best.pt --device 1;

# --hyp  data/hyps/hyp.scratch-med.yaml
# --hyp  data/hyps/hyp.scratch-high.yaml




#