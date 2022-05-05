# add=lambda n1,n2:n1+n2
# print(add(4,5))

# nums = [1,2,3,4,5,6]
# print(list(map(lambda num:(num*2),nums)))

nums=[1,2,3,4,5,6]
odd=list(filter(lambda num:(num%2)!=0 , nums))
print(odd)