"""This module implements the trigrams algorithm."""

import io


def main(file_path):
    """A function that calls get_text and generate_trigrams returns dict."""
    return generate_trigrams(get_text(file_path))


def get_text(file_path):
    """Get file and returns words in a list."""
    f = io.open(file_path, encoding='utf-8')
    return f.read().lower().split()


def generate_trigrams(text_list):
    """A function that returns a dict based on the get_text file."""
    trigram_dict = {}
    for index, word in enumerate(text_list[:-2]):
        key = word + ' ' + text_list[index + 1]
        if key in trigram_dict:
            value = trigram_dict.get(key)
            value.append(text_list[index + 2])
        else:
            trigram_dict.setdefault(key, [text_list[index + 2]])

    return trigram_dict


print(main('./text.txt'))
