import os
import time
import datetime as dt


def turn_down():
    print("Доброй ночи!")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


def sleep_time(minutes):
    time_now = dt.datetime.now()
    time_delta = dt.timedelta(minutes=minutes)
    time_for_sleep = time_now + time_delta

    print(f"Обратный отсчет начат в {time_now.hour}:{time_now.minute}. "
          f"В спящий режим компьютер уйдет в "
          f"{time_for_sleep.hour}:{time_for_sleep.minute}.")

    time.sleep(minutes * 60)

    turn_down()


if __name__ == '__main__':
    print("Через сколько минут вы хотите выключить свой пк?")
    input_minutes = input()

    sleep_time(int(input_minutes))
