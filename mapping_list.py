from abc import abstractmethod


nums=[2,3,4,5,6,7]

# def mapfunction(num):
#     return num*2

# nums = list(map(mapfunction,nums))
# print(nums)

a = [num*2 for num in nums]
print(a)