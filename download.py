# -*- coding:utf-8 -*-
# @FileName : download.py
# @Time : 2024/1/11 0:01
# @Author :fiv

import os

from modelscope import snapshot_download


def download():
    # create dir
    os.makedirs('/root/data/model', exist_ok=True)
    snapshot_download('Shanghai_AI_Laboratory/internlm-chat-7b', cache_dir='/root/data/model', revision='v1.0.3')
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
    os.system(
        'huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir /root/data/model/sentence-transformer')
