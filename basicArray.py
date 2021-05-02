#wow


array = [1,2,5]
array2 = [1,2,5]
print(len(array))			# prints length of an array
print(max(array)) 			# prints max value
print(min(array))
print(sum(array))

print(type(array))			# prints type of array --> list 

print(array == array2) 		# True 


# indexing 

# array[0]
# array[1:]



# mutability 

x = 5 
print(x + 1)		# 6 
x + 1 				# x is not 6.. because x is immutable 
print(x)

x = x + 1 			# now x is 6 
print x 


# lists are mutable 

x = [1,2,3]
x.append(2)			# add element 2 at the end of the list 
print(x)			# [1,2,3]

# x = x.append(2) 	# this is not right. lists are mutable. This will return wrong output 

x = [1,2,3,1,2,5,6,7]
print(x.count(1))	# counts element 1 in the array x 
print(x.index(2))	# gets the index of number 2 (but only the first occurence)
		
x = x + ['a']		# adding list with a list 
y = [1] + x 
print(x)
print(y)

x = [1,2,3,4,5,6,7,8]
removed = x.pop(3)	# removing the 3rd index, so 4 and stores it in the variable called removed 
print(removed)
print(x)			# 4 is gone from the list 

x.remove(5)			# removes the element 5, not the index 5 
print(x)

x.extend([17, 19])	# adds the list to the another list 
print(x)
	
x.reverse() 		# reverses list (not available in string!)
print(x)

x.sort() 			# sorts the elements 
print(x)

y = ['a', 'dc', 1000000]		# integer comes before the summer 
y.sort()
print(y)

