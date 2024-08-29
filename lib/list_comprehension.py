def return_evens(num_list):
    '''Returns a list of even numbers from num_list.'''
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    '''Returns a list of sentences with an exclamation mark appended to each.'''
    return [sentence + '!' for sentence in sentence_list]
