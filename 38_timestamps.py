import time

print(time.time())
print(time.ctime())

def sendEmails():
    for i in range(100000):
        pass

startTime = time.time()
sendEmails()
endTime = time.time()
print(endTime - startTime)
