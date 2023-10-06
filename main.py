def print_line():
    print("="*55)

def print_error():
    print()
    print("* "*22)
    print("입력 오류입니다. 초기 화면으로 돌아갑니다.")
    print("* "*22)
    print()

def boot_screen():
    print_line()
    print("\t\t 계산기를 실행합니다.")
    print("1. 기본 연산\t2. 특수 연산\t3. 단위 변환\t0. 종료")
    print_line()

def off_calc():
    print_line()
    print("\t\t  계산기를 종료합니다.")
    print_line()
    exit()

def return_calc():
    print_line()
    print("\t\t초기화면으로 돌아갑니다.")
    print_line()
    return 0

def check_function(CALC_FUNC):
    if CALC_FUNC < 0 or CALC_FUNC > 3:
        print_error()
        print("오류: 잘못된 번호가 입력되었습니다.\n")

def check_basic_calc(CALC_NUM):
    if CALC_NUM == 9:
        return_calc()
    elif CALC_NUM == 0:
        off_calc()
    elif CALC_NUM < 0 or CALC_NUM > 5:
        print_error()
        print("오류: 잘못된 번호가 입력되었습니다.\n")

def check_special_calc(CALC_NUM):
    if CALC_NUM == 9:
        return_calc()
    elif CALC_NUM == 0:
        off_calc()
    elif CALC_NUM < 0 or CALC_NUM > 3:
        print_error()
        print("오류: 잘못된 번호가 입력되었습니다.\n")

def check_unit_convert(CALC_NUM):
    if CALC_NUM == 9:
        return_calc()
    elif CALC_NUM == 0:
        off_calc()
    elif CALC_NUM < 0 or CALC_NUM > 9:
        print_error()
        print("오류: 잘못된 번호가 입력되었습니다.\n")

def check_calc_percent(CALC_NUM):
    if CALC_NUM == 9:
        return_calc()
    elif CALC_NUM == 0:
        off_calc()
    elif CALC_NUM < 0 or CALC_NUM > 4:
        print_error()
        print("오류: 잘못된 번호가 입력되었습니다.\n")

def sum(CALC_NUM):
    if CALC_NUM == 1:
        print("덧셈: 입력한 수들의 총합을 구합니다.")
        sum=0
        while True:
            var=int(input("더할 수를 입력하세요(0 입력 시 결과 표시): "))
            sum+=var
            if var == 0:
                print_line()
                print("입력한 수의 총합은",sum,"입니다.")
                print_line()
                break
                
def sub(CALC_NUM):
    if CALC_NUM == 2:
        print("뺄셈: 입력한 수의 차를 구합니다.")
        var1=int(input("첫 번째 수를 입력하세요: "))
        while True:
            var2=int(input("뺄 수를 입력하세요(0 입력 시 결과 표시): "))
            var1-=var2
            if var2 == 0:
                print_line()
                print("입력한 수의 차는",var1,"입니다.")
                print_line()
                break

def mul(CALC_NUM):
    if CALC_NUM == 3:
        print("곱셈: 입력한 수의 곱을 구합니다.")
        mul=1
        while True:
            var=int(input("곱할 수를 입력하세요(0 입력 시 결과 표시): "))
            if var > 0:
                mul=mul*var
            else:
                print_line()
                print("입력한 수의 곱은",mul,"입니다.")
                print_line()
                break

def div(CALC_NUM):
    if CALC_NUM == 4:
        print("나눗셈: 입력한 두 수를 나눕니다.")
        div_res=0
        div_quo=0
        div_rem=0

        var1=int(input("나눌 숫자를 입력하세요: "))
        var2=int(input("어떤 수로 나눕니까? "))
            
        if var2 > 0:
            div_res=var1/var2
            div_quo=var1//var2
            div_rem=var1%var2
            print_line()
            print("결과는",div_res,"입니다.")
            print("몫은",div_quo,"이고,","나머지는",div_rem,"입니다.")
            print_line()
        elif var2 == 0:
            print_error()
            print("오류: 0으로 나눌 수 없습니다.\n")

def pow(CALC_NUM):
    if CALC_NUM == 5:
        res=1
        print("거듭제곱: 첫 번째 수를 두 번째 수만큼 곱합니다.")
        var1=int(input("첫 번째 수를 입력하세요: "))
        var2=int(input("두 번째 수를 입력하세요: "))
        res=var1**var2
        print_line()
        print(var1,"의",var2,"제곱은",res,"입니다.")
        print_line()

def per_1(S_PER_CALC_NUM):
    if S_PER_CALC_NUM == 1:
        print("비율값: 전체 값의 일부 % 값을 계산합니다.")
        var1=int(input("전체 값을 입력하세요: "))
        var2=int(input("비율(%)를 입력하세요: "))
        res=var1*(var2/100)
        print_line()
        print(var1,"의",var2,"%는",res,"입니다.")
        print_line()

def per_2(S_PER_CALC_NUM):
    if S_PER_CALC_NUM == 2:
        print("일부값: 전체 값에서 일부 값은 몇%인지 계산합니다.")
        var1=int(input("전체 값을 입력하세요: "))
        var2=int(input("일부 값을 입력하세요: "))
        res=(var2/var1)*100
        print_line()
        print(var1,"의",var2,"은",res,"% 입니다.")
        print_line()

def per_3(S_PER_CALC_NUM):
    if S_PER_CALC_NUM == 3:
        print("증감값: 전체 값이 증감 값으로 변했을 때 몇% 증감한 것인지 계산합니다.")
        var1=int(input("전체 값을 입력하세요: "))
        var2=int(input("증감 값을 입력하세요: "))
        res=((var2-var1)/var1)*100

        if res > 100:
            print_line()
            print(var1,"이",var2,"로 변하면",res,"%만큼 증가합니다.")
            print_line()
        elif res < 100:
            print_line()
            print(var1,"이",var2,"로 변하면",res,"%만큼 감소합니다.")
            print_line()

def per_4(S_PER_CALC_NUM):
    if S_PER_CALC_NUM == 4:
        print("증가율: 전체 값이 일부 %만큼 증가했을 때의 값을 계산합니다.")
        var1=int(input("전체 값을 입력하세요: "))
        var2=int(input("증가율(%)를 입력하세요: "))
        res=var1*(1+(var2/100))
        print_line()
        print(var1,"이",var2,"%만큼 증가한 값은",res,"입니다.")
        print_line()

def calc_percent(S_CALC_NUM):
    if S_CALC_NUM == 1:
        print("\t     퍼센트 계산을 선택하셨습니다.")
        print_line()
        print("1. 비율값\t2. 일부값\t3. 증감값\t4. 증감율")
        print("9. 초기 화면으로\t\t\t\t0. 종료")
        print_line()
        S_PER_CALC_NUM=int(input("연산 기능을 선택하세요(번호로 입력): "))
        print_line()
        check_calc_percent(S_PER_CALC_NUM)

        per_1(S_PER_CALC_NUM)
        per_2(S_PER_CALC_NUM)
        per_3(S_PER_CALC_NUM)
        per_4(S_PER_CALC_NUM)

def calc_bmi(S_CALC_NUM):
    if S_CALC_NUM == 2:
        print("\t   비만도(BMI) 계산을 선택하셨습니다.")
        print_line()
        weight=float(input("몸무게를 입력하세요(kg): "))
        tall=float(input("키를 입력하세요(m): "))
        bmi=weight/(tall*tall)
        print_line()
        print("비만도(BMI)는",bmi,"입니다.")

        if bmi < 18.5:
            print("저체중입니다.") 
            print_line()
        elif bmi >= 18.5 and bmi <= 22.9:
            print("정상입니다.") 
            print_line()
        elif bmi >= 23 and bmi <= 24.9:
            print("비만 전 단계(과체중)입니다.") 
            print_line()
        elif bmi >= 25 and bmi <= 29.9:
            print("1단계 비만입니다.") 
            print_line()
        elif bmi >= 30 and bmi <= 34.9:
            print("2단계 비만입니다.") 
            print_line()
        elif bmi >= 35:
            print("3단계 비만(고도 비만)입니다.") 
            print_line()

def calc_leap_year(S_CALC_NUM):
    if S_CALC_NUM == 3:
        print("\t      윤년 계산을 선택하셨습니다.")
        print_line()
        year=int(input("연도를 입력하세요: "))
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            print_line()
            print("\t\t",year,"년은 윤년입니다.")
            print_line()
        else:
            print_line()
            print("\t     ",year,"년은 윤년이 아닙니다.")
            print_line()

def in_to_cm(U_CALC_NUM):
    if U_CALC_NUM == 1:
        print("센티미터(cm)를 인치(inch)로 변환합니다.")
        var_cm=float(input("센티미터(cm) 값을 입력하세요: "))
        var_in=var_cm/2.54
        print_line()
        print(var_cm,"센티미터(cm)는", var_in,"인치(inch)입니다.")
        print_line()

def cc_to_li(U_CALC_NUM):
    if U_CALC_NUM == 2:
        print("cc를 리터(L)로 변환합니다.")
        var_cc=float(input("cc 값을 입력하세요: "))
        var_li=var_cc/1000
        print_line()
        print(var_cc,"cc는", var_li,"리터(L)입니다.")
        print_line()

def pl_to_m2(U_CALC_NUM):
    if U_CALC_NUM == 3:
        print("평수를 제곱미터(m²)로 변환합니다.")
        var_pl=float(input("평수를 입력하세요: "))
        var_m2=var_pl*3.305785
        print_line()
        print(var_pl,"평은", var_m2,"제곱미터(m²)입니다.")
        print_line()

def C_to_F(U_CALC_NUM):
    if U_CALC_NUM == 4:
        print("섭씨(℃ )를 화씨(℉ )로 변환합니다.")
        var_C=float(input("섭씨(℃ )를 입력하세요: "))
        var_F=(var_C*1.8)+32
        print_line()
        print(var_C,"℃ 는", var_F,"℉ 입니다.") 
        print_line()       

def cm_to_in(U_CALC_NUM):
    if U_CALC_NUM == 5:
        print("인치(inch)를 센티미터(cm)로 변환합니다.")
        var_in=float(input("인치(inch) 값을 입력하세요: "))
        var_cm=var_in*2.54
        print_line()
        print(var_in,"인치(inch)는", var_cm,"센티미터(cm)입니다.")
        print_line()

def li_to_cc(U_CALC_NUM):
    if U_CALC_NUM == 6:
        print("리터(L)를 cc로 변환합니다.")
        var_li=float(input("리터(L) 값을 입력하세요: "))
        var_cc=var_li*1000
        print_line()
        print(var_li,"리터(L)는", var_cc,"cc입니다.")
        print_line()

def m2_to_pl(U_CALC_NUM):
    if U_CALC_NUM == 7:
        print("제곱미터(m²)를 평수로 변환합니다.")
        var_m2=float(input("제곱미터(m²)를 입력하세요: "))
        var_pl=var_m2/3.305785
        print_line()
        print(var_m2,"제곱미터(m²)는", var_pl,"평입니다.")
        print_line()

def F_to_C(U_CALC_NUM):
    if U_CALC_NUM == 8:
        print("화씨(℉ )를 섭씨(℃ )로 변환합니다.")
        var_F=float(input("화씨(℉ )를 입력하세요: "))
        var_C=(var_F-32)/1.8
        print_line()
        print(var_F,"℉ 는", var_C,"℃ 입니다.")
        print_line()

def basic_calc(CALC_FUNC):
    if CALC_FUNC == 1:
        print("\t      기본 연산을 선택하셨습니다.")
        print_line()
        print("1. 덧셈   2. 뺄셈   3. 곱셈   4. 나눗셈   5. 거듭제곱")
        print("9. 초기 화면으로\t\t\t  0. 종료")
        print_line()
        CALC_NUM=int(input("연산 기능을 선택하세요(번호로 입력): "))
        print_line()
        check_basic_calc(CALC_NUM)

        sum(CALC_NUM)
        sub(CALC_NUM)
        mul(CALC_NUM)
        div(CALC_NUM)
        pow(CALC_NUM)

def special_calc(CALC_FUNC):
    if CALC_FUNC == 2:
        print("\t      특수 연산을 선택하셨습니다.")
        print_line()
        print("1. 퍼센트(%) 계산   2. 비만도(BMI) 계산   3. 윤년 계산")
        print("9. 초기 화면으로\t\t\t  0. 종료")
        print_line()
        S_CALC_NUM=int(input("연산 기능을 선택하세요(번호로 입력): "))
        print_line()
        check_special_calc(S_CALC_NUM)

        calc_percent(S_CALC_NUM)
        calc_bmi(S_CALC_NUM)
        calc_leap_year(S_CALC_NUM)

def unit_convert(CALC_FUNC):
    if CALC_FUNC == 3:
        print("\t      단위 변환을 선택하셨습니다.")
        print_line()
        print("1. 센티미터(cm)→인치(inch)\t2. cc→리터(L)\t3. 평→제곱미터(m²)\t4. 섭씨(℃ )→화씨(℉ )")
        print("5. 인치(inch)→센티미터(cm)\t6. 리터(L)→cc\t7. 제곱미터(m²)→평\t8. 화씨(℉ )→섭씨(℃ )")
        print("9. 초기 화면으로\t\t0. 종료")
        print_line()
        U_CALC_NUM=int(input("변환할 단위를 선택하세요(번호로 입력): "))
        print_line()
        check_unit_convert(U_CALC_NUM)

        in_to_cm(U_CALC_NUM)
        cc_to_li(U_CALC_NUM)
        pl_to_m2(U_CALC_NUM)
        C_to_F(U_CALC_NUM)
        cm_to_in(U_CALC_NUM)
        li_to_cc(U_CALC_NUM)
        m2_to_pl(U_CALC_NUM)
        F_to_C(U_CALC_NUM)

def main():
    while True:
        boot_screen()
        CALC_FUNC=int(input("연산 기능을 선택하세요(번호로 입력): "))
        print_line()
        check_function(CALC_FUNC)

        if CALC_FUNC == 0:
            off_calc()

        basic_calc(CALC_FUNC)
        special_calc(CALC_FUNC)
        unit_convert(CALC_FUNC)

main()