import RPi.GPIO as GPIO
import time
import system
'''
os.system("xset s 30") #设置屏幕保护时间为30S

#初始化
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.IN) #火焰传感器GPIO口
    GPIO.setup(12,GPIO.OUT) #蜂鸣器GPIO口
    GPIO.setup(13,GPIO.IN) #红外传感GPIO口
    pass
 
#蜂鸣器鸣叫函数
def beep()
    GPIO.output(12,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(12,GPIO.HIGH)
    time.sleep(0.5)
#感应器侦测函数
def detct():
    while True:
        if GPIO.input(13) == True:
            print "Someone isclosing!"
            os.system("xset dpms force on")
        if GPIO.input(11) == True:
            Print "On Fire!"
            for i in range(1,6):
                beep()
        time.sleep(30)
        pass

time.sleep(5)
init()
detct()

#脚本运行完毕执行清理工作
GPIO.cleanup()
'''

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.IN) #rad-scan
    GPIO.setup(12,GPIO.IN) #fire-scan
    GPIO.setup(13,GPIO.IN) #rain-scan
    GPIO.setup(14,GPIO,IN) #soil-humidity-scan
    GPIO.setup(15,GPIO.IN) #DTH11
    GPIO.setup(16,GPIO.IN)
    GPIO.setup(17,GPIO.OUT) #beep
    GPIO.setup(18,GPIO.OUT) #power%1
    GPIO.setup(19,GPIO.OUT) #power%2
    GPIO.setup(20,GPIO.OUT) #power%3
    GPIO.setup(21,GPIO.OUT) #power%4

def beep():
    GPIO(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO(17.GPIO.HIGH)
    time.sleep(0.5)

def red_scan()
    if GPIO.input==True:
        print "Scaned Someone!"
        os.system("xset dpms force on")

    else:
        print "Nobody here!"

def fire_scan()
    if GPIO.input==True:
        print "On Fire!"

    else:
        print "Not on fire!"

def rain_scan()
    if GPIO.input==True:
        print "Rainning!"

    else:
        print "Sun"

def soil_humidity_scan()
    if GPIO.input==True:
        print "Dry!"

    else:
        print "damp!"

def power_control()

time.sleep(5)
GPIO.cleanup()