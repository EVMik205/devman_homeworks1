import requests
default_wttr_params = {'nTqu': '', 'lang': 'en'}


def get_weather(location, base_url='http://wttr.in',
                params=default_wttr_params):
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

    url_template = '{}/{}'
    url = url_template.format(base_url, location)
    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.text


def main():
    print(get_weather('san francisco'))

    offices = ('Лондон', 'svo', 'Череповец')
    for office in offices:
        print(get_weather(office))

    cherepovets_wttr_params = {'nTqnM': '', 'lang': 'ru'}
    print(get_weather('Череповец', params=cherepovets_wttr_params))


if __name__ == '__main__':
    main()
