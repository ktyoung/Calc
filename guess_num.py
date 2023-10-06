import random

print()
print("="*33)
print("숫자 게임에 오신 것을 환영합니다.")
print("="*33)

while True:
    min_lev=1
    max_lev=6
    
    if(min_lev < max_lev):
        for a in range(min_lev,max_lev):
            min_num=1
            max_num=100*a
            print(a,"단계 범위:",min_num,"~",max_num)
        print()

        level = int(input("난이도를 선택하세요: "))

        if level < min_lev or level > max_lev-1:
            print("* "*19)
            print(min_lev,"과",max_lev-1,"사이의 값을 입력하세요")
            print("입력 오류: 처음부터 다시 설정합니다.")
            print("* "*19)

        else:
            print("-"*33)
            print(level,"단계를 선택하셨습니다.")
            print("-"*33)

            min_life=1
            max_life=99

            print("="*33)
            print("최소:",min_life,"번","\t최대:",max_life,"번")
            life=int(input("몇 번의 기회를 가지시겠습니까? ")); print("="*33)

            if life < min_life or life > max_life:
                print("* "*19)
                print(min_life,"과",max_life,"사이의 값을 입력하세요")
                print("입력 오류: 처음부터 다시 설정합니다.")
                print("* "*19)

            else:
                print("-"*33)
                print("당신은",life,"번의 기회를 가집니다.")
                print("-"*33)
                
                print("="*31)
                print("난이도:",level,"\t","기회:",life)
                print("위 설정으로 게임을 시작합니다.")
                print("="*31)

                number=random.randint(min_num,100*level)

                MIN=min_num
                MAX=100*level
                print(level,"단계 범위:", MIN,"~",MAX,"\n")

                tries=0
                
                while True:
                    guess = int(input("범위 내 숫자를 입력하세요: "))

                    if number == guess:
                        print("★ "*10)
                        print("정답입니다!")
                        print("시도 횟수:",tries,"회")
                        print("★ "*10)
                        print("축하합니다! 게임을 종료합니다.")
                        break

                    elif guess < MIN or guess > MAX:
                        print("* "*16)
                        print("알맞은 범위의 수를 입력하세요.")
                        print("(",level,"단계 범위:", MIN,"~",MAX,")")
                        print("* "*16)

                    else:
                        print("-"*33)
                        print("오답입니다.")
                        tries=tries+1
                        life=life-1
                        if number > guess:
                            print(guess,"보다 큽니다.")
                            print("남은 기회:",life,"회")
                            print("-"*33)
                        else:
                            print(guess,"보다 작습니다.")
                            print("남은 기회:",life,"회")
                            print("-"*33)
                        if life == 0:
                            print("남은 기회가 없습니다.")
                            print("정답은",number,"입니다. 다시 시도해보세요.")
                            break
                break
    else:
        print("초기값 설정이 잘못됐습니다.")
        break
