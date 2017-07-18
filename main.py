from bs4 import BeautifulSoup
import urllib.request
from os import system
from time import sleep

class Main():

    def __init__(self, site_name, season, episode, *args, **kwargs):
        self.season = season # начальный сезон
        self.episode = episode # начальная серия
        self.link = site_name + "/season-{}/episode-{}".format(season, episode)

        with urllib.request.urlopen(self.link) as response:
            # Запись в переменную html код страницы
            html = response.read()

        soup = BeautifulSoup(html, 'html.parser')

        # Поиск тега с классом .empty
        search_empty_tag = soup.select(".empty")

        check_new_video(search_empty_tag) # Проверка новых серий

        check_new_season()

    # Проверка нового сезона
    def check_new_season(self):
        season = self.season + 1
        episode = 1
        link = self.link
        print(link)

    # Отправка аудио сигнала
    def send_audio(count, time_loop):
        i = count # кол-во уведомлений
        while i >= 0:
            system('beep.mp3')
            sleep(time_loop) # интервал уведомлений в секундах
            i = i - 1

    # Проверка новой серии
    def check_new_video(empty_tag):
        if not empty_tag:
            # Если такого тега нет, то есть новые серии.
            print("Новые серии!")
            send_audio(3, 60*5) # Звуковые сигналы (5 минут интервал)
            return True
            # Затем проверить 1 серию нового сезона, если ее нет,
            # тогда проверить следующую текущего сезона, если она есть,
            # тогда подать сигнал и написать в телеграмм.
        else:
            print("Нет новых серий")
            return False


wrecked = Main("http://www.torrentino.me/serial/888489-wrecked", 2, 5)

