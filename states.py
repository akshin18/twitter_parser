from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='english', target='ru').translate('hello')
print(translated)