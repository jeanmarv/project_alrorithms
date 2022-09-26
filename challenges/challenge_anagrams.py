def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    for itens in first_list:
        if itens in second_list:
            second_list.remove(itens)
        else:
            return False
    if len(second_list) == 0:
        return True
    else: return False

print(is_anagram("pedra", "perdaa"))