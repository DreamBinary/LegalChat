# -*- coding:utf-8 -*-
# @FileName : download.py
# @Time : 2024/1/11 0:01
# @Author :fiv

import os

import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer


def download():
    model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm-chat-7b', cache_dir='/root/data/model',
                                  revision='v1.0.3')
    # 设置环境变量
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

    # 下载模型
    os.system(
        'huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir /root/data/model/sentence-transformer')
