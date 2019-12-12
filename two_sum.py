

def two_sum(input_nums, target):
    """
    accept list of numbers, and a target, print index of numbers that add to target
    """

    dict = {}

    for i,num in enumerate(input_nums):
        complement_to_target = target - num
        if complement_to_target in dict:
            print(  dict.get( complement_to_target), ",", i)
        else:
            dict[num] = i


input_nums = [2, 3, 7, 8]

two_sum(input_nums, 10)