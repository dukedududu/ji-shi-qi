import time#time  模块
print("回车开始计时  ctrl+c停止计时")
while True: 
    try:
        input() 
        starttime = time.time()#函数time.time()用于获取当前时间戳
        print('开始')
        while True:
            print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
            time.sleep(1)#time.sleep(secs)   推迟调用线程的运行，secs指秒数。
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - starttime, 2),'secs')
        break

