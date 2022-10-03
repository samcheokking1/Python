
# 정수 
o_a = "{:d}".format(52)

# 특정 칸에 출력하기
o_b = "{:5d}".format(52)    #5칸
o_c = "{:10d}".format(52)   #10칸

# 빈칸을 0으로 채우기
o_d = "{:05d}".format(52)   #양수 
o_e = "{:05d}".format(-52)  #음수 

print("# 기본")
print(o_a)

print("# 특정 칸에 출력하기")
print(o_b)
print(o_c)

print("# 빈칸을 0으로 채우기")
print(o_d)
print(o_e)
