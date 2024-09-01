import re
import sys

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.", file=sys.stdout)
        else:
            self._value = new_value

    def is_sentence(self):
        """Returns True if the value ends with a period."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if the value ends with a question mark."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Counts the number of sentences in the value."""
        # Use regex to split based on '.', '?', '!', but make sure to avoid empty splits
        sentences = re.split(r'[.?!]+', self.value)
        # Filter out any empty strings that result from split
        return len([s for s in sentences if s.strip()])
