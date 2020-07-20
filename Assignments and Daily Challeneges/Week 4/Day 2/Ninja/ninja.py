# 1.

# my_num = [
# [3, 47, 99, -80, 22, 97, 54, -23, 5, 7],
# [44, 91, 8, 24, -6, 0, 56, 8, 100, 2],
# [3, 21, 76, 53, 9, -82, -3, 49, 1, 76], 
# [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# ]

# print(my_num)
# high_list = []

# for num_lists in my_num:
#     my_sort = sorted(num_lists, reverse=True)
#     print(my_sort)
#     print(sum(my_sort))

# first_last = [] 
# for num_lists in my_num:
#     first_last.append(num_lists[0])
#     first_last.append(num_lists[-1])

# print(first_last)

# over_fifty = []

# for num_lists in my_num:
#     for num in num_lists:
#         if num > 50:
#             over_fifty.append(num)

# print(over_fifty)

# under_ten = []

# for num_lists in my_num:
#     for num in num_lists:
#         if num < 10:
#             under_ten.append(num)

# print(under_ten)

# squared = []

# for num_lists in my_num:
#     for num in num_lists:
#         squared.append(num**2)

# print(squared)

# my_set = []
# for nums in my_num:
#     my_set += nums

# set(my_set)
# print(my_set)
# print(len(my_set))


# 2.

# marvel = "There are over 20 movies in the Marvel Cinematic Universe, and it becomes challenging to keep track of the characters and story-lines. And then there are the Infinity Stones that appear in select films and they suddenly gain their relevance. Some of the movies that came later are set at an earlier time which adds to the complexity. So, at a glance, here are all the Marvel Cinematic Universe Movies in the order of the story, the timeline, and the characters."

# print(f'The paragraph has {len(marvel)} charachters.')

# count = 0
# for period in marvel:
#     if period == ".":
#         count += 1
# print(f'There are {count} sentences in the paragraph.')

# new_count = 1
# for period in marvel:
#     if period == " ":
#         new_count +=1
# print(f'There are {new_count} words in the paragraph.')

# not_blank = 0
# for period in marvel:
#     if period != " ":
#         not_blank += 1
# print(f'There are {not_blank} letters in the paragraph.')

# 3.

# sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

# counts = dict()
# words = sentence.split(" ")

# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1

# count_dict = counts.items()
# count_sorted = sorted(count_dict)
# print(count_sorted)

