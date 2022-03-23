import argparse
from text_handler import Handler


if __name__ == '__main__':
    text = Handler.get_text()
    Handler.show_dictionary(Handler.get_words_numb(Handler.custom_split(text)))
    print("Average words number per sentence is:")
    print(Handler.average_words_number(text))
    print("Median words number per sentence is:")
    print(Handler.median_words_number(text))

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-n', help=' input n', default=10)
    argument_parser.add_argument('-k', help='input k', default=4)
    arguments = argument_parser.parse_args()
    n = int(arguments.n)
    k = int(arguments.k)
    print(f"List of ngrams where n= {n} k={k}")
    print(Handler.n_grams(text, n, k))
