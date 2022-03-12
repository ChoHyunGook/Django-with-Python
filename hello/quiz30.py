import pandas as pd
from icecream import ic

from hello import Quiz20
from hello.domains import myRandom
import random
import string

class Quiz30:
    '''
            데이터프레임 문제 Q02
        ic| df:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4  10  11  12
        '''

    def quiz30_df_4_by_3(self) -> None:

        columns = Quiz20.askicode(65,68)
        d1 = [i for i in range(1, 13)]
        d2=[d1[i:i + 3] for i in range(0, len(d1), 3)]
        Quiz30.random_cutter(i,(1,13),3)


        df = pd.DataFrame(d2, index=range(1, 5), columns=columns)
        # 위 식을 리스트결합 형태로 분해해서 조립하시오

        ic(df)
        return None
#http://pertinency.blogspot.com/2019/10/blog-post_7.html
    '''
            데이터프레임 문제 Q03.
            두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
            ic| df:     0   1   2
                    0  97  57  52
                    1  56  83  80
    '''
    def quiz31_rand_2_by_3(self) -> str:
        data=Quiz30.random_cutter(myRandom(10,100),6,3)
        df = pd.DataFrame(data, index=range(0, 2), columns=range(0,3))

        ic(df)
        return None

    '''
                데이터프레임 문제 Q04.
                국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
                 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

                  ic| df4:        국어  영어  수학  사회
                            lDZid  57  90  55  24
                            Rnvtg  12  66  43  11
                            ljfJt  80  33  89  10
                            ZJaje  31  28  37  34
                            OnhcI  15  28  89  19
                            claDN  69  41  66  74
                            LYawb  65  16  13  20
                            QDBCw  44  32   8  29
                            PZOTP  94  78  79  96
                            GOJKU  62  17  75  49
        '''

    def quiz32_df_grade(self) -> str:
        data=Quiz30.cutter(myRandom(0,101),40,4)
        columns=['국어','영어','수학','사회']
        ls=[]
        for i in range(10):
            name=""
            for j in range(5):
                name += (str(random.choice(string.ascii_uppercase)))
            ls.append(name)
        df = pd.DataFrame(data, index=ls, columns=columns)
        ic(df)
        return None

    def quiz33(self) -> str: return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None

    @staticmethod
    def random_cutter(start,point,cutter):
        d = [start for i in range(point)]
        d1 = [d[i:i + cutter] for i in range(0, len(d), cutter)]
        return d1

