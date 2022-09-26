def is_palindrome_recursive(word, low_index, high_index):
    word_len = word[low_index:high_index]

    if word == "":
        return False

    if len(word_len) < 1:
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
