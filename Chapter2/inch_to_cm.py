# 숫자를 입력받습니다.
i_inch = input("inch 단위의 숫자를 입력해주세요: ")

# 입력받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다.
i_cm = float(i_inch) * 2.54

# 출력합니다.
print(i_inch, "inch는 cm 단위로 ",i_cm, "cm 입니다.")