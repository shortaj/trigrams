"""This module implements the trigrams algorithm."""

import io
import random


def main(file_path, num_words_to_generate=100):
    """Return a trigram string based on text file."""
    return generate_trigrams(get_text(file_path), num_words_to_generate)


def get_text(file_path):
    """Return words in a list from a text file."""
    f = io.open(file_path, encoding='utf-8')
    return f.read().lower().split()


def generate_trigrams(text_list, num_words_to_generate):
    """Return a trigram string based on a list of words."""
    output_string = ''
    trigram_dict = generate_dict(text_list)
    arbitrary_word_pair = generate_random_key(trigram_dict)

    for i in range(num_words_to_generate):
        next_word = generate_random_value(trigram_dict, arbitrary_word_pair)
        arbitrary_word_pair = arbitrary_word_pair.split()[1] + ' ' + next_word
        output_string += ' ' + next_word

    return output_string


def generate_dict(text_list):
    """Return a trigram dictionary from a list of words."""
    trigram_dict = {}
    for index, word in enumerate(text_list[:-2]):
        key = word + ' ' + text_list[index + 1]
        if key in trigram_dict:
            value = trigram_dict.get(key)
            value.append(text_list[index + 2])
        else:
            trigram_dict.setdefault(key, [text_list[index + 2]])

    return trigram_dict


def generate_random_key(trigram_dict):
    """Return a random key from a dictionary."""
    return random.choice(list(trigram_dict.keys()))


def generate_random_value(trigram_dict, key):
    """Return a random value from a key in a dictionary."""
    return random.choice(trigram_dict.get(key))

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 3:
        file_path = sys.argv[1]
        num_of_words = int(sys.argv[2])
        print(main(file_path, num_of_words))
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
        print(main(file_path))
    else:
        print('Please enter the file path to a text file. A number of words to be generated is optional.')