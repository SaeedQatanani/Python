# #1
# def downCounter(num):
#     list = []
#     for x in range(num,-1,-1):
#         list.append(x)
#     return list
# print(downCounter(5))

# #2
# def print_return(list):
#     print(list[0])
#     return list[1]
# print_return([1,2])
# print(print_return([1,2])+1)

# #3
# def first_plus_length(list):
#     sum = list[0] + len(list)
#     return sum
# print(first_plus_length([1,2,3,4,5]))

# #4
# def values_greater_than_second(list):
#     if len(list) <= 2:
#         return False
#     else:
#         num = list[1]
#         new_list =[]
#         counter = 0
#         for i in range (len(list)):
#             if list[i] > num:
#                 new_list.append(list[i])
#                 counter += 1
#     print(counter)
#     return new_list
# print(values_greater_than_second([5,2,3,2,1,4,4]))

# #5
# def length_and_value(size, value):
#     list = []
#     for i in range (size):
#         list.append(value)
#     return list
# print(length_and_value(4,7))
# print(length_and_value(6,2))
