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

class BmiCalc(object):

    def __init__(self, inch, weight, name):
        self.name = name
        self.inch = inch
        self.weight = weight


class Grade(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


if __name__ == '__main__':

    while 1:
        menu = input('0.Exit 1.계산기 2.BMI 계산기 3. 성적표')

        if menu == '0':
            break

        elif menu == '1':
            num1 = int(input('첫번째 숫자'))
            num2 = int(input('두번째 숫자'))
            op = str(input('연산자'))
            # 객체생성
            calc = Calculator(num1, num2, op)

            print('*'*30)

            if op == '+':
                res =calc.add()
            elif op == '-':
                res =calc.min()
            elif op == '*':
                res =calc.mul()
            elif op == '/':
                res =calc.div()
            elif op == '%':
                res =calc.rest()

            print(f'{calc.num1}{calc.op}{calc.num2}={res}')

        elif menu == '2':
            name = str(input('이름'))
            inch = float(input('키'))
            weight = float(input('몸무게'))

            bmi = BmiCalc(inch, weight, name)

            res = (inch * inch) / weight * 10000

            print('*'*30)

            if res <= 18.0:
                result = '저체중'
            elif res <= 22.9:
                result = '정상'
            elif res <= 23.0:
                result = '과체중'
            elif res <= 24.9:
                result = '위험 체중'
            elif res <= 29.9:
                result = '1단계 비만'
            elif res <= 34.9:
                result = '2단계 비만'
            else:
                result = '고도 비만'
            print(f'이름: {name}\n BMI지수: {res}\n 결과: {result}')

        elif menu == '3':
            name = str(input('이름'))
            kor = int(input('국어점수'))
            eng = int(input('영어점수'))
            math = int(input('수학점수'))
            total = kor+eng+math
            avg = total/3
            if avg >= 60:
                pas = '합격'
            else:
                pas = '불합격'

            print(f'########## 성적표 ########\n '
                  f'* 이름: {name}\n  '
                  f'* > 국어: {kor}점\n  '
                  f'* > 영어: {eng}점\n" '
                  f'* > 수학: {math}점\n '
                  f'* 총점: {total}점\n '
                  f'* 평균(정수): {avg}점\n'
                  f'합격여부: {pas}\n'
                  f'* #######################')

        else:
            print('숫자 똑바로 적어라')

