# Translate Text with MyMemory API
### like google translator for free

This Python script provides a simple function to translate text from one language to another using the MyMemory API.

## Introduction

The `translate_text.py` script allows you to translate text from a source language to a target language using the MyMemory API. The script is easy to use and can be integrated into your own Python applications.

## How it Works

The script defines a single function, `translate_text`, which takes three parameters: `text` (the text to be translated), `source_lang` (the source language of the text), and `target_lang` (the language to translate the text into).

The function uses the `requests` module to send a GET request to the MyMemory API with the specified text and language parameters. The API returns a JSON response containing the translated text, which is then extracted and returned by the function.

## Features

* Translates text from one language to another using the MyMemory API
* Easy to use and integrate into your own Python applications
* Supports all languages supported by the MyMemory API

## Contribution

We welcome contributions to this project! If you would like to contribute, please submit a pull request with your changes. We ask that you follow the [Python style guide](https://www.python.org/dev/peps/pep-0008/) and include documentation for any new features or changes.


## Usage

To use the `translate_text` function, simply import the `translate_text` module and call the function with the text and language parameters:
```python
import translate_text

text_to_translate = "Hello, how are you?"
source_language = "en"
target_language = "fr"

translated_text = translate_text.translate_text(text_to_translate, source_language, target_language)
print("Translated text:", translated_text)
```

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

