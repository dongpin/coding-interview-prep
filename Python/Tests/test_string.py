
from python.basic_algorithm import string_algorithms as String


def test_is_palindrome():
    assert String.is_palindromic('aba')
    assert String.is_palindromic('abbbbbbbbbbba')
    assert not String.is_palindromic('ab')
    assert String.is_palindromic('')


lcsubsequence_test_cases = [(('a', 'a'), 'a'), (('ab', 'acbd'), 'ab'),
                            (('abcd', 'ac'), 'ac'), ((
                                'abcdefghijk', 'caegijk'), 'aegijk'),
                            (('a', ''), ''), (('', ''), '')]


def test_longest_common_subsequence():
    for t in lcsubsequence_test_cases:
        assert String.longest_common_subsequence(t[0][0], t[0][1]) == t[1]


def test_longest_common_subsequence_iterative():
    for t in lcsubsequence_test_cases:
        assert String.longest_common_subsequence_iterative(
            t[0][0], t[0][1]) == t[1]


lcsubstring_test_cases = [(('OldSite:GeeksforGeeks.org', 'NewSite:GeeksQuiz.com'), 10),
                          (('abc', 'cba'), 1), (('abcd', 'efgh'), 0), (('', ''), 0),
                          (('abcde', 'ace'), 1)]


def test_longest_common_substring_iterative():
    for t in lcsubstring_test_cases:
        assert String.longest_common_substring_iterative(
            t[0][0], t[0][1]) == t[1]


edit_distance_test_cases = [('a', '', 1), ('abc', 'abc', 0), ('abc', 'cde', 3),
                            ('', '', 0)]


def test_edit_distance():
    for t in edit_distance_test_cases:
        assert String.edit_distance(t[0], t[1]) == t[2]
