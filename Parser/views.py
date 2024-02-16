from bs4 import BeautifulSoup
from .models import Profile
from django.http import HttpResponse
import requests


def parse_and_save_profiles(request):
    url = 'https://bet-hub.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    widget_container = soup.find('div', {'class': 'ratings_long_term'})
    nicknames = widget_container.select('.capper_ticker')

    for nickname in nicknames:
        profile_nickname = nickname.text

        # Проверяем существует ли никнейм в базе данных, если да то не записываем, если нет то создаём
        if not Profile.objects.filter(nickname=profile_nickname).exists():
            Profile.objects.create(nickname=profile_nickname)

    return HttpResponse("Cохранение уникальных никнеймов завершено")
