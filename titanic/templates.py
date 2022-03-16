from context.domains import Dataset
from context.models import Model
from titanic import TitanicModels
from icecream import ic
import matplotlib.pyplot as plt #시각화
'''
데이터 시각화
엔터티(개체)를 차트로 표현하는것

모든 feature 를 다 그려야 하지만, 시간관계상
survived, pclass, sex, embarked 의 4개만 그리겠습니다.
템플릿 메소드 패턴으로 구성하시오.
'''

class TitanicTemplate(object):
    dataset = Dataset()
    model=Model()
    def __init__(self,fname):
        self.entity = self.model.new_model(fname)
        this=self.entity
        ic(f'트레인 타입: {type(this)}')
        ic(f'트레인 컬럼: {this.columns}')
        ic(f'트레인 상위5행: {this.head()}')
        ic(f'트레인 하위5행: {this.tail()}')

    def matplot_visualize(self)->None:
        this=self.entity
        self.draw_survived_dead(this)
        self.pclass(this)
        self.sex(this)
        self.embarked(this)
        plt.show(this)

    @staticmethod
    def draw_survived_dead(this)->None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived']
        plt.show(this)
    @staticmethod
    def pclass(this)->None:
        plt.show(this)
    @staticmethod
    def sex(this)->None:
        plt.show(this)
    @staticmethod
    def embarked(this)->None:
        plt.show(this)