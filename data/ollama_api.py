from util import json_read
from ollama import Client

client = Client(host='http://localhost:11434')


def ollama_list():
    # 列表
    data = client.list()
    return json_read.json_format(data)


def ollama_show(model_name):
    # 显示
    data = client.show(model_name)
    return json_read.json_format(data)


def ollama_create():
    # 创造
    modelfile = '''
  FROM llama3.1
  SYSTEM You are mario from super mario bros.
  '''
    data = client.create(model='example', modelfile=modelfile)
    return json_read.json_format(data)


def ollama_copy():
    # 复制
    data = client.copy('llama3.1', 'user/llama3.1')
    return json_read.json_format(data)


def ollama_delete(model_name):
    # 删除
    data = client.delete(model_name)
    return json_read.json_format(data)


def ollama_pull(model_name):
    # 拉取
    data = client.pull(model_name)
    return json_read.json_format(data)


def ollama_push():
    # 推送
    data = client.push('user/llama3.1')
    return json_read.json_format(data)


def ollama_embeddings():
    # 嵌入
    data = client.embeddings(model='llama3.1', prompt='The sky is blue because of rayleigh scattering')
    return json_read.json_format(data)


def ollama_ps():
    # 列出
    data = client.ps()
    return json_read.json_format(data)


def ollama_chat(model_name, content):
    # 生成
    response = client.chat(model=model_name, messages=[
        {
            'role': 'user',
            'content': content,
        },
    ])
    print(json_read.json_format(response))
    return response['message']['content']


if __name__ == '__main__':
    model_name = 'llama3.1'
    ollama_txt = ollama_chat(model_name, '天空是什么颜色')
    # ollama_txt = ollama_list()
    # ollama_txt = ollama_show(model_name)
    # ollama_txt = ollama_delete("llama3:latest")
    print(ollama_txt)
