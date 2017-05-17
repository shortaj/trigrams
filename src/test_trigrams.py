"""A file to test the functions of trigrams."""
import pytest

SAMPLE_TXT = ''


@pytest.mark.parametrize('file_path', SAMPLE_TXT)
def test_get_text(file_path):
    """A test function for get_text."""
    pass

@pytest.mark.parametrize('text_list', SAMPLE_DICT)
def test_generate_trigrams(text_list):
    """A test function for generate_trigrams."""
    pass
