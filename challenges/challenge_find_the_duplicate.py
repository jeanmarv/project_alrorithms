def find_duplicate(nums):
    sorted_nums = sorted(nums)
    try:
        for i, itens in enumerate(sorted_nums):
            if isinstance(itens, str) or itens < 0:
                return False
            if itens == sorted_nums[i+1]:
                return itens
    except IndexError:
        return False
    return False
