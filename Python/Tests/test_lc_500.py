from python.problems.lc524_longest_word_in_dict_thru_deleting import find_longest_word


def test_find_longest_word():
    assert find_longest_word("abpcplea", ["ale", "apple", "monkey", "plea"]) == "apple"
