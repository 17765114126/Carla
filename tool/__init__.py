import gradio as gr


def start_recording():
    # 开始录音的逻辑
    print("开始录音")
    return gr.update(visible=True), gr.update(visible=False)


def stop_recording_and_process():
    # 停止录音并处理的逻辑
    print("停止录音并处理")
    return gr.update(visible=False), gr.update(visible=True)


with gr.Blocks() as demo:
    start_button = gr.Button("开始", variant="primary")
    stop_button = gr.Button("停止", variant="primary", visible=False)

    # 绑定按钮事件
    start_button.click(fn=start_recording, outputs=[stop_button, start_button])
    stop_button.click(fn=stop_recording_and_process, outputs=[start_button, stop_button])

demo.launch()