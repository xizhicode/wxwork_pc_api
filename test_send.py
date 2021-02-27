import requests
# data = {'dialog_name': 'Python开发_通知专用', 'message': 'hello机器人'}
data = {'dialog_name': "秦曼", 'message': 'hello python'}
res = requests.post('http://192.168.8.140:77/send_message', data=data)
print(res.json())