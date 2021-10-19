import vk_api
from yandex_music import Client
import configparser
import time as tm

#Подключение конфига
config = configparser.ConfigParser()
config.read("cfg.ini")
YaLogin = config["YandexAccount"]["login"]
YaPassword = config["YandexAccount"]["password"]
VkLogin = config["Vk"]["username"]
VkPassword = config["Vk"]["password"]
wait = config["misc"]["waitingtime"]

if ((YaLogin == 'YOUR_YANDEX_LOGIN_HERE@yandex.com') or (VkLogin == 'YOUR_VK_USERNAME_HERE')):
    print('Edit cfg.ini file!!!')

#Авторизация в Яндекс
client = Client.from_credentials(YaLogin, YaPassword)
#Авторизация в ВК
vk_session = vk_api.VkApi(login = VkLogin, password = VkPassword)
vk_session.auth()
vk = vk_session.get_api()

while (True):
    queues = client.queues_list()
    last_queue = client.queue(queues[0].id)
    last_track_id = last_queue.get_current_track()
    last_track = last_track_id.fetch_track()
    artists = ', '.join(last_track.artists_name())
    title = last_track.title
    songname = f'Слушает: {artists} - {title}'
    print('status.set return code:', vk.status.set(text = songname))
    tm.sleep(10)
