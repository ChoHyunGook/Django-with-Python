from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02BmiCalc, Quiz03Grade, Quiz04Circle, Quiz05Salary, Quiz07Dice, \
    Quiz08Generator, Quiz09RandomChoice, Quiz10Rps, Quiz11GetPrime, Quiz12LeapYear, Quiz13NumberGolf, Quiz14Lotto, \
    Quiz15Bank, Quiz16Gugudan

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기 2.BMI 계산기 3. 성적표 4.원넓이 계산기 5.월급(주급)계산기\n'
                     ' 6.오토 성적표 7.주사위 8.랜덤값 1개추출(정수) 9.랜덤 1명이름 추출 10.가위 바위 보\n '
                     '11. 소수 12.윤년 13. 숫자 스무고개 14.로또 15.은행 16.구구단')

        if menu == '0':
            break

        elif menu == '1':
            q1 = Quiz01Calculator()
            print(f'{q1.calc()}')
        elif menu == '2':
            member=Member()
            q2 = Quiz02BmiCalc()
            member.name=input('이름: ')
            member.inch=float(input('키: '))
            member.weight=float(input('몸무게: '))
            res=q2.bmicalc(member)
            print(f'이름:{member.name}\n {res} ')
        elif menu == '3':
            q3 = Quiz03Grade()
            print(f'{q3.myGrade()}')
        elif menu == '4':
            q4 = Quiz04Circle()
            print(f'{q4.circle()}')
        elif menu == '5':
            q5 = Quiz05Salary()
            print(f'{q5.salary()}')
        elif menu == '6':
            for i in ['김유신','강감찬','유관순','윤봉길','신사임당']:
                print(i)
        elif menu == '7':
            q7 = Quiz07Dice()
            print(f'{q7.dice()}')
        elif menu == '8':
            q8 = Quiz08Generator()
            print(f'{q8.generator()}')
        elif menu == '9':
            q9 = Quiz09RandomChoice()
            print(f'{q9.choice()}')
        elif menu == '10':
            q10 = Quiz10Rps()
            print(f'{q10.game()}')
        elif menu == '11':
            q11=Quiz11GetPrime()
            print(f'{q11.prime()}')
        elif menu == '12':
            q12 = Quiz12LeapYear()
            print(f'{q12.leap()}')
        elif menu == '13':
            q13 = Quiz13NumberGolf()
            print(f'{q13.game()}')
        elif menu == '14':
            q14 = Quiz14Lotto()
            print(f'{q14.lotto}')
        elif menu == '15':
            q15 = Quiz15Bank()
            print(f'{q15.bank()}')
        elif menu == '16':
            q16 = Quiz16Gugudan()
            print(f'{q16.gugudan()}')
        else:
            print('숫자 똑바로 적어라')