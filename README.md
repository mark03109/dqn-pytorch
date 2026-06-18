# DQN play pong

![alt text](assets/pong.gif)

## PC环境

windows 11
Geforce RTX 5060

## 依赖

建议先单独安装torch，安装命令如下：

```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu132
```

安装完毕后可以先运行`gpu_config.py`查看是否正确安装了torch和cuda

```bash
python gpu_config.py
```

然后安装其他依赖：

```bash
pip install -r requirements.txt
```

## 训练

```bash
python train.py
```

训练时长可能较长，无法中途退出中断
最终训练过程视频将被保存在`./videos`目录下

## 参考文献

Playing Atari with Deep Reinforcement Learning，https://arxiv.org/abs/1312.5602
github.com/floringogianu/atari-agents

