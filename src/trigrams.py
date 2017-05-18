"""This module implements the trigrams algorithm."""

import io
import random


def main(file_path, num_words_to_generate=100):
    """A function that calls get_text and generate_trigrams returns dict."""
    return generate_trigrams(get_text(file_path), num_words_to_generate)


def get_text(file_path):
    """Get file and returns words in a list."""
    f = io.open(file_path, encoding='utf-8')
    return f.read().lower().split()


def generate_trigrams(text_list, num_words_to_generate):
    """Return a trigram string based on the text_list file."""
    output_string = ''
    trigram_dict = generate_dict(text_list)
    arbitrary_word_pair = generate_random_key(trigram_dict)

    for i in range(num_words_to_generate):
        next_word = generate_random_value(trigram_dict, arbitrary_word_pair)
        arbitrary_word_pair = arbitrary_word_pair.split()[1] + ' ' + next_word
        output_string += ' ' + next_word

    return output_string


def generate_dict(text_list):
    """Return a trigram dictionary string."""
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


print(main('./text.txt'))
