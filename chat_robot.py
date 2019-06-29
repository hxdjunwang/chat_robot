#!/user/bin/env/ python3
import urllib.request #调用第三方接口库
import urllib.parse


def get_robot_reply(question):
    '''
    函数功能：对于特定问题进行特定的回复，对于非特定的问题进行智能回复

    参数描述：
    question：聊天内容或者问题

    返回值：str，回复内容
    '''
    if "你叫什么名字？" in question:
        answer = "我是jun哥"
    elif "你的生日是多少？" in question:
        answer = "10.22"
    elif "你几岁了？" in question:
        answer = "10"
    elif "你是男还是女？" in question:
        answer = "你说呢？"
    else:
        try:
            #调用NLP接口实现智能回复

            #将字符类型转换为字节类型
            params = urllib.parse.urlencode({'msg':question}).encode()
            #创建请求对象
            req = urllib.request.Request("http://api.itmojun.com/chat_robot",params,method = "POST")
            #调用接口（即向目标服务器发送HTTP请求，并获取服务器的响应数据）
            answer = urllib.request.urlopen(req).read().decode()
        except Exception as e:
            answer = "机器人出现故障（原因：%s）"% e
    return answer
if __name__ == '__main__':
    while True:
        question = input("请输入聊天内容：")
        if ("exit" == question):
            exit()
        answer =get_robot_reply(question) 
        print("小魔仙回答你：%s"%answer)
    