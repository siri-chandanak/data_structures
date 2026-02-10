# Arrays in python
# Lists are mutable

'''
Operation  ---> Average Case
Copy  ---> O(n)
Append[1]  ---> O(1)
Pop last  ---> O(1)
Pop intermediate[2]  ---> O(n)
Insert  ---> O(n)
Get Item  ---> O(1)
Set Item  ---> O(1)
Delete Item  ---> O(n)
Iteration  ---> O(n)
Get Slice  ---> O(k)
Del Slice  ---> O(n)
Set Slice  ---> O(k+n)
Extend[1]  ---> O(k)
Sort  ---> O(n log n)
Multiply  ---> O(nk)
x in s  ---> O(n)
min(s), max(s)  ---> O(n)
Get Length  ---> O(1)
'''

arr1 = [i for i in range(1,100,5)]
print(arr1)

arr2 = [i//2 for i in arr1]
print(arr2)

print(len(arr1))  #----->  O(1)
print(arr2[5])    #----->  O(1)
print(arr1[2:7])  #----->  O(k)

arr1.append(105)  #----->  O(1)
arr1[6] = 25      #----->  O(1)

arr3 = arr2.copy()  # Different Address    -----------> O(n)
print(id(arr2))
print(id(arr3))

arr4=arr1    # same address, both pointing same address
print(id(arr4))
print(id(arr1))

arr4.append(3)
print(arr1)

arr1.pop()   #--------> O(1)
print(arr1)

n=arr1.pop(4)  #--------->O(n)
print(arr1)
print(n)

del arr1[6]  #---->O(n)

arr1.insert(4,4003)  #------>O(n)  returns none
print(arr1)

for i in arr1:     #--->O(n)
    print(i)

arr1[3:5] = [23,54]   #----->O(k+n)
print(arr1)

arr1.extend([34,21,65])   #----->O(k)
print(arr1)

print(min(arr1),"  ", max(arr1))  #------> O(n)

print(43 in arr1)    #--------> O(n)

arr1.sort()   #------>O(n logn)
print(arr1)

arr1.clear()
print(arr1)

del arr1
del arr2
del arr3
del arr4