 # Translate queries (GoogleTranslator)

from deep_translator import GoogleTranslator
from langdetect import detect

def translate_to_english(query: str):
    lang = detect(query)
    if lang != "en":
        translated = GoogleTranslator(source="auto", target="en").translate(query)
        return translated, lang
    return query, "en"

def translate_back(answer: str, target_lang: str):
    if target_lang != "en":
        return GoogleTranslator(source="en", target=target_lang).translate(answer)
    return answer

def multilingual_qa(query: str, qa_chain):
    translated_query, lang = translate_to_english(query)
    result = qa_chain({"question": translated_query})
    english_answer = result["answer"]
    return translate_back(english_answer, lang)
