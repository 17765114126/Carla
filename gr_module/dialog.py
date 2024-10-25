import gradio as gr
from data import real_say


def start_recording():
    # 开始录音的逻辑
    real_say.start_recording()
    # 返回更新后的按钮状态：显示停止按钮，隐藏开始按钮
    return gr.update(visible=True), gr.update(visible=False)


def stop_recording_and_process():
    # 停止录音并处理的逻辑
    result = real_say.stop_recording_and_process()
    # 返回更新后的按钮状态：隐藏停止按钮，显示开始按钮
    return gr.update(visible=True), gr.update(visible=False), result  # 注意这里返回了result

# with gr.Tab("实时转录"):
#     with gr.Row():
#         recording_button = gr.Button("开始/停止录音", variant="primary")
#         state_label = gr.Label("等待开始...")
#
#         recording_button.click(
#             recording.listen_for_audio,
#             inputs=[recording_button],
#             outputs=[state_label]
#         )


def dialog():
    output = gr.Textbox()
    start_button = gr.Button("开始", variant="primary")
    stop_button = gr.Button("停止", variant="primary", visible=False)  # 初始状态不显示停止按钮

    # 绑定按钮事件
    start_button.click(fn=start_recording, outputs=[stop_button, start_button])
    stop_button.click(fn=stop_recording_and_process, outputs=[start_button, stop_button, output])
