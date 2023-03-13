import requests

def get_weather(location, base_url='http://wttr.in', params='nTqu&lang=en'):
    """Возвращает прогноз погоды.
  
    Параметры
    ---------
    location : str
        Место, для которого запрашиваем прогноз.  
    base_url : str, optional
        Адрес сервера (по умолчанию 'http://wttr.in').
    params : str, optional
        Параметры выдачи (по умолчанию 'nTqu&lang=en')
    """

    url_template = '{}/{}?{}'
    url = url_template.format(base_url, location, params)
    response = requests.get(url)
    response.raise_for_status()
    
    return(response.text)

print(get_weather('san francisco'))

offices = ('Лондон', 'svo', 'Череповец')
for place in offices:
    print(get_weather(place))

print(get_weather('Череповец', params='nTqnmM&lang=ru'))