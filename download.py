# -*- coding:utf-8 -*-
# @FileName : download.py
# @Time : 2024/1/11 0:01
# @Author :fiv

import os

from modelscope import snapshot_download


def download():
    # create dir
    os.makedirs('data/model', exist_ok=True)
    snapshot_download('Shanghai_AI_Laboratory/internlm-chat-7b', cache_dir='data/model', revision='v1.0.3')
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
    os.system(
        'huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir data/model/sentence-transformer')

    os.system("git clone https://gitee.com/yzy0612/nltk_data.git  --branch gh-pages")
    os.system("cd nltk_data")
    os.system("mv packages/* ./")
    os.system("cd tokenizers")
    os.system("unzip punkt.zip")
    os.system("cd ../taggers")
    os.system("unzip averaged_perceptron_tagger.zip")
