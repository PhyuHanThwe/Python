nums=[1,2,3,4,5,6]

# def even(num):
#     return (num%2)==0

# even_nums = list(filter(even,nums))
# print(even_nums)

# even_nums=[num for num in nums if (num%2)==0]
# print(even_nums)

odd_nums=[]
for num in nums:
    if (num%2) != 0:
        odd_nums.append(num)
print(odd_nums)