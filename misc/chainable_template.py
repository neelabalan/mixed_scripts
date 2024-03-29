import string

## Generated with Github Copilot


class ChainableTemplate(string.Template):
    def __or__(self, other):
        if isinstance(other, dict):
            return ChainableTemplate(super().safe_substitute(other))
        else:
            return ChainableTemplate(self.template + ' ' + str(other))

    def __str__(self):
        return self.template


## Also generated with Github Copilot :)


def test_chainable_template():
    # Test substitution with a dictionary
    template = ChainableTemplate('Hello, ${name}')
    result = template | {'name': 'John'}
    assert str(result) == 'Hello, John'

    # Test chaining with another string
    template = ChainableTemplate('Hello, ${name}')
    result = (template | {'name': 'John'}) | 'How are you?'
    assert str(result) == 'Hello, John How are you?'

    # Test chaining with another dictionary
    template = ChainableTemplate('Hello, ${name}. Today is ${day}')
    result = (template | {'name': 'John'}) | {'day': 'Monday'}
    assert str(result) == 'Hello, John. Today is Monday'

    # Test chaining with a string and a dictionary
    template = ChainableTemplate('Hello, ${name}.')
    result = (template | 'How are you?') | {'name': 'John'}
    assert str(result) == 'Hello, John. How are you?'


# **Not** generated by GitHub Copilot. I had look into the documentation
# pytest -s -o python_files=*.py misc/chainable_template.py
