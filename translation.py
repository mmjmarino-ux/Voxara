from deep_translator import GoogleTranslator

def translate_text(text, target_language, source_language='auto'):
    try:
        result = GoogleTranslator(source=source_language, target=target_language).translate(text)
        return result
    except Exception as e:
        return f"Translation error: {str(e)}"