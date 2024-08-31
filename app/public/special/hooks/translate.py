import requests as req


def use_translator(text, lang):
    response = req.get(
        f'https://api.mymemory.translated.net/get?q={text}&langpair=en|{lang}')
    return response
