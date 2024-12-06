_base_ = './yolov5_m-v61_syncbn_fast_8xb16-300e_coco.py'
deepen_factor = 1.33
widen_factor = 1.25

model = dict(
    init_cfg=dict(
        type='Pretrained', checkpoint='https://download.openmmlab.com/mmyolo/v0/yolov5/mask_refine/yolov5_x_mask-refine-v61_syncbn_fast_8xb16-300e_coco/yolov5_x_mask-refine-v61_syncbn_fast_8xb16-300e_coco_20230305_154321-07edeb62.pth'),
    backbone=dict(
        deepen_factor=deepen_factor,
        widen_factor=widen_factor,
    ),
    neck=dict(
        deepen_factor=deepen_factor,
        widen_factor=widen_factor,
    ),
    bbox_head=dict(head_module=dict(widen_factor=widen_factor)))

default_hooks = dict(checkpoint=dict(interval=1))

train_cfg=dict(max_epochs = 12, # Maximum training epochs
               val_interval=1)