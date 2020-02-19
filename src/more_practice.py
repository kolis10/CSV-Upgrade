# lst_of_lsts = [
#     ['first','second','third','fourth'],
#     ['dndj','fdsas','3eewr','cdfsedf'],
#     ['dsfdfw','rrerrt','iuyjgf','wertrtr'],
#     ['rgergr','rtgtg','gertgtgt','trt5gtt'],
#     ['thbfgd','dscsdf','sdfthygt','rbythu'],
#     ['nrxhs','ndxhdz','ndhxsbs','pdkidha']
# ]

# smaller_lst = lst_of_lsts[0]
# lst_dict = {}

# for x in lst_of_lsts:
#     if x > 0:
#         print(x)
#         # lst_dict[x] = lst_of_lsts[y]

# # print(lst_dict)

# #def lst_dict():
# #lst_dict = []

# # this_dict = {}
# # this_dict[smaller_lst[0][0]] = lst_of_lsts[1]
# # this_dict[smaller_lst[0][1]] = lst_of_lsts[2]
# # this_dict[smaller_lst[0][2]] = lst_of_lsts[3]
# # this_dict[smaller_lst[0][3]] = lst_of_lsts[4]

# # print(this_dict)
###########################################################################

# lst = ['first','second','third','fourth']

# lst1 = ['dndj','fdsas','3eewr','cdfsedf']
# lst2 = ['dsfdfw','rrerrt','iuyjgf','wertrtr']
# lst3 = ['rgergr','rtgtg','gertgtgt','trt5gtt']
# lst4 = ['thbfgd','dscsdf','sdfthygt','rbythu']

# for index, item in enumerate(list):
#     print(item, index)

# def make_dict(item):

#     dct = {}
#     dic_lst = []

#     for index, item in enumerate(list):
#         dct["first"] = lst1[item]
#         dct["second"] = lst2[item]
#         dct["third"] = lst3[item]
#         dct["fourth"] = lst4[item]
#         dic_lst.append(dct)
#     return dic_lst

#     # if q == 3:
#     #     dic_lst.append(dct)
#     #     return dic_lst
#     # else:
#     #     dic_lst.append(dct)
#     # return make_dict(q + 1)

# print(make_dict(2))

# def calc_factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * calc_factorial(x-1))

# print(calc_factorial(5))
#########################################
lst = ['first','second','third','fourth']

lst1 = ['dndj','fdsas','3eewr','cdfsedf']
lst2 = ['dsfdfw','rrerrt','iuyjgf','wertrtr']
lst3 = ['rgergr','rtgtg','gertgtgt','trt5gtt']
lst4 = ['thbfgd','dscsdf','sdfthygt','rbythu']

for i, word in enumerate(lst):
    lst1 = lst1[i]
    lst2 = lst2[i]
    lst3 = lst3[i]
    lst4 = lst4[i]