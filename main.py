import requests


def translate_text(text, source_lang, target_lang):
    url = "http://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}"
    }
    response = requests.get(url, params=params)
    translation = response.json()["responseData"]["translatedText"]
    return translation


# Example usage
text_to_translate = input("text: ")
source_language = "en"
target_language = "fr"

translated_text = translate_text(text_to_translate, source_language, target_language)
print("Translated text:", translated_text)
