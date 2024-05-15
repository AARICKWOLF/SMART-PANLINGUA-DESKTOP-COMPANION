from googletrans import Translator

translator = Translator()

# Translate text to Tamil
text_to_translate_tamil = "Hello, how are you?"
translated_text_tamil = translator.translate(text_to_translate_tamil, dest='ta')  # for Tamil language
print("Translated text (Tamil):", translated_text_tamil.text)

# Translate text to Malayalam
text_to_translate_malayalam = "Hello, how are you?"
translated_text_malayalam = translator.translate(text_to_translate_malayalam, dest='ml')  # for Malayalam language
print("Translated text (Malayalam):", translated_text_malayalam.text)


# Translate text to telugu
text_to_translate_telugu = "Hello, how are you?"
translated_text_telugu = translator.translate(text_to_translate_telugu, dest='te')  # for telugu language
print("Translated text (telugu):", translated_text_telugu.text)