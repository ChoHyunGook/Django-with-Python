from context.domains import Dataset
from context.models import Model
from titanic import TitanicModels
from icecream import ic


class TitanicTemplate(object):
    def __init__(self,train_fname,test_fname):
        self.model = Model()
        self.ds = Dataset()
        self.titanic = TitanicModels(train_fname,test_fname)
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.test.head()}')
        ic(self.train)
