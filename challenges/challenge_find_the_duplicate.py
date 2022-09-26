def negative_str(nums):
    for itens in nums:
        if isinstance(itens, str) or itens < 0 or itens == "":
            return False


def find_duplicate(nums):
    sorted_nums = sorted(nums)
    if negative_str(sorted_nums) is False:
        return False
    if (return_duplicate(sorted_nums) is not False
       and return_duplicate(sorted_nums) is not None):
        return return_duplicate(sorted_nums)
    else:
        return False


def return_duplicate(nums):
    try:
        for i, itens in enumerate(nums):
            if itens == nums[i+1]:
                return itens
    except IndexError:
        return False
