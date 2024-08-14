from util import json_read
import requests
import json
host = "http://localhost:11434"


def ollama_list():
    # 列表 列出本地可用的模型。
    data = requests.get(host + "/api/tags")
    # data = client.list()
    print(data.status_code)
    # 假设 data.content 包含上述字节串
    decoded_content = data.content.decode('utf-8')

    # 将字符串解析为 JSON 对象
    json_data = json.loads(decoded_content)

    # 格式化输出 JSON
    formatted_json = json.dumps(json_data, indent=4)
    return formatted_json


def ollama_show(model_name):
    # 显示有关模型的信息，包括详细信息、模型文件、模板、参数、许可证、系统提示符。
    data = requests.post(host + "/api/show", params={"name": model_name})
    return json_read.json_format(data)


def ollama_create(name):
    # 创建模型

    # 参数
    # name：要创建的模型的名称
    # modelfile（可选）：模型文件的内容
    # stream：（可选）如果响应将作为单个响应对象返回，而不是作为对象流返回false
    # path（可选）：模型文件的路径
    #   modelfile = '''
    # FROM llama3.1
    # SYSTEM You are mario from super mario bros.
    # '''
    data = requests.post(host + "/api/create", params={"name": name, "modelfile": ""})
    return json_read.json_format(data)


def ollama_copy():
    # 复制模型。使用现有模型中的另一个名称创建模型。
    data = requests.post(host + "/api/copy", params={"source": model_name, "destination": "backup"})
    return json_read.json_format(data)


def ollama_delete(model_name):
    # 删除模型及其数据。
    data = requests.delete(host + "/api/delete", params={"name": model_name})
    return json_read.json_format(data)


def ollama_pull(model_name):
    # 拉取模型 从 ollama 库下载模型。已取消的拉取将从中断的位置恢复，多个调用将共享相同的下载进度。

    # 参数
    # name：要拉取的模型的名称
    # insecure：（可选）允许与库建立不安全的连接。仅在开发过程中从自己的库中提取时才使用此方法。
    # stream：（可选）如果响应将作为单个响应对象返回，而不是作为对象流返回false
    data = requests.post(host + "/api/pull", params={"name": model_name})
    return json_read.json_format(data)


def ollama_push():
    # 推送 将模型上传到模型库。需要先注册 ollama.ai 并添加公钥。
    # 参数
    # name：以 的形式推送的模型名称<namespace>/<model>:<tag>
    # insecure：（可选）允许与库建立不安全的连接。仅在开发期间推送到库时才使用此方法。
    # stream：（可选）如果响应将作为单个响应对象返回，而不是作为对象流返回false
    data = requests.post(host + "/api/push", params={"name": model_name})
    return json_read.json_format(data)


def ollama_embed():
    # 嵌入 从模型生成嵌入
    data = requests.post(host + "/api/embed", params={"model": model_name, "input": "Why is the sky blue?"})
    return json_read.json_format(data)


def ollama_ps():
    # 列出正在运行的模型
    data = requests.get(host + "/api/ps")
    return json_read.json_format(data)


def ollama_chat(model_name, messages, stream, tools):
    # stream = True 为流式输出
    if stream is None:
        stream = False
    # 生成

    # 参数
    # model：（必填）模型名称
    # messages：聊天的消息，这可以用来保持聊天记忆
    # tools：模型要使用的工具（如果支持）。需要设置为streamfalse
    # 该对象包含以下字段：message
    #
    # role：消息的角色，可以是 、 、 或systemuserassistanttool
    # content：消息的内容
    # images（可选）：要包含在消息中的图像列表（对于多模态模型，例如llava)
    # tool_calls（可选）：模型要使用的工具列表
    # 高级参数（可选）：
    #
    # format：返回响应的格式。目前唯一接受的值是json
    # options：模型文件文档中列出的其他模型参数，例如temperature
    # stream：如果响应将作为单个响应对象返回，而不是作为对象流返回false
    # keep_alive：控制模型在请求后将保持加载到内存中的时间（默认值：5m)
    # 单次聊天请求
    # [
    #     {
    #         "role": "user",
    #         "content": "content"
    #     }
    # ]
    # 带历史记录聊天请求
    # [
    #     {
    #       "role": "user",
    #       "content": "why is the sky blue?"
    #     },
    #     {
    #       "role": "assistant",
    #       "content": "due to rayleigh scattering."
    #     },
    #     {
    #       "role": "user",
    #       "content": "how is that different than mie scattering?"
    #     }
    #   ]
    # 聊天请求（带图片）:图像应以数组形式提供，单个图像以 Base64 编码。
    # [
    #     {
    #       "role": "user",
    #       "content": "what is in this image?",
    #       "images": []
    #     }
    #   ]
    # 聊天请求（使用工具）
    # [
    #     {
    #       "type": "function",
    #       "function": {
    #         "name": "get_current_weather",
    #         "description": "Get the current weather for a location",
    #         "parameters": {
    #           "type": "object",
    #           "properties": {
    #             "location": {
    #               "type": "string",
    #               "description": "The location to get the weather for, e.g. San Francisco, CA"
    #             },
    #             "format": {
    #               "type": "string",
    #               "description": "The format to return the weather in, e.g. 'celsius' or 'fahrenheit'",
    #               "enum": ["celsius", "fahrenheit"]
    #             }
    #           },
    #           "required": ["location", "format"]
    #         }
    #       }
    #     }
    #   ]

    data = requests.post(host + "/api/chat ", params={
        "model": model_name,
        "messages": messages,
        "stream": stream
    })
    # response = client.chat(model=model_name, messages=[
    #     {
    #         'role': 'user',
    #         'content': content,
    #     },
    # ])
    # print(json_read.json_format(response))
    return data['message']['content']


def ollama_generate(model_name, prompt, stream):
    # stream = True 为流式输出
    if stream is None:
        stream = False
    # 参数
    # model：（必填）模型名称
    # prompt：生成响应的提示
    # suffix：模型响应后的文本
    # images：（可选）base64 编码图像的列表（对于多模态模型，例如llava)
    # 高级参数（可选）：
    #
    # format：返回响应的格式。目前唯一接受的值是json
    # options：模型文件文档中列出的其他模型参数，例如temperature
    # system：系统消息 to（覆盖Modelfile)
    # template：要使用的提示模板（覆盖Modelfile)
    # context：从上一个请求返回的上下文参数，可用于保持简短的对话记忆/generate
    # stream：如果响应将作为单个响应对象返回，而不是作为对象流返回false
    # raw：如果未对提示应用任何格式设置。如果您在对 API 的请求中指定了完整的模板化提示，则可以选择使用该参数trueraw
    # keep_alive：控制模型在请求后将保持加载到内存中的时间（默认值：5m)
    data = requests.post(host + "/api/generate ", params={
        "model": model_name,
        "prompt": prompt,
        "stream": stream
    })


if __name__ == '__main__':
    model_name = 'llama3.1'
    # ollama_txt = ollama_chat(model_name, '天空是什么颜色')
    ollama_txt = ollama_list()
    # ollama_txt = ollama_show(model_name)
    # ollama_txt = ollama_delete("llama3:latest")
    print(ollama_txt)
