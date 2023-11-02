# input_elements = input().split()
# result = []
#
# for el in input_elements:
#     number = int(el)
#     result.append(-number)
#
# print(result)

line = input().split(' ')
opposites_list = [int(x) * -1 for x in line]
print(opposites_list)
