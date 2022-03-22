from statistics import median, mean
import re
SYMBOLS_TO_REPLACE = "?!.;"


class Handler:

    @staticmethod
    def get_text():
        with open("text.txt", "r", encoding="UTF-8") as file:
            inside = file.read().lower()
            return inside

    @staticmethod
    def custom_split(text):
        for i in SYMBOLS_TO_REPLACE:
            text = text.replace(i, '')
        text = text.replace('\n', '').replace(';', '.')
        return text.split(' ')

    @staticmethod
    def get_words_numb(text):
        words = {}
        for element in text:
            if words.get(element, None):
                words[element] += 1
            else:
                words[element] = 1

        return dict(words)

    @staticmethod
    def show_dictionary(dictionar):
        for key, value in dictionar.items():
            print("{0}: {1}".format(key, value))

    @staticmethod
    def words_in_sentence(text):
        num_of_words = []
        text = text.replace('?', '.').replace('!', '.').replace('...', '.').replace(';', '.')
        for i in filter(None, text.split('.')):
            num_of_words.append(len(i.split()))
        num_of_words.remove(0)
        return num_of_words

    @staticmethod
    def average_words_number(text):
        return int(mean(Handler.words_in_sentence(text)))

    @staticmethod
    def median_words_number(text):
        return int(median(Handler.words_in_sentence(text)))

    @staticmethod
    def n_grams(text, n, k):
        list_of_words = re.split("[^a-za-я]", text.lower())
        list_of_words = list(
            filter(lambda word: len(word) >= n, list_of_words))

        ngrams = []
        for word in list_of_words:
            word_ngram = list(zip(*[word[i:] for i in range(k)]))
            for ngram in word_ngram:
                ngrams.append(''.join(ngram))
        ngrams_count = Handler.get_words_numb(ngrams)
        sorted_values = sorted(ngrams_count.values(), reverse=True)
        sorted_dict = {}
        for i in sorted_values:
            for j in ngrams_count.keys():
                if ngrams_count[j] == i:
                    sorted_dict[j] = ngrams_count[j]
        return dict(list(sorted_dict.items())[:n])
