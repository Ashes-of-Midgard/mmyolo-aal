# Overview

这是一个整合了联想对抗学习（Associative Adversarial Learning, AAL）训练方法的YOLOv5网络项目. AAL方法能够提升网络对抗干扰的鲁棒性.

# Install

```
conda create -n aal python=3.10
conda activate aal
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
pip install "numpy<2.0"
pip install -U openmim
mim install "mmengine>=0.6.0"
mim install "mmcv>=2.0.0rc4,<2.1.0"
mim install "mmdet>=3.0.0rc5,<3.1.0"
cd mmyolo-aal
pip install -r requirements.txt
pip install "albumentations<1.4"
pip install -e . -v
```
！使用mim安装mmcv时，需要手动指定版本，否则会默认安装最新版本。目前最新版本的mmcv无法支持mmdet，需要手动降低版本。另外还需要注意mmcv版本与pytorch, cuda版本的匹配关系。尝试安装不匹配的版本会出现编译错误。

！建议在安装前先确定所需的mmcv版本。经过测试，"mmcv>=2.0.0rc4,<2.1.0"能够支持最新版本的mmdet和mmyolo，随后再前往[https://mmcv.readthedocs.io/zh-cn/latest/get_started/installation.html#pip]确认和所需的mmcv版本匹配的pytorch，再配置环境。

# Train

训练采用了AAL方法的YOLOv5
```shell
python tools/train.py configs/yolov5/yolov5aal_x-v61_syncbn_fast_8xb16-300e_coco.py
```

训练原版YOLOv5
```shell
python tools/train.py configs/yolov5/yolov5_x-v61_syncbn_fast_8xb16-300e_coco.py
```