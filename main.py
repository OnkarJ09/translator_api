import requests


def translate_text(text, target_language):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target_language}&dt=t&q={text}"
    response = requests.get(url)
    translation = response.json()[0][0][0]
    return translation


# Example usage
text_to_translate = "Hello, how are you?"
target_language = "fr"

translated_text = translate_text(text_to_translate, target_language)
print("Translated text:", translated_text)
