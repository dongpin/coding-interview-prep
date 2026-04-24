# 345. Reverse Vowels of a String

def reverse_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    arr = list(s)
    i, j = 0, len(arr) - 1
    while i <= j:
        if arr[i] not in vowels:
            i += 1
        elif arr[j] not in vowels:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return ''.join(arr)
