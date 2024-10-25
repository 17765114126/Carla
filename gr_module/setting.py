import gradio as gr
from data import ollama_api


def setting():
    # with gr.Accordion("高级设置", open=False):
    # gr.Text(label="token")
    output_text = gr.Textbox(label="输出信息")
    with gr.Row():
        model_name = gr.Text(label="模型名称")
        pull_button = gr.Button(value="拉取模型")
    with gr.Row():
        del_model = gr.Dropdown(ollama_api.ollama_list(), value=ollama_api.ollama_list()[0], label="删除模型")
        del_button = gr.Button(value="删除模型")
    # 将按钮点击绑定到pull_model函数
    pull_button.click(fn=ollama_api.ollama_pull, inputs=model_name, outputs=output_text)
    # 将按钮点击绑定到del_model函数
    del_button.click(fn=ollama_api.ollama_delete, inputs=del_model, outputs=output_text)
