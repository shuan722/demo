import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

"""
# APScheduler提供了七种调度器：
BlockingScheduler：适合于只在进程中运行单个任务的情况，通常在调度器是你唯一要运行的东西时使用。
BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用。

# APScheduler提供了三种任务触发器

data：固定日期触发器：任务只运行一次，运行完毕自动清除；若错过指定运行时间，任务不会被创建
interval：时间间隔触发器
cron：cron风格的任务触发
"""


def job(text=""):
    print(text, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def run_date():
    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用阻塞的方式
    # 采用date的方式，在特定时间只执行一次
    scheduler.add_job(job, 'date', run_date='2018-09-21 15:30:00')
    scheduler.start()


def run_back_ground_scheduler():
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用。
    scheduler = BackgroundScheduler()
    # 采用非阻塞的方式

    # 采用固定时间间隔（interval）的方式，每隔3秒钟执行一次
    scheduler.add_job(job, 'interval', seconds=3)
    # 这是一个独立的线程
    scheduler.start()

    # 其他任务是独立的线程
    while True:
        print('main-start:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(2)
        print('main-end:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def run_5():
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用
    scheduler = BackgroundScheduler()
    # 采用非阻塞的方式

    # 采用corn的方式
    scheduler.add_job(job, 'cron', day_of_week=5, second='*/5')
    '''
    year (int|str) – 4-digit year
    month (int|str) – month (1-12)
    day (int|str) – day of the (1-31)
    week (int|str) – ISO week (1-53)
    day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
    hour (int|str) – hour (0-23)
    minute (int|str) – minute (0-59)
    econd (int|str) – second (0-59)

    start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
    end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

    *    any    Fire on every value
    */a    any    Fire every a values, starting from the minimum
    a-b    any    Fire on any value within the a-b range (a must be smaller than b)
    a-b/c    any    Fire every c values within the a-b range
    xth y    day    Fire on the x -th occurrence of weekday y within the month
    last x    day    Fire on the last occurrence of weekday x within the month
    last    day    Fire on the last day within the month
    x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
    '''
    scheduler.start()

    # 其他任务是独立的线程
    while True:
        print('main-start:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(2)
        print('main-end:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def run_task():
    scheduler = BlockingScheduler()
    # 5秒执行一次
    scheduler.add_job(job, 'interval', seconds=5, args=['5秒执行一次'])
    # 每天6点5分执行一次
    scheduler.add_job(job, 'cron', hour=1, minute=5, args=['每天6点5分执行一次'])
    # 每天6点执行智慧引导服务
    scheduler.add_job(job, 'cron', hour=18, args=['每天执行一次'])
    scheduler.start()


def other_task():
    scheduler = BlockingScheduler()
    # 每隔5s执行一次my_job函数，输出当前时间信息
    scheduler.add_job(job, 'interval', seconds=5)
    # 时间： 周一到周五每天早上6点半, 执行my_job
    scheduler.add_job(job, 'cron', day_of_week='1-5', hour=6, minute=30)
    # 在每天22点，每隔 1分钟 运行一次 job 方法
    scheduler.add_job(job, 'cron', hour=22, minute='*/1', args=['job1'])
    # 在每天22和23点的25分，运行一次 job 方法
    scheduler.add_job(job, 'cron', hour='22-23', minute='25', args=['job2'])
    # 在每天 8 点，运行一次 job 方法
    scheduler.add_job(job, 'cron', hour='8', args=['job2'])
    # 在每天 8 点 20点，各运行一次 job 方法    设置最大运行实例数
    scheduler.add_job(job, 'cron', hour='1, 20', minute="26", max_instances=4)
    scheduler.start()


if __name__ == '__main__':
    # run_task()
    other_task()
