import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen


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

    def quiz24zip(self) -> str:
        url='https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')
        # print(soup.prettify())
        artists=soup.find_all('p', {'class':"artist"})
        artists=[i.get_text() for i in artists]
        print(''.join(i for i in artists))
        return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers={'User-Agent':'Mozilla/5.0'}
        url='https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req=urllib.request.Request(url,headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        play_songs=soup.find_all('div', {'class':'ellipsis rank01'})
        play_songs=[i.get_text() for i in play_songs]
        print(''.join(i for i in play_songs))
        return None


        return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None