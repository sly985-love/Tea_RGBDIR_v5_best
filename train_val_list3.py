
#####################################################################################################################################################

# python train.py --name a_yolov5s  --data data/apple/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data  data/apple/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/a_yolov5s/weights/best.pt --device 1;

# python train.py --name a_best  --data data/apple/c2d.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data  data/apple/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/a_best/weights/best.pt --device 1;

# python train.py --name a_a1_yolov5s  --data data/apple/c2d_ir_depth.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data  data/apple/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/a_a1_yolov5s/weights/best.pt --device 1;

# python train.py --name a_a1_best  --data data/apple/c2d_ir_depth.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data  data/apple/c2d_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/a_a1_best/weights/best.pt --device 1;

# python train.py --name a_a2_yolov5s  --data data/apple/rgb_ir_depth.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data  data/apple/rgb_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/a_a2_yolov5s/weights/best.pt --device 1;

# python train.py --name a_a2_best  --data data/apple/rgb_ir_depth.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data  data/apple/rgb_ir_depth.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/a_a2_best/weights/best.pt --device 1;



# python train.py --name k_yolov5s  --data data/kiwi/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/kiwi/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/k_yolov5s/weights/best.pt --device 1;

# python train.py --name k_best  --data data/kiwi/c2d.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/kiwi/c2d.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/k_best/weights/best.pt --device 1;

# python train.py --name k_a1_yolov5s  --data data/kiwi/c2d_ir.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/kiwi/c2d_ir.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/k_a1_yolov5s/weights/best.pt --device 1;

# python train.py --name k_a1_best  --data data/kiwi/c2d_ir.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/kiwi/c2d_ir.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/k_a1_best/weights/best.pt --device 1;



#####################################################################################################################################################


# python train.py --name ao_yolov5s  --data data/apple/c2d_o.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/apple/c2d_o.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/ao_yolov5s/weights/best.pt --device 1;

# python train.py --name ao_best  --data data/apple/c2d_o.yaml --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/apple/c2d_o.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/ao_best/weights/best.pt --device 1;

# python train.py --name ap_yolov5s  --data data/apple/c2d_p.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/apple/c2d_p.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/ap_yolov5s/weights/best.pt --device 1;

# python train.py --name ap_best  --data data/apple/c2d_p.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/apple/c2d_p.yaml    --weights /home/ps/rgbd/result/yolov5_best_27/ap_best/weights/best.pt --device 1;




# python train.py --name ao_a1_yolov5s  --data data/apple/c2d_ir_depth_o.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;

# python train.py --name ao_a1_best  --data data/apple/c2d_ir_depth_o.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;

# python train.py --name ap_a1_yolov5s  --data data/apple/c2d_ir_depth_p.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;

# python train.py --name ap_a1_best  --data data/apple/c2d_ir_depth_p.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;


# mim install mmengine
# mim install "mmcv>=2.0.0"

# nv top
# ctrl shift P





# python train.py --name tea2p_yolov5s  --data data/apple/c2d_tea2p.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;

# python train.py --name tea2p_best  --data data/apple/c2d_tea2p.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;


# python train.py --name tea2o_yolov5s  --data data/apple/c2d_tea2o.yaml --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;

# python train.py --name tea2o_best  --data data/apple/c2d_tea2o.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;


# python train.py --name atea2o_yolov5s  --data data/apple/c2d_ir_depth_tea2o.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;

# python train.py --name atea2o_best  --data data/apple/c2d_ir_depth_tea2o.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;



# python train.py --name 3_best_tea2p_pre  --weights  /home/ps/rgbd/result/yolov5_best_27/tea2p_best/weights/best.pt  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_best_27/3_best_tea2p_pre/weights/best.pt --device 1;

# python train.py --name 3_yolov5s_tea2p_pre --weights  /home/ps/rgbd/result/yolov5_best_27/tea2p_yolov5s/weights/best.pt --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_best_27/3_yolov5s_tea2p_pre/weights/best.pt --device 1;

# python train.py --name 3_best_tea2o_pre  --weights  /home/ps/rgbd/result/yolov5_best_27/tea2o_best/weights/best.pt  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_best_27/3_best_tea2o_pre/weights/best.pt --device 1;

# python train.py --name 3_yolov5s_tea2o_pre --weights  /home/ps/rgbd/result/yolov5_best_27/tea2o_yolov5s/weights/best.pt --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_best_27/3_yolov5s_tea2o_pre/weights/best.pt --device 1;


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#