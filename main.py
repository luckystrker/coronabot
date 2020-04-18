import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from bs4 import BeautifulSoup


token = "26a1c4b052f5cbee679a7ce920131f6b694aaa567e48855bbace0822dfd791eb128e996ec19fb1fb26a2f"
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


photos = ['photo-194380991_457239022', 'photo-194380991_457239023',
'photo-194380991_457239024', 'photo-194380991_457239025',
'photo-194380991_457239026', 'photo-194380991_457239027',
'photo-194380991_457239028', 'photo-194380991_457239029',
'photo-194380991_457239030', 'photo-194380991_457239031',
'photo-194380991_457239032', 'photo-194380991_457239033',
'photo-194380991_457239034', 'photo-194380991_457239035',
'photo-194380991_457239036']


def getInfo():
    site = requests.get("https://xn--80aesfpebagmfblc0a.xn--p1ai/")

    if site.status_code != 200:
        return "Извините, в данный момент информация недоступна."
    html = site.text

    soup = BeautifulSoup(html, features="html.parser")
    # ill_count = soup.find('div', class_="cv-countdown__item-value _accent").text
    # day_ill_count = soup.fint('div', class_="")

    all = soup.find_all('div', class_="cv-countdown__item-value")
    # all = soup.find_all('div', class_="cv-countdown__item-value _accent")

    tests = all[0].text
    ill = all[1].text
    day_ill = all[2].text
    heal = all[3].text
    dead = all[4].text
    info = "На данный момент в России по коронавирусу ситуация следующая:\n" \
           "Проведено тестов: {}\n" \
           "Случаев заболевания: {}\n" \
           "Случаев заболевания за последние сутки: {}\n" \
           "Выздоровевших: {}\n" \
           "Умерших: {}.".format(tests, ill, day_ill, heal, dead)
    return info


def random_id():
    return random.randint(0, 10000000000000)


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if event.text.lower() in ['начать', 'привет']:
                vk.messages.send(
                    user_id = event.user_id,
                    message = "Привет!",
                    keyboard = open('keyboard.json', 'r', encoding='UTF-8').read(),
                    random_id = random_id()
                )
            elif event.text.lower() == 'ситуация в стране':
                vk.messages.send(
                    user_id=event.user_id,
                    message=getInfo(),
                    keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                    random_id=random_id()
                )
            elif event.text.lower() == 'мемы':
                vk.messages.send(
                    user_id=event.user_id,
                    message="",
                    keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                    random_id=random_id(),
                    attachment = random.choice(photos)
                )
            elif event.text.lower() == 'мифы':
                vk.messages.send(
                    user_id=event.user_id,
                    message='''-новым коронавирусом нельзя заразиться через письма и посылки
-нет никаких доказательств, что домашние животные, как собаки или кошки, могут быть переносчиками нового коронавируса
-вакцины против пневмонии не защищают от нового коронавируса
-высокая и низкая температура не убивает новый коронавирус
-новый коронавирус не лечится антибиотиками
-на данный момент лекарств для профилактики или лечения нового коронавируса нет. Тем не менее обращаться к врачу необхожимо каждому пациенту. Медицинская помощь поможет облегчить симптомы и не допустить дальнейшего развития заболевания''',
                    keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                    random_id=random_id()
                )
            elif event.text.lower() == 'симптомы':
                vk.messages.send(
                    user_id=event.user_id,
                    message=''' повышение температуры тела;
утомляемость;
сухой кашель.
У некоторых инфицированных могут также наблюдаться:
боли в мышцах и суставах;
заложенность носа;
выделения из носа;
боль в горле;
диарея.
В среднем с момента заражения до возникновения симптомов проходит 5-6 дней, хотя в отдельных случаях этот период может продолжаться до 14 дней.''',
                    keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                    random_id=random_id()
                )
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    message="Не понял ваше сообщение...",
                    keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                    random_id=random_id()
                )

