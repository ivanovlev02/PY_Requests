import requests
from datetime import datetime

tag = 'Python'
day = 2

def tag_search(days, tag):

    finish_date = int(datetime.timestamp(datetime.now()))
    init_date = finish_date - days * 86400

    params = {
        'previous_day': init_date,
        'the_next_day': finish_date,
        'tagged': tag,
        'site': 'stackoverflow',
    }

    response = requests.get('https://api.stackexchange.com/2.2/questions', params=params)
    print(f"Вопросы, заданные за последние {day} дня, содержaщие тэг '{tag}': ")
    for question in response.json().get('items'):
        print(str(question['tags']), '\n')

tag_search(day, tag)