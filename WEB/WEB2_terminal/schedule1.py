# import datetime
# import schedule
#
# i = 1
#
#
# def job():
#     global i
#     print(f"Функция запустилась {i} раз")
#     i += 1
#     print(datetime.datetime.now())
#     if i > 3:
#         return schedule.CancelJob
#
#
# schedule.every(5).seconds.do(job)
# while schedule.get_jobs():
#     schedule.run_pending()

import datetime
import schedule


def job():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    if minute == 0 and second < 1:
        if hour > 12:
            print(*["Ky"] * (hour - 12))
        else:
            print(*["Ky"] * hour)


schedule.every(1).second.do(job)
while schedule.get_jobs():
    schedule.run_pending()
