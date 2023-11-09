
#####################################################################################################################################################
# sn.set_theme(font='Times New Roman')
# python train.py --name 111  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python train.py --name 1111  --data data/tea/c2d_tea2.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python train.py --name 11111  --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;

# python train.py --name 1up_v5  --data data/tea/c2d_tea1up.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1up.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1up_v52/weights/best.pt --device 1;

# python train.py --name 1up_best  --data data/tea/c2d_tea1up.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea/c2d_tea1up.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1up_best2/weights/best.pt --device 1;

# python train.py --name 2_v5_preup  --weights /home/ps/rgbd/result/yolov5_05_06/1up_v52/weights/best.pt  --data data/tea/c2d_tea2.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea/c2d_tea2.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_v5_preup/weights/best.pt --device 1;

# python train.py --name 2_best_preup  --weights /home/ps/rgbd/result/yolov5_05_06/1up_best2/weights/best.pt  --data data/tea/c2d_tea2.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea2.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_best_preup/weights/best.pt --device 1;




# python train.py --name 1_v5  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1_v5/weights/best.pt --device 1;

# python train.py --name 1_best  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1_best/weights/best.pt --device 1;


# python train.py --name 2_v5  --data data/tea/c2d_tea2.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea2.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_v5/weights/best.pt --device 1;

# python train.py --name 2_best  --data data/tea/c2d_tea2.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea2.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_best/weights/best.pt --device 1;


# python train.py --name 2_v5_p  --data data/apple/c2d_tea2p.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/apple/c2d_tea2p.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_v5_p/weights/best.pt --device 1;

# python train.py --name 2_best_p  --data data/apple/c2d_tea2p.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/apple/c2d_tea2p.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_best_p/weights/best.pt --device 1;


# python train.py --name 2_v5_o  --data data/apple/c2d_tea2o.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/apple/c2d_tea2o.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_v5_o/weights/best.pt --device 1;

# python train.py --name 2_best_o  --data data/apple/c2d_tea2o.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/apple/c2d_tea2o.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_best_o/weights/best.pt --device 1;

# _____
# python train.py --name 1_v5_pre  --weights /home/ps/rgbd/result/yolov5_05_06/2_v5/weights/best.pt  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1_v5_pre/weights/best.pt --device 1;

# python train.py --name 1_best_pre  --weights /home/ps/rgbd/result/yolov5_05_06/2_best/weights/best.pt   --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1_best_pre/weights/best.pt --device 1;
# _____
# _____
# python train.py --name 2_v5_pre  --weights /home/ps/rgbd/result/yolov5_05_06/1_v5/weights/best.pt  --data data/tea/c2d_tea2.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea/c2d_tea2.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_v5_pre/weights/best.pt --device 1;

# python train.py --name 2_best_pre  --weights /home/ps/rgbd/result/yolov5_05_06/1_best/weights/best.pt   --data data/tea/c2d_tea2.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea/c2d_tea2.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2_best_pre/weights/best.pt --device 1;

# _____



# python train.py --name 1_v5_pre_p  --weights /home/ps/rgbd/result/yolov5_05_06/2_v5_p/weights/best.pt  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1_v5_pre_p/weights/best.pt --device 1;

# python train.py --name 1_best_pre_p  --weights /home/ps/rgbd/result/yolov5_05_06/2_best_p/weights/best.pt   --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1_best_pre_p/weights/best.pt --device 1;

# python train.py --name 1_v5_pre_o  --weights /home/ps/rgbd/result/yolov5_05_06/2_v5_o/weights/best.pt  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1_v5_pre_o/weights/best.pt --device 1;

# python train.py --name 1_best_pre_o  --weights /home/ps/rgbd/result/yolov5_05_06/2_best_o/weights/best.pt   --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1_best_pre_o/weights/best.pt --device 1;

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# python train.py --name 1a_v5  --data data/tea/a_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/a_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1a_v5/weights/best.pt --device 1;

# python train.py --name 1a_best  --data data/tea/a_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/a_tea1.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/1a_best/weights/best.pt --device 1;

# python train.py --name 2a_v5  --data data/tea/a_tea2.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/a_tea2.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2a_v5/weights/best.pt --device 1;

# python train.py --name 2a_best  --data data/tea/a_tea2.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/a_tea2.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2a_best/weights/best.pt --device 1;



# python train.py --name 2a_v5_o  --data data/apple/c2d_ir_depth_tea2o.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/apple/c2d_ir_depth_tea2o.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2a_v5_o/weights/best.pt --device 1;

# python train.py --name 2a_best_o  --data data/apple/c2d_ir_depth_tea2o.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/apple/c2d_ir_depth_tea2o.yaml    --weights /home/ps/rgbd/result/yolov5_05_06/2a_best_o/weights/best.pt --device 1;



# python train.py --name 1a_v5_pre_o  --weights /home/ps/rgbd/result/yolov5_05_06/2a_v5_o/weights/best.pt  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/1a_v5_pre_o/weights/best.pt --device 1;

# python train.py --name 1a_best_pre_o  --weights /home/ps/rgbd/result/yolov5_05_06/2a_best_o/weights/best.pt   --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea/c2d_tea1.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/1a_best_pre_o/weights/best.pt --device 1;

#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# python train.py --name 1_v5  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 1_best  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 2_v5  --data data/tea/c2d_tea2.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 2_best  --data data/tea/c2d_tea2.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 2_v5_p  --data data/apple/c2d_tea2p.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 2_best_p  --data data/apple/c2d_tea2p.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 2_v5_o  --data data/apple/c2d_tea2o.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 2_best_o  --data data/apple/c2d_tea2o.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 1_v5_pre_p  --weights /home/ps/rgbd/result/yolov5_05_06/2_v5_p/weights/best.pt  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 1_best_pre_p  --weights /home/ps/rgbd/result/yolov5_05_06/2_best_p/weights/best.pt   --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 1_v5_pre_o  --weights /home/ps/rgbd/result/yolov5_05_06/2_v5_o/weights/best.pt  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name 1_best_pre_o  --weights /home/ps/rgbd/result/yolov5_05_06/2_best_o/weights/best.pt   --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 1;


# python train.py --name 1a_v5  --data data/tea/a_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name 1a_best  --data data/tea/a_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name 2a_v5  --data data/tea/a_tea2.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name 2a_best  --data data/tea/a_tea2.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name 2a_v5_o  --data data/apple/c2d_ir_depth_tea2o.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name 2a_best_o  --data data/apple/c2d_ir_depth_tea2o.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name 1a_v5_pre_o  --weights /home/ps/rgbd/result/yolov5_05_06/2a_v5_o/weights/best.pt  --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/yolov5s.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name 1a_best_pre_o  --weights /home/ps/rgbd/result/yolov5_05_06/2a_best_o/weights/best.pt   --data data/tea/c2d_tea1.yaml  --cfg models/axiaorong/best_all.yaml   --epochs 2000  --batch-size 4   --device 0;


# python train.py --name bh  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh/weights/best.pt --device 1;

# python train.py --name bh1  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh1.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh1/weights/best.pt --device 1;

# python train.py --name bh2  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh2.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh2/weights/best.pt --device 0;

# python train.py --name bh3  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh3.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh3/weights/best.pt --device 1;

# python train.py --name bh4  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh4.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh4/weights/best.pt --device 0;

# python train.py --name bh5  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh5.yaml   --epochs 2000  --batch-size 4   --device 0;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh5/weights/best.pt --device 0;

# python train.py --name bh6  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh6.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh6/weights/best.pt --device 0;

# python train.py --name bh7  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh7.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh7/weights/best.pt --device 0;

# python train.py --name bh8  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh8.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh8/weights/best.pt --device 0;

# python train.py --name bh9  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh9.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh9/weights/best.pt --device 0;

# python train.py --name bh10 --data data/tea3_single/c2d.yaml  --cfg models/bh/bh10.yaml   --epochs 2000  --batch-size 4   --device 1;
# python val.py --data data/tea3_single/c2d.yaml   --weights /home/ps/rgbd/result/yolov5_05_06/bh10/weights/best.pt --device 0;



# python train.py --name bh  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name bh1  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh1.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name bh2  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh2.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name bh3  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh3.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name bh4  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh4.yaml   --epochs 2000  --batch-size 4   --device 0; python train.py --name bh5  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh5.yaml   --epochs 2000  --batch-size 4   --device 0;

# python train.py --name bh6  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh6.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name bh7  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh7.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name bh8  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh8.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name bh9  --data data/tea3_single/c2d.yaml  --cfg models/bh/bh9.yaml   --epochs 2000  --batch-size 4   --device 1; python train.py --name bh10 --data data/tea3_single/c2d.yaml  --cfg models/bh/bh10.yaml   --epochs 2000  --batch-size 4   --device 1;





# python train.py --name 1 --data data/tea3_single/c2d.yaml  --cfg models/axiaorong/yolov5s.yaml  --epochs 10  --batch-size 4   --device 1;

# +++++++++++++++++++++++++++++++++++++++++++++++++