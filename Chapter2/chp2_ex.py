a = input("문자열 입력> ")
b = input("문자열 입력> ")

print(a, b)

a1 = a  
b1 = b

b = a1
a = b1

# 더 간단한 방법 (튜플사용안하고)
# c = a
# a = b 
# b = c
 
print(a, b)