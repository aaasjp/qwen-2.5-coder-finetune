使用 NVIDIA CUDA 基础镜像
FROM nvidia/cuda:12.1.0-cudnn8-devel-ubuntu22.04

# 设置工作目录
WORKDIR /app

# 避免交互式前端
ENV DEBIAN_FRONTEND=noninteractive

# 安装基本依赖
RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    python3 \
    python3-dev \
    python3-pip \
    build-essential \
    vim \
    nano \
    htop \
    tmux \
    less \
    tree \
    net-tools \
    iputils-ping \
    zip \
    unzip \
    tar \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 创建软链接使 python 指向 python3
RUN ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# 升级 pip
RUN pip install --upgrade pip

# 配置pip国内源加速
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip config set global.trusted-host pypi.tuna.tsinghua.edu.cn

# 从GitHub克隆项目
RUN git clone https://github.com/QwenLM/Qwen2.5-Coder.git /app

# 安装项目依赖
RUN cd /app/finetuning/sft && pip install -r requirements.txt

# 安装微调相关的额外依赖
RUN pip install \
    datasets \
    deepspeed \
    accelerate \
    sentencepiece \
    peft \
    bitsandbytes \
    transformers>=4.37.0

# 设置环境变量
ENV PYTHONPATH=/app
ENV CUDA_VISIBLE_DEVICES=0

# 创建数据和模型目录
RUN mkdir -p /app/data /app/models /app/output

# 设置工作目录为微调脚本目录
WORKDIR /app/finetuning/sft

# 添加执行权限给微调脚本
RUN chmod +x ./scripts/*.sh

# 容器启动命令（默认为Bash）
CMD ["/bin/bash"]