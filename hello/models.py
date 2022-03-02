class Calculator(object):

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
            elif op == '*':
                return self.mul()
            elif op == '/':
                return self.div()
            elif op == '%':
                return self.rest()
            else:
                return '똑바로 적어라'

class BmiCalc(object):

    def __init__(self, name, inch, weight):
        self.name = name
        self.inch = inch
        self.weight = weight

    def res (self):
        return weight/(inch * inch / 10000)

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


class Grade(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total (self):
        return self.kor + self.eng + self.math

    def avg (self):
        return self.total()/3

    def pas (self):
        if self.avg() >= 60:
            return '합격'
        else:
            return '불합격'


class Circle(object):

    def __init__(self, pi, half):
        self.pi=pi
        self.half=half

    def res (self):
        return self.pi*self.half*self.half

class Week(object):

    def __init__(self,name,time,money,day):
        self.name = name
        self.time = time
        self.money = money
        self.day = day

    def oneday (self):
        return self.time * self.money

    def salary (self):
        return self.oneday() * self.day



if __name__ == '__main__':

    while 1:
        menu = input('0.Exit 1.계산기 2.BMI 계산기 3. 성적표 4.원넓이 계산기 5.월급(주급)계산기')

        if menu == '0':
            break

        elif menu == '1':
            num1 = int(input('첫번째 숫자'))
            num2 = int(input('두번째 숫자'))
            op = input('연산자')
            # 객체생성
            calc = Calculator(num1, num2, op)
            print('*'*30)
            print(f'{calc.num1}{calc.op}{calc.num2}={calc.res()}')

        elif menu == '2':
            name = input('이름')
            inch = float(input('키'))
            weight = float(input('몸무게'))

            bmi = BmiCalc(name, inch, weight)

            print('*'*30)

            print(f'이름: {bmi.name}\n BMI지수: {bmi.res()}\n 결과: {bmi.result()}')

        elif menu == '3':
            name = input('이름')
            kor = int(input('국어점수'))
            eng = int(input('영어점수'))
            math = int(input('수학점수'))

            grade = Grade(name, kor, eng, math)


            print(f'########## 성적표 ########\n '
                  f'* 이름: {grade.name}\n  '
                  f'* > 국어: {grade.kor}점\n  '
                  f'* > 영어: {grade.eng}점\n" '
                  f'* > 수학: {grade.math}점\n '
                  f'* 총점: {grade.total()}점\n '
                  f'* 평균(정수): {grade.avg()}점\n'
                  f'합격여부: {grade.pas()}\n'
                  f'* #######################')

        elif menu == '4':
            pi = float(input('원주율'))
            half = float(input('반지름'))
            circle = Circle(pi, half)
            print(f'원주율:{circle.pi}\n 반지름:{circle.half}\n 원넓이:{circle.res()}')

        elif menu == '5':
            name = input('성함')
            time = int(input('일하는 시간'))
            day = int(input('일하는 날짜'))
            money = int(input('시급'))
            week = Week(name, time, day, money)
            print(f'{week.name}님의\n일급:{week.oneday()}\n 월급:{week.salary()}')

        else:
            print('숫자 똑바로 적어라')

