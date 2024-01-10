# -*- coding:utf-8 -*-
# @FileName : app.py
# @Time : 2024/1/10 23:06
# @Author :fiv


import gradio as gr


def greet(name): return "Hello " + name + "!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
