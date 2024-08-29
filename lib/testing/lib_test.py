import pytest
from list_comprehension import return_evens, make_exclamation

class TestReturnEvens:
    '''Function return_evens()'''

    def test_return_empty_list_if_odds(self):
        '''Returns empty list when num_list has no evens'''
        num_list = range(1, 10, 2)  # This generates: [1, 3, 5, 7, 9]
        assert return_evens(num_list) == []  # No even numbers, should return []

    def test_return_evens(self):
        '''Returns list of even numbers from num_list'''
        num_list = range(10)  # This generates: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert return_evens(num_list) == [0, 2, 4, 6, 8]  # Should return even numbers


class TestMakeExclamation:
    '''Function make_exclamation()'''

    def test_return_empty_list_if_empty_input(self):
        '''Returns empty list when sentence_list is empty'''
        assert make_exclamation([]) == []  # Empty input should return empty list

    def test_return_exclamation_list(self):
        '''Returns list of sentences with exclamation marks appended'''
        sentence_list = [
            "I like computers",
            "I require coffee",
            "Live long and prosper",
        ]
        assert make_exclamation(sentence_list) == [
            "I like computers!",
            "I require coffee!",
            "Live long and prosper!",
        ]  # Each sentence should have an exclamation mark appended
