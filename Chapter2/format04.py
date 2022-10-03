# 조합하기
o_h = "{:+5d}".format(52)     # 기호를 뒤로 밀기: 양수
o_i = "{:+5d}".format(-52)    # 기호를 뒤로 밀기: 음수
o_j = "{:=+5d}".format(52)    # 기호를 앞으로 밀기: 양수
o_k = "{:=+5d}".format(-52)   # 기호를 앞으로 밀기: 음수
o_l = "{:+05d}".format(52)    # 0으로 채우기: 양수
o_m = "{:+05d}".format(-52)   # 0으로 채우기: 음수


print("# 조합하기")
print(o_h)  
print(o_i)
print(o_j)
print(o_k)
print(o_l)
print(o_m)
