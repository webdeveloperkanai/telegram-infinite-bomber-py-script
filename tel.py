import pyautogui as pg
from time import sleep

message = input("What is your Message ")

v = input("Enter Name/User Id ")
bar = int(input("How much do you want to send ? "))

sleep(2)
pg.hotkey('win')
sleep(2)
pg.write("Telegram")
sleep(3)
pg.press("enter")
sleep(5)
pg.moveTo(150, 55, 1)
pg.click()


def meessagePathao(message, v,vvv):
    # print("Tumi mot " + len(v) + " jon ke pthabe")
    pg.write(v)
    sleep(2)
    pg.press("enter")

    for cc in range(0, len(v)):
        pg.write(message)
        sleep(2)
        pg.press('enter')


for vvv in range(0,bar):
    meessagePathao(message, v,vvv)