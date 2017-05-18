"""A file to test the functions of trigrams."""
import pytest

SAMPLE_TXT_LIST = [
    'i', 'wish', 'i', 'may', 'i', 'wish', 'i',
    'might', 'i', 'wish', 'i', 'may', 'i', 'wish', 'i',
    'might', 'monkey', 'banana', 'might', 'monkey', 'banana',
    'might', 'monkey', 'banana', 'burger', 'waffle', 'soda',
    'burger', 'waffle', 'soda', 'may', 'i', 'waffle',
    'soda', 'may', 'i', 'i', 'wish', 'banana', 'burger',
    'might', 'banana', 'burger', 'might', 'i', 'wish',
    'i', 'may', 'i', 'wish', 'i', 'might', 'monkey', 'banana'
]

SAMPLE_DICT = {
    'i wish': ['i', 'i', 'i', 'i', 'banana', 'i', 'i'],
    'wish i': ['may', 'might', 'may', 'might', 'may', 'might'],
    'i may': ['i', 'i', 'i'],
    'may i': ['wish', 'wish', 'waffle', 'i', 'wish'],
    'i might': ['i', 'monkey', 'monkey'],
    'might i': ['wish', 'wish'],
    'might monkey': ['banana', 'banana', 'banana', 'banana'],
    'monkey banana': ['might', 'might', 'burger'],
    'banana might': ['monkey', 'monkey'],
    'banana burger': ['waffle', 'might', 'might'],
    'burger waffle': ['soda', 'soda'],
    'waffle soda': ['burger', 'may', 'may'],
    'soda burger': ['waffle'],
    'soda may': ['i', 'i'],
    'i waffle': ['soda'],
    'i i': ['wish'],
    'wish banana': ['burger'],
    'burger might': ['banana', 'i'],
    'might banana': ['burger']
}


@pytest.mark.parametrize('file_path', SAMPLE_TXT_LIST)
def test_get_text(file_path):
    """A test function for get_text."""
    from trigrams import get_text
    assert get_text('./text.txt') == SAMPLE_TXT_LIST


@pytest.mark.parametrize('text_list', SAMPLE_DICT)
def test_generate_dict(text_list):
    """A test function for generate_dict."""
    from trigrams import generate_dict
    assert generate_dict(SAMPLE_TXT_LIST) == SAMPLE_DICT


@pytest.mark.parametrize('trigram_dict', SAMPLE_DICT)
def test_generate_random_key(trigram_dict):
    """A test function for generate_random_key."""
    from trigrams import generate_random_key
    assert generate_random_key(SAMPLE_DICT) in SAMPLE_DICT


# @pytest.mark.parametrize('trigram_dict', 'key', SAMPLE_DICT)
# def test_generate_random_value(trigram_dict, key):
#     """A test function for generate_random_value."""
#     from trigrams import generate_random_value
#     from trigrams import generate_random_key
#     # assert generate_random_value(SAMPLE_DICT, generate_random_key(SAMPLE_DICT))
#     assert generate_random_value(SAMPLE_DICT, generate_random_key(SAMPLE_DICT)) in list(SAMPLE_DICT.values())


