import urllib.request
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


class Quiz20:

    def quiz20list(self) -> str: return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('-----------legacy------------')
        a =[]
        for i in range(5):
            a.append(i)
        print(a)
        print('-----------comprehension------------')
        a2=[i for i in range(5)]
        print(a2)
        return None

    @staticmethod
    def quiz24zip() -> {}:
        dict = {}
        soup = BeautifulSoup(urlopen('https://music.bugs.co.kr/chart/track/realtime/total'), 'lxml')
        cls_names=['artist', 'title']
        # print(''.join(i for i in Quiz20.soup_(soup, 'p', 'class', [i for i in cls_names])))
        a=[i for i in cls_names]
        ls1 = Quiz20.soup_(soup, 'p', 'class', 'title')
        ls2 = Quiz20.soup_(soup, 'p', 'class', 'artist')
        #Quiz20.dict1(dict, ls1, ls2)
        #Quiz20.dict2(dict,ls1,ls2)
        for i, j in zip(ls1,ls2):
            dict[i]=j
        pprint(dict)
        return dict

        #url='https://music.bugs.co.kr/chart/track/realtime/total'
        #html_doc = urlopen(url)
        #soup = BeautifulSoup(html_doc, 'lxml')
        # print(soup.prettify())
        #titles=soup.find_all('p',{'class':"title"})
        #titles = [i.get_text() for i in titles]
        #print(''.join(i for i in artists))

    @staticmethod
    def quiz27melon() -> {}:
        dict = {}
        soup = BeautifulSoup(urlopen(urllib.request.Request('https://www.melon.com/chart/index.htm?dayTime=2022031017',
                                                            headers={'User-Agent': 'Mozilla/5.0'})).read(), 'lxml')
        ls1 = Quiz20.soup_(soup, 'div', 'class', 'ellipsis rank01')
        ls2 = Quiz20.soup_(soup, 'span', 'class', 'checkEllipsis')
        for i, j in zip(ls1, ls2):
            dict[i] = j
        pprint(dict)
        return dict


    @staticmethod
    def dict1(dict,ls1,ls2)->{}:
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        pprint(dict)

    @staticmethod
    def dict2(dict,ls1,ls2)->{}:
        for i,j in enumerate(ls1):
            dict[j] = ls2[i]
        pprint(dict)


    @staticmethod
    def rank(soup)-> None:
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(Quiz20.soup_(soup, 'p', 'class', j)):
                print(f'{i}위 : {j}')
            print('#' * 100)


    @staticmethod
    def soup_(soup, point,deep_point,name)->[]:
         return [i.get_text().strip() for i in soup.find_all(point,{deep_point:name})]




    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None




    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df =pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

    def quiz29(self) -> str: return None

