import pyautogui as pg
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.delay(30)
for i in range(10):
	pg.press("d")
	pg.press("enter")
