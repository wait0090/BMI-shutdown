import time
import os
import pyttsx3

#朗读文本
def speak(text):
    # 初始化语音引擎
    engine = pyttsx3.init()
    
    # 设置语速（默认 200，范围 50-500）
    engine.setProperty('rate', 200)  
    
    # 设置音量（0.0-1.0）
    engine.setProperty('volume', 0.9)  
    
    # 朗读文本
    engine.say(text)
    
    # 等待语音播放完成
    engine.runAndWait() 

#强制关机
def warning (*i):
    text = "系统检测到您的BMI"+str(i)+"⚠️⚠️⚠️"+"\n"+"您的健康风险系数高\n请立即停止使用您的电脑"+"为了您的身体健康\n系统将在60秒后关闭您的电脑"
    print(text)
    speak(text)
    os.system("shutdown /s /t 60")

#系统建议
def advice() :
    text = "系统检测到您的BMI正常\n但检测到您长时间使用电脑\n建议您执行15分钟身体活动"
    print(text)
    speak(text)
    time.sleep(1)
    text = "您是否接受建议（Y/N）："
    print(text)
    speak(text)
    option = str(input())
    if 'Y'== option :
        text = "系统将在60秒内关机"
        print(text)
        speak(text)
        os.system("shutdown /s /t 60")
    else :
        text = "您可以继续使用您的电脑了😊\n注意适当休息"
        print(text)
        speak(text)

#用户输入
text = "请输入您的体重"
speak(text)
user_weight = float(input(text+"(KG)："))
text = "请输入您的身高"
speak(text)
user_heigh = float(input(text+"(M)："))
user_BMI = user_weight / (user_heigh)**2

#输出BMI
text = "您的BMI为："+str(user_BMI)
print(text)
speak(text)

#判断BMI
if user_BMI <= 18.5 :
    print("偏瘦")
    time.sleep(1)
    warning("过低")
elif 18.5 < user_BMI <= 25 :
    print("正常")
    time.sleep(1)
    advice()
elif 25 < user_BMI <= 30 :
    print("偏胖")
    time.sleep(1)
    warning("过高")
else :
    print("肥胖")
    time.sleep(1)
    warning("严重偏高")

#延迟终端关闭
os.system("pause")