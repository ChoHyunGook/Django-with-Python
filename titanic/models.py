from icecream import ic
from context.domains import Dataset
from context.models import Model

class TitanicModels(object):
    def __init__(self,train_fname,test_fname):
        self.model = Model()
        self.ds = Dataset()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.test.head()}')
        ic(self.train)



    def preprocess(self):
        self.sibsp_gar()
        self.parch_gar()
        self.ticket_gar()
        self.cabin_gar()
        self.create_train()
        self.create_label()
        self.name_nominal()
        self.sex_nominal()
        self.age_ratio()
        self.embarked_nominal()
        self.pclass_ordinal()
        self.fare_ratio()




    def create_label(self)->object:
        pass

    def create_train(self)->object:
        pass

    def drop_feature(self)->object:
        pass

    '''categori=>
        nominal(이름) vs ordinal(순서)
        quantitative=>(숫자)
        interval(상대) vs ratio(절대적인기준)'''

    def pclass_ordinal(self)->object:
        pass

    def name_nominal(self)->object:
        pass

    def sex_nominal(self)->object:
        pass

    def age_ratio(self)->object:
        pass

    def sibsp_gar(self)->object:
        pass

    def parch_gar(self)->object:
        pass

    def ticket_gar(self)->object:
        pass

    def fare_ratio(self)->object:
        pass

    def cabin_gar(self)->object:
        pass

    def embarked_nominal(self)->object:
        pass