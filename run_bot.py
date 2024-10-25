import gradio as gr
from gr_module.setting import setting
from gr_module.dialog import dialog
from gr_module.chat import chat

# orange    green emerald     teal  cyan
dark_theme = gr.themes.Base(
    # primary_hue=gr.themes.colors.orange,
    # secondary_hue=gr.themes.colors.orange,
    neutral_hue=gr.themes.colors.teal,
)
css = """
    .wide-first-column td:nth-child(1) {
        width: 95%;
    }
    .wide-first-column td:nth-child(2) {
        width: 5%;
    }
"""

with gr.Blocks(title="carla", theme=dark_theme, css=css) as bot_webui:
    markdown = gr.Markdown(
        """
        ## carla-V1.0
        即将开发：
        - 流式返回信息
        - 图片发送与识别
        - 图片生成
        - 模型工具调用
        - 创建自定义模型
        """,
        label="自定义大模型webui"
    )
    with gr.Tab("聊天模式"):
        chat()

    with gr.Tab("语音对话模式"):
        dialog()

    with gr.Tab("设置"):
        setting()

if __name__ == '__main__':
    # 启用队列功能
    # bot_webui.queue()
    bot_webui.launch(
        share=False,
        server_port=9536,
        inbrowser=True,
        favicon_path="./static/icon.ico"
    )
