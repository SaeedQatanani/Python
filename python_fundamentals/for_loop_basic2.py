# #1
# def biggie_size(list):
#     for i in range (len(list)):
#         if list[i] > 0:
#             list[i]="big"
#     return list
# print(biggie_size([-1,3,5,-5]))

# #2
# def count_positives(list):
#     counter = 0
#     for i in range (len(list)):
#         if list[i] > 0:
#             counter += 1
#     if counter == 0:
#         return False
#     else:
#         list[len(list)-1] = counter
#         return list
# print(count_positives([-1,1,1,1]))
# print(count_positives([1,6,-4,-2,-7,-2]))

# #3
# def sum_total(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum
# print(sum_total([1,2,3,4]))
# print(sum_total([6,3,-2]))

# #4
# def average(list):
#     sum = 0
#     avg = 0
#     for i in list:
#         sum += i
#     avg = sum / len(list)
#     return avg
# print(average([1,2,3,4]))

# #5
# def length(list):
#     leng = len(list)
#     return leng
# print(length([37,2,1,-9]))

# #6
# def minimum(list):
#     if list == []:
#         return False
#     else:
#         min = list[0]
#         for i in range (1,len(list)):
#             if list[i] < min:
#                 min = list[i]
#         return min
# print(minimum([37,2,1,-9]))
# print(minimum([]))

# #7
# def maxmum(list):
#     if list == []:
#         return False
#     else:
#         max = list[0]
#         for i in range (1,len(list)):
#             if list[i] > max:
#                 max = list[i]
#         return max
# print(maxmum([37,2,1,-9]))
# print(maxmum([]))

# #8
# def ultimate_analysis(list):
#     dirct = {}
#     sumTotal = 0
#     length = len(list)
#     avg = 0
#     min = list[0]
#     max = list [0]
#     for i in range (length):
#         sumTotal += list[i]
#         if list[i] < min:
#             min = list[i]
#         elif list[i] < max:
#             max = list[i]
#     avg = sumTotal/length
#     dirct = {'sumTotal':sumTotal, 'average':avg, 'minimum':min, 'maximum':max, 'length':length}
#     return dirct
# print(ultimate_analysis([37,2,1,-9]))

# #9
# def reverse_list(list):
#     temp = 0
#     j = len(list)-1
#     for i in range(int(len(list)/2)):
#         temp = list[i]
#         list[i] = list[j]
#         list[j] = temp
#         j -= 1
#     return list
# print(reverse_list([37,2,1,-9]))

