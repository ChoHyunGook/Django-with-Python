from hello.domains import myRandom


class Quiz10:

    def quiz10bubble(self) -> str:
        arr = ten_nums()
        print(arr)
        for i in range(0, len(arr) - 1):
            for j in range(0, len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    tmp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = tmp
            print(f'{i}회차 배열 : {arr}')
        return None

    def quiz11insertion(self) -> str:
        arr = ten_nums()
        arr2 = []
        print(arr)
        for i in range(1, len(arr) - 1):
            for j in range(0, i):
                if arr[j] > arr[i]:
                    arr2[j] = arr[j]
                else:
                    for k in range(j, i):
                        arr

            print(f'{i}회차 배열 : {arr}')
        return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self) -> str:
        a = myRandom(2, 100)
        res = ''
        for i in range(2, a):
            num = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    num += 1
            if num == 1:
                res += str(i) + '\t'
        return print(res)

    def quiz18golf(self) -> str:
        st = myRandom(0, 100)
        count = 0
        while 1:
            se = int(input('숫자!'))
            if st == se:
                return print(f'정답{st}\n 틀린횟수:{count}')
            elif st > se:
                count += 1
                print('업')
            elif st < se:
                count += 1
                print('아래')


    def quiz19booking(self) -> str:return None