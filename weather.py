import requests


def get_weather(location, base_url='http://wttr.in',
                params=None):
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
    if params is None:
        params = {'nTqu': '', 'lang': 'en'}
   url_template = '{}/{}'
    url = url_template.format(base_url, location)
    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.text


def main():
    offices = ('san francisco', 'Лондон', 'svo')
    for office in offices:
        print(get_weather(office))

    cherepovets_wttr_params = {'nTqM': '', 'lang': 'ru'}
    print(get_weather('Череповец', params=cherepovets_wttr_params))


if __name__ == '__main__':
    main()
