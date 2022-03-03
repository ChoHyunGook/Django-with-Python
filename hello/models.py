import random
from dataclasses import dataclass




class Quiz01Calculator(object):
    def calc(self):
        n1=int(input('첫번째 숫자'))
        n2=int(input('두번째 숫자'))
        op=input('연산자')
        if op == '+':
            res = n1+n2
        elif op == '-':
            res = n1-n2
        elif op == '*':
            res = n1*n2
        elif op == '/':
            res = n1/n2
        elif op == '%':
            res = n1%n2
        return res

class Quiz02BmiCalc(object):
    @staticmethod
    def bmicalc(member):
        this=member
        bmi=this.weight/( this.inch * this.inch /10000)
        if bmi <= 18.0:
            res= f'BMI 지수:{bmi}\n 결과: 저체중'
        elif bmi <= 22.9:
            res= f'BMI 지수:{bmi}\n 결과: 정상'
        elif bmi <= 23.0:
            res= f'BMI 지수:{bmi}\n 결과: 과체중'
        elif bmi <= 24.9:
            res= f'BMI 지수:{bmi}\n 결과: 위험체중'
        elif bmi <= 29.9:
            res= f'BMI 지수:{bmi}\n 결과: 1단계 비만'
        elif bmi <= 34.9:
            res= f'BMI 지수:{bmi}\n 결과: 2단계 비만'
        elif bmi < 35:
            res= f'BMI 지수:{bmi}\n 결과: 고도 비만'
        return res

class Quiz03Grade(object):
    def myGrade(self):
        name=input('이름')
        kor=int(input('국어점수'))
        eng=int(input('영어점수'))
        math=int(input('수학점수'))
        total=kor+eng+math
        avg=total/3
        if avg >= 90:
            grade= 'A'
        elif avg >= 80:
            grade= 'B'
        elif avg >= 70:
            grade= 'C'
        elif avg >= 65:
            grade= 'D'
        elif avg >= 60:
            grade= 'E'
        else:
            grade= 'F'
            if grade == 'F':
                grpass='불합격'
            else:
                grpass='합격'

        return print(f'########## 성적표 ########\n '
                  f'* 이름: {name}\n  '
                  f'* > 국어: {kor}점\n  '
                  f'* > 영어: {eng}점\n" '
                  f'* > 수학: {math}점\n '
                  f'* 총점: {total}점\n '
                  f'* 평균(정수): {avg}점\n'
                  f'* 학점: {grade}\n'
                  f'합격여부: {grpass}\n'
                  '* #######################')

class Quiz04Circle(object):
    def circle (self):
        pi=float(input('원주율'))
        half=float(input('반지름'))
        return f'원주율 : {pi}\n 반지름 : {half}\n 원넓이 : {pi*half*half}'

class Quiz05Salary(object):

    def salary(self):
        name=input('이름')
        time=int(input('일하는 시간'))
        day=int(input('일하는 날짜'))
        money=int(input('시급'))
        oneday=time*money
        salary=oneday*day

        return print(f'{name}님의\n 일급: {oneday}원\n 월급: {salary}\n')

class Quiz06GradeAuto(object):
    def myGrade(self):
        name=input('이름')
        kor=int(input('국어점수'))
        eng=int(input('영어점수'))
        math=int(input('수학점수'))
        total=kor+eng+math
        avg=total/3
        if avg >= 90:
            grade= 'A'
        elif avg >= 80:
            grade= 'B'
        elif avg >= 70:
            grade= 'C'
        elif avg >= 65:
            grade= 'D'
        elif avg >= 60:
            grade= 'E'
        else:
            grade= 'F'
            if grade == 'F':
                grpass='불합격'
            else:
                grpass='합격'

        return print(f'########## 성적표 ########\n '
                  f'* 이름: {name}\n  '
                  f'* > 국어: {kor}점\n  '
                  f'* > 영어: {eng}점\n" '
                  f'* > 수학: {math}점\n '
                  f'* 총점: {total}점\n '
                  f'* 평균(정수): {avg}점\n'
                  f'* 학점: {grade}\n'
                  f'합격여부: {grpass}\n'
                  '* #######################')

@staticmethod
def myRandom(start, end):
    return random.randint(start, end)

class Quiz07Dice(object):
    def dice(self):
        while 1:
            dice1 = myRandom(1, 6)
            dice2 = myRandom(1, 6)
            start=int(input('0. 종료 1. 스타트'))
            if start==0:
                return '종료'
            if start==1:
                if dice1 > dice2:
                    print(f'1번 주사위{dice1}\n 2번주사위:{dice2}\n 1번 주사위가 {dice1 - dice2}차이로 이겼다')
                elif dice1 < dice2:
                    print(f'1번 주사위: {dice1}\n 2번주사위: {dice2}\n2번 주사위가 {dice2-dice1}차이로 이겼다')
                else:
                    print('비겼다')

class Quiz08Generator(object):#원하는 범위의 정수에서 랜덤값 1개 추출
    def generator(self):
        min=int(input('최소값'))
        max=int(input('최대값'))
        return myRandom(min, max)

class Quiz09RandomChoice(object):#803호에서 랜덤으로 1명 이름 추출
    def __init__(self):
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        '권혜민', '서성민', '조현국', '김한슬', '김진영',
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        '강 민', '최건일', '유재혁', '김아름', '장원종']
    def choice(self):
        return self.members[myRandom(0, 23)]

class Quiz10Rps(object):
    def game(self):
        while 1:
            c = myRandom(0, 2)
            p = int(input('0.가위 1.바위 2.보 3.EXIT'))
            if p == 3:
                return 'EXIT'
            if c-p == 2 or c-p == -1:
                print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:WIN')
            elif c-p == 1 or c-p == -2:
                print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:LOSE')
            elif c-p == 0:
                print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:DRAW')


    '''
    <게이머 승리일때>
     컴퓨터0(가위) / 게이머1(바위)(win) = -1
     컴퓨터1(바위) / 게이머2(보)(win) = -1
     컴퓨터2(보) / 게이머0(가위)(win) = 2
    <컴퓨터 승리일때>
     컴퓨터0(가위) / 게이머2(보)(lose) = -2
     컴퓨터1(바위) / 게이머0(가위)(lose) = 1
     컴퓨터2(보) / 게이머1(바위)(lose) = 1 '''

class Quiz11GetPrime(object):
    def prime(self):
        a = int(input('최대값'))
        res=''
        for i in range(2, a):
            num = 0
            for j in range(2, i+1):
                if i % j == 0:
                    num += 1
            if num == 1:
                res +=  str(i) +'\t'
        return res

class Quiz12LeapYear(object):
    def leap(self):
        y=int(input('년도를 입력하세요'))
        if (y % 4 == 0 and not y % 100 == 0 or y % 400 == 0):
            res='윤년'
        else:
            res='평년'
        return res

class Quiz13NumberGolf(object):
    def __init__(self):
        self.static = myRandom(0, 100)

    def game(self):
        st = self.static
        count=0
        while 1:
            se = int(input('숫자!'))
            if st == se:
                return f'정답\n 틀린횟수:{count}'
            elif st > se:
                count += 1
                print('업')
            elif st < se:
                count += 1
                print('아래')

class Quiz14Lotto(object):
    def __init__(self):
        self.lotto = random.sample(range(1, 45), 6)
        self.lotto.sort()

class Quiz15Bank(object): # 이름, 입금, 출금만 구현
    def bank(self):
        total = 100000
        while 1:
            menu = int(input('사용하실 메뉴를 선택해 주세요\n'
                  '0.종료 1.잔액조회 2.현금인출 3.입금'))
            if menu == 0:
                return ('종료')
            if menu == 1:
                print(f'{total}')
            elif menu == 2:
                output = int(input('출금하실 금액'))
                if total >= output:
                    total = total-output
                    print(f'인출금액: {output}\n 잔액: {total}')
                elif total < output:
                    print('잔액이 부족합니다.')
            elif menu == 3:
                inp = int(input('입금하실 금액'))
                total = inp + total
                print(f'입금 금액:{inp} 잔액:{total}')

class Quiz16Gugudan(object): # 책받침구구단
    def gugudan(self):
        res = ""
        for i in [2, 6]:
            for j in range(1, 10):
                for k in range(0, 4):
                    res += f'{i + k} * {j} = {(i + k) * j}\t'
                res += '\n'
            res += '\n'
        return res


