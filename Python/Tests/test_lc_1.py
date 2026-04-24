from python.problems.lc2_add_two_numbers import ListNode, add_two_numbers
from python.problems.lc3_longest_substring_without_repeating_chars import (
    longest_substring_without_repeating_chars,
)
from python.problems.lc5_longest_palindromic_substr import longest_palindrome
from python.problems.lc32_longest_valid_parentheses import find_longest_valid_parenthese
from python.problems.lc44_wildcard_matching import is_wildcard_match
from python.problems.lc56_merge_intervals import merge


def test_add_two_nums():
    head1 = ListNode(2)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)
    head2 = ListNode(5)
    head2.next = ListNode(6)
    head2.next.next = ListNode(4)

    result = add_two_numbers(head1, head2)
    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 8
    assert result.next.next.next is None


def test_longest_substr_without_repeating_chars():
    assert longest_substring_without_repeating_chars("abcabcbb") == 3
    assert longest_substring_without_repeating_chars("bbbbb") == 1
    assert longest_substring_without_repeating_chars("pwwkew") == 3


def test_longest_palindromic_substr():
    assert longest_palindrome("babad") == "aba"
    assert longest_palindrome("cbbd") == "bb"


def test_longest_parentheses():
    assert find_longest_valid_parenthese(")()())") == 4


def test_wildcard_matching():
    assert is_wildcard_match("aa", "*")
    assert not is_wildcard_match("cb", "?a")
    assert is_wildcard_match("adceb", "*a*b")
    assert not is_wildcard_match("acdcb", "a*c?b")


def test_merge_intervals():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
