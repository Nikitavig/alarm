from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time
import datetime

from multiprocessing import Process

TIME_START = '20:51'

def start_alarm():
	while True:
		# try:
		options = Options()
		options.add_argument('--user-data-dir=alarm')
		options.add_argument('--profile-directory=my_profil')
		options.add_argument('--start-maximized')

		browser = webdriver.Chrome(chrome_options=options)
		browser.implicitly_wait(10)


		browser.get('https://music.youtube.com/')
		# browser.get('https://music.youtube.com/watch?v=anGVuSFJ2w8&list=RDEMzT1XwmFnIup_KYXuc2rUZA')
		browser.find_element_by_xpath("//a[@title='Мой джем']").click()
		browser.find_element_by_xpath("//div[@class='circle style-scope paper-spinner-lite']").click()
		time.sleep(99999)
		# except Exception as e:
		# 	print(e)
		# finally:
		# 	browser.close()



def main():
	"""
	
	Основноая main функция
	"""

	# Разбираем первоначальную строку на чалсы и минуты
	hour = int(TIME_START.split(':')[0])
	minute = int(TIME_START.split(':')[1])

	# Сохраняем текущую дату
	time_now = datetime.datetime.today()

	# Устанавливаем дату будильника

	# Временноая переменная под дату и вермя будильника
	# Забираем год, месяц, день из текущей даты
	# Часы и минуты устанавливаем из выпаршеных значений
	temp_time = datetime.datetime(time_now.year, time_now.month, time_now.day, hour, minute)

	# Проверяем, если текущее время больше, чем временное временая переменная
	# то нужно добавить к дате один день 
	if time_now > temp_time:
		# Добавляем один день
		time_alarm = datetime.datetime(time_now.year, time_now.month, time_now.day + 1, hour, minute)
	# Если нет, то время будильника =  временной переменной 
	else:
		time_alarm = temp_time

	print(f"Будильник установлене на: {time_alarm}")

	# Ждем времени наступления будильника наступления 
	while time_alarm > datetime.datetime.today():
		
		# print(f"Будильник установлене на: {time_alarm}")
		print(f"******    ОСТАЛОСЬ    >>> {time_alarm - datetime.datetime.today()}", end='')
		print('\r', end='')

		time.sleep(1)

	start_alarm()


if __name__ == '__main__':
	main()