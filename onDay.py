import schedule
import time


def job():
    print(time.time())
    print('In onDay')

def onDay():
    schedule.every(10).seconds.do(job)
    i = 0
    while True:
        schedule.run_pending()
        print(i)
        i += 1
        time.sleep(10)
