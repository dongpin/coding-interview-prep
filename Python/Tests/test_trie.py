from python.basic_algorithm.trie import Trie


def test_trie():
    trie = Trie()
    trie.build_trie(['add', 'new', 'slk', 'above'])
    assert trie.search('add')
    assert not trie.search('ADD')
    assert not trie.search('ad')
    assert not trie.search('addd')
    assert not trie.search('')
    trie.add('cup')
    assert trie.search('cup')
