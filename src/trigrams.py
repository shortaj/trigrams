"""This module implements the trigrams algorithm"""

import io

def main(file_path):
    return generateTrigrams(getText(file_path))


def getText(file_path):
    """Get file and returns words in a list"""
    f = io.open(file_path, encoding='utf-8')
    return f.read().lower().split()

def generateTrigrams(textList):
    trigram_dict = {}
    for index, word in enumerate(textList[:-2]):
        key = word + ' ' + textList[index + 1]
        if key in trigram_dict:
            value = trigram_dict.get(key)
            value.append(textList[index + 2])
        else:
            trigram_dict.setdefault(key, [textList[index + 2]])

    return trigram_dict

print(main('./text.txt'))
