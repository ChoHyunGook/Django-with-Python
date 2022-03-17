from icecream import ic
from context.domains import Dataset
from context.models import Model

class TitanicModels(object):
    model=Model()
    ds=Dataset()
    def __init__(self,train_fname,test_fname):
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.train.head()}')
        # id 추출


    # hook

    def preprocess(self):
        df=self.train
        ic(df)
        df=self.drop_feature(df)
        df=self.create_train(df)
        df=self.create_label(df)
        df=self.name_nominal(df)
        df=self.sex_nominal(df)
        df=self.age_ratio(df)
        df=self.embarked_nominal(df)
        df=self.pclass_ordinal(df)
        df=self.fare_ratio(df)
        return df

    @staticmethod
    def create_label(df)->object:
        return df
    @staticmethod
    def create_train(df)->object:
        return df

# 결합도는 낮추고 응집도는 높일수록 이상적인 모듈화가 이루어진다
    def drop_feature(self,df)->object:
        for i in []:
            pass
        '''self.ticket_gar(df)
        self.cabin_gar(df)
        self.parch_gar(df)
        self.sibsp_gar(df)
        '''
        return df

    '''categori=>
        nominal(이름) vs ordinal(순서)
        quantitative=>(숫자)
        interval(상대) vs ratio(절대적인기준)'''

    @staticmethod
    def pclass_ordinal(df)->object:

        return df

    @staticmethod
    def name_nominal(df)->object:
        return df

    @staticmethod
    def sex_nominal(df)->object:
        return df

    @staticmethod
    def age_ratio(df)->object:
        return df

    @staticmethod
    def fare_ratio(df)->object:
        return df

    @staticmethod
    def embarked_nominal(df)->object:
        return df