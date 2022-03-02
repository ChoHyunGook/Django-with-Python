import random

def main():
    while 1:
        menu = input('0.Exit 1.계산기 2.BMI 계산기 3. 성적표 4.원넓이 계산기 5.월급(주급)계산기\n'
                     ' 6.오토 성적표 7.주사위 8.랜덤값 1개추출(정수) 9.랜덤 1명이름 추출 10.가위 바위 보\n '
                     '11. 소수 12.윤년 13. 숫자 스무고개 14.로또 15.은행 16.구구단')

        if menu == '0':
            break

        elif menu == '1':
            calc = Quiz01Calculator(int(input('첫번째 숫자')), int(input('두번째 숫자')), input('연산자'))
            print('*'*30)
            print(f'{calc.num1}{calc.op}{calc.num2}={calc.res()}')

        elif menu == '2':
            bmi = Quiz02BmiCalc(input('이름'), float(input('키')), float(input('몸무게')))
            print('*'*30)
            print(f'이름: {bmi.name}\n BMI지수: {bmi.res()}\n 결과: {bmi.result()}')

        elif menu == '3':
            grade = Quiz03Grade(input('이름'), int(input('국어점수')), int(input('영어점수')), int(input('수학점수')))

            print(f'########## 성적표 ########\n '
                  f'* 이름: {grade.name}\n  '
                  f'* > 국어: {grade.kor}점\n  '
                  f'* > 영어: {grade.eng}점\n" '
                  f'* > 수학: {grade.math}점\n '
                  f'* 총점: {grade.total()}점\n '
                  f'* 평균(정수): {grade.avg()}점\n'
                  f'* 학점: {grade.getGrade()}\n'
                  f'합격여부: {grade.gradePass()}\n'
                  '* #######################')

        elif menu == '4':
            circle = Quiz04Circle(float(input('원주율')), float(input('반지름')))
            print(f'원주율:{circle.pi}\n 반지름:{circle.half}\n 원넓이:{circle.res()}')

        elif menu == '5':
            week = Quiz05Week(input('성함'), int(input('일하는 시간')), int(input('일하는 날짜')), int(input('시급')))
            print(f'{week.name}님의\n일급:{week.oneday()}\n 월급:{week.salary()}')

        elif menu == '6':
            for i in ['김유신','강감찬','유관순','윤봉길','신사임당']:
                print(i)

        elif menu == '7':
            dice = Quiz07Dice()
            print(f'주사위 1 :{dice.dice01}\n '
                  f'주사위 2 :{dice.dice02}\n'
                  f' {dice.vs()}')

        elif menu == '8':
            q8 = Quiz08Generator(int(input('최소값')), int(input('최대값')))
            print(f'{q8.essence}')

        elif menu == '9':
            q9 = Quiz09RandomChoice()
            print(f'{q9.choice()}')

        elif menu == '10':
            q10 = Quiz10Rps(int(input('0.가위 1.바위 2.보')))
            print(f'사용자: {q10.player}\n 컴퓨터: {q10.com}\n 결과: {q10.game()}')
        elif menu == '11':
            print()
        elif menu == '12':
            print()
        elif menu == '13':
            print()
        elif menu == '14':
            print()
        elif menu == '15':
            print()
        elif menu == '16':
            print()

        else:
            print('숫자 똑바로 적어라')



class Quiz01Calculator(object):

    def __init__(self, num1, num2, op):
        self.num1= num1
        self.num2 = num2
        self.op = op

    def add (self):
        return self.num1 + self.num2

    def min (self):
        return self.num1 - self.num2

    def mul (self):
        return self.num1 * self.num2

    def div (self):
        return self.num1 / self.num2

    def rest (self):
        return self.num1 % self.num2

    def res(self):
            if self.op == '+':
                return self.add()
            elif self.op == '-':
                return self.min()
            elif self.op == '*':
                return self.mul()
            elif self.op == '/':
                return self.div()
            elif self.op == '%':
                return self.rest()
            else:
                return '똑바로 적어라'

class Quiz02BmiCalc(object):

    def __init__(self, name, inch, weight):
        self.name = name
        self.inch = inch
        self.weight = weight

    def res (self):
        return self.weight/(self.inch * self.inch / 10000)

    def result(self):
        if self.res() <= 18.0:
            return '저체중'
        elif self.res() <= 22.9:
            return '정상'
        elif self.res() <= 23.0:
            return '과체중'
        elif self.res() <= 24.9:
            return '위험 체중'
        elif self.res() <= 29.9:
            return '1단계 비만'
        elif self.res() <= 34.9:
            return '2단계 비만'
        elif self.res() < 35:
            return '고도 비만'
        else:
            return '똑바로 적어라'


class Quiz03Grade(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total (self):
        return self.kor + self.eng + self.math

    def avg (self):
        return self.total()/3

    def getGrade(self):
        if self.avg() >= 90:
            return 'A'
        elif self.avg() >= 80:
            return 'B'
        elif self.avg() >= 70:
            return 'C'
        elif self.avg() >= 65:
            return 'D'
        elif self.avg() >= 60:
            return 'E'
        else:
            return 'F'

    def gradePass(self):
        if self.getGrade() == 'F':
            return '불합격'
        else:
            return '합격'


class Quiz04Circle(object):

    def __init__(self, pi, half):
        self.pi=pi
        self.half=half

    def res (self):
        return self.pi*self.half*self.half

class Quiz05Week(object):

    def __init__(self,name,time,money,day):
        self.name = name
        self.time = time
        self.money = money
        self.day = day

    def oneday (self):
        return self.time * self.money

    def salary (self):
        return self.oneday() * self.day

class Quiz06GradeAuto(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total (self):
        return self.kor + self.eng + self.math

    def avg (self):
        return self.total()/3

    def getGrade(self):
        if self.avg()>=90:
            return 'A'
        elif self.avg()>=80:
            return 'B'
        elif self.avg()>=70:
            return 'C'
        elif self.avg()>=65:
            return 'D'
        elif self.avg()>=60:
            return 'E'
        else:
            return 'F'

    def gradePass(self):
        if self.getGrade() == 'F':
            return '불합격'
        else:
            return '합격'

@staticmethod
def myRandom(start, end):
    return random.randint(start, end)

class Quiz07Dice(object):
    def __init__(self):
        self.dice01 = myRandom(1, 6)
        self.dice02 = myRandom(1, 6)

    def vs(self):
        if self.dice01 > self.dice02:
            return f'1번 주사위가 {self.dice01 - self.dice02}차이로 이겼다'
        elif self.dice01 < self.dice02:
            return f'2번 주사위가 {self.dice02-self.dice01}차이로 이겼다'
        else:
            return '비겼다'


class Quiz08Generator(object):#원하는 범위의 정수에서 랜덤값 1개 추출
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.essence = myRandom(self.min, self.max)


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
    def __init__(self,player):
        self.player = player
        self.com = myRandom(0, 2)

    def game(self):
        c = self.com
        p = self.player
        if c-p == 2 or -1:
            res = 'WIN'
        elif c-p == 1 or -2:
            res = 'LOSE'
        elif c-p == 0:
            res = 'DRAW'
        return res

    ''' 컴퓨터0(가위) / 게이머1(바위)(win) = -1
     컴퓨터1(바위) / 게이머2(보)(win) = -1
     컴퓨터2(보) / 게이머0(가위)(win) = 2

     컴퓨터0(가위) / 게이머2(보)(lose) = -2
     컴퓨터1(바위) / 게이머0(가위)(lose) = 1
    컴퓨터2(보) / 게이머1(바위) = 1 '''

class Quiz11GetPrime(object):
    def __init__(self):
        pass
class Quiz12LeapYear(object):
    def __init__(self):
        pass
class Quiz13NumberGolf(object):
    def __init__(self):
        pass
class Quiz14Lotto(object):
    def __init__(self):
        pass
class Quiz15Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass
class Quiz16Gugudan(object): # 책받침구구단
    def __init__(self):
        pass


if __name__ == '__main__':
    main()