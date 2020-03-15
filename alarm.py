import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


TIME_START = '20:51'


def start_alarm():
	"""

	Функция для запуска случайного плейлиста предпочтений и youtube music
	"""

	while True:
		try:
			# Задаем параметры для драйвера
			options = Options()
			# Задаем директорию для сохранения профиля браузера
			options.add_argument('--user-data-dir=alarm')
			options.add_argument('--profile-directory=my_profil')
			# Открыть браузер в полном окное
			options.add_argument('--start-maximized')

			browser = webdriver.Chrome(chrome_options=options)
			# Ожидать появления того или иного объекта 10 секунд
			browser.implicitly_wait(10)

			# Открыть страницу music.youtube
			browser.get('https://music.youtube.com/')
			# Нажать на кнопку "Мой джем"
			browser.find_element_by_xpath("//a[@title='Мой джем']").click()
			browser.find_element_by_xpath("//div[@class='circle style-scope paper-spinner-lite']").click()
			time.sleep(99999)
		except Exception as e:
			print(e)
		finally:
			# Закрыть браузер
			browser.close()


def main():
	"""
	
	Основная main функция
	"""

	# Разбираем первоначальную строку на часы и минуты
	hour = int(TIME_START.split(':')[0])
	minute = int(TIME_START.split(':')[1])

	# Сохраняем текущую дату
	time_now = datetime.datetime.today()

	# Устанавливаем дату будильника

	# Временная переменная под дату и время будильника
	# Забираем год, месяц, день из текущей даты
	# Часы и минуты устанавливаем из выпаршеных значений
	temp_time = datetime.datetime(time_now.year, time_now.month, time_now.day, hour, minute)

	# Проверяем, если текущее время больше, чем временное временая переменная
	# то нужно добавить к дате один день 
	if time_now > temp_time:
		# Добавляем один день
		time_alarm = datetime.datetime(time_now.year, time_now.month, time_now.day + 1, hour, minute)
	# Если нет, то время будильника = временной переменной 
	else:
		time_alarm = temp_time

	print(f"Будильник установлен на: {time_alarm}")

	# Ждем времени наступления будильника наступления 
	while time_alarm > datetime.datetime.today():
		print(f"******    ОСТАЛОСЬ    >>> {time_alarm - datetime.datetime.today()}", end='')
		print('\r', end='')

		time.sleep(1)

	start_alarm()


if __name__ == '__main__':
	main()