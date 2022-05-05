nums = [1,3,5,6,4,2,8]

# even_double_num=[]
# for num in nums:
#     if (num%2) == 0:
#         even_double_num.append(num*2)
# print(even_double_num)

even_double_num=[num*2 for num in nums if (num%2) == 0]
odd_double_num=[num*2 for num in nums if (num%2) != 0]
print(even_double_num)
print(odd_double_num)