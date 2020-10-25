import threading,requests#,ks
from cs import *
# 监听消息实例 通过消息来判断
def msgdata():
    msger = jtxx()
    for data in msger:
        print(data)
        if data[0]=="msgdp": #消息内容
            
            if data[5]=="0": # 1代表发送消息 0代表收到消息
                if data[2].find("@chatroom") != -1:  # 群里发的消息
                    print("群里发的消息")
                if data[2][0:3].find("gh_") != -1:   #公众号收到的消息
                    print("公众号消息")
                if data[2].find("@chatroom") == -1 and data[2][0:3].find("gh_") == -1: #排除 群里发的消息 公众号收到的消息
                    print("私人消息")
                    #下面是AI调用实例
                    a=requests.get("http://ai.wfzc.vip/"+str(data[6])+"/")
                    text = a.text
                    if text=='<meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport">欢迎来到挽风智障AI <br/>请在连接携带要问<br>如 http://ai.wfzc.vip/你在干嘛啊/ 访问接口':
                        text="不知道你在说什么"
                    fxx(data[2], text[0:100])#发送消息 data[2]=微信id  text[0:100]=请求后的消息 
threading.Thread(target=msgdata).start()#多线程收消息 处理
input("启动微信")
while True:
    ID=input("id")
    msg=input("内容")
    fxx(id=ID, msg=msg)
