from google.cloud import translate

class Translate():
    def __init__(self):
        _wordList = ["Apple", "Orange", "Grape", "Pineapple", "Grapefruit"]

    def translate_words(self, wordList, targetLanguage):
        index = 0
        while index < 10 and index < len(wordList):
            self.sample_translate_text("personalized-language-learning", wordList[index], targetLanguage)
            index += 1

    def sample_translate_text(self, project_id="YOUR_PROJECT_ID", word="", targetLanguage="fr"):
        """Translating Text."""

        client = translate.TranslationServiceClient()

        parent = client.location_path(project_id, "global")

        # Detail on supported types can be found here:
        # https://cloud.google.com/translate/docs/supported-formats
        response = client.translate_text(
            parent=parent,
            contents=[word],
            mime_type="text/plain",  # mime types: text/plain, text/html
            source_language_code="en-US",
            target_language_code=targetLanguage,
        )
        # Display the translation for each input text provided
        for translation in response.translations:
            print(u"Translated text: {}".format(translation.translated_text))

# Tests
word_list = ["Apple", "Orange", "Grape", "Pineapple", "Grapefruit"]
# translation = Translate()
# translation.translateWords(wordList, "fr")