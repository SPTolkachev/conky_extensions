def translate(text: str, lang: str) -> str:
    ''' Todo: заменить на gettext '''
    texts = {
        'ru': {
            'days': 'дней',
            'less than a day': 'меньше суток',
            'the event has come': 'событие наступило'
        }
    }

    result = text
    if lang in texts:
        if text in texts[lang]:
            result = texts[lang][text]

    return result
