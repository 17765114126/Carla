import json


# 读取配置文件配置
def read(one):
    f = open('data.json')
    data = json.load(f)
    f.close()
    return dict(data)['data'][one]
