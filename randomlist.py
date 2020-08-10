import random

def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result

# list = [1, 2, 3, 4]
# print(get_random(list))
# print(get_random([]))