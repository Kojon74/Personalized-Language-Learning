from google.cloud import translate

# export GOOGLE_APPLICATION_CREDENTIALS="/Users/kenjohnson/Documents/Work/Personalized-Language-Learning/GoogleCloudKey_PLL.json"

class Translate():
    def __init__(self):
        # _wordList = ["Apple", "Orange", "Grape", "Pineapple", "Grapefruit"]
        pass

    def translate_words(self, word_list, target_language):
        translated_list = self.sample_translate_text("personalized-language-learning", word_list, target_language)
        dictionary = self.create_dictionary(word_list, translated_list)
        self.print_translations(dictionary)

    def sample_translate_text(self, project_id="YOUR_PROJECT_ID", word_list=[], target_language="fr"):
        """Translating Text."""

        client = translate.TranslationServiceClient()

        parent = client.location_path(project_id, "global")

        # Detail on supported types can be found here:
        # https://cloud.google.com/translate/docs/supported-formats
        response = client.translate_text(
            parent=parent,
            contents=word_list,
            mime_type="text/plain",  # mime types: text/plain, text/html
            source_language_code="en-US",
            target_language_code=target_language,
        )
        return response.translations

    def print_translations(self, dictionary):
        # Display the translation for each input text provided
        print(str(dictionary))

    def create_dictionary(self, english_list, target_list):
        if len(english_list) != len(target_list):
            return  #Return excetion
        dictionary = {english_list[i] : target_list[i].translated_text for i in range(len(english_list))}
        return dictionary
        
# Tests
word_list = ["Apple", "Orange", "Grape", "Pineapple", "Grapefruit"]
translation = Translate()
translation.translateWords(wordList, "fr")
