from icecream import ic
from context.domains import Dataset
from context.models import Model

class TitanicModels(object):
    model=Model()
    ds=Dataset()


    def preprocess(self,train_fname,test_fname):
        this = self.ds
        that = self.model
        this.train = that.new_dframe(train_fname)
        this.test= that.new_dframe(test_fname)
        this.id =this.test['PassengerId']
        this.label=this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        this=self.drop_feature(this,'Cabin', 'Parch', 'Ticket', 'SibSp')
        #self.kwargs_sample(name='이순신')
        this = self.name_nominal(this)

        '''
        this=self.create_train(this)
        this=self.sex_nominal(this)
        this=self.age_ratio(this)
        this=self.embarked_nominal(this)
        this=self.pclass_ordinal(this)
        this=self.fare_ratio(this)
        '''
        self.df_info(this)
        return this

    @staticmethod
    def id_info(this):
        ic(f'9. id의 타입 {type(this.id)}\n')
        ic(f'9. id의 상위 3개 {type(this.id[:3])}\n')

    @staticmethod
    def df_info(this):
        [ic(f'{i.info()}')for i in [this.train,this.test]]

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}')for i in [this.train,this.test]]

    def create_this(self,dataset)->object:
        this = dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id
        return this

    @staticmethod
    def create_train(this)->object:
        return this

    # 결합도는 낮추고 응집도는 높일수록 이상적인 모듈화가 이루어진다

    @staticmethod
    def drop_feature(this,*feature)->object:
        #[i.drop(j, axis=1, inplace=True)for j in feature for i in [this.train,this.test]]
        [i.drop(list(feature), axis = 1)for i in [this.train, this.test]]
        # 리스트로 형태를 바꿔주는게 a
        '''a=[i for i in feature]
        this.train=this.train.drop(a, axis=1)
        this.test=this.test.drop(a,axis=1)
        '''
        return this

    '''categori=>
        nominal(이름) vs ordinal(순서)
        quantitative=>(숫자)
        interval(상대) vs ratio(절대적인기준)'''

    @staticmethod
    def name_nominal(this) -> object:
        combine = [this.train,this.test]
        for dataset in combine:
            dataset['Title']=dataset.Name.str.extract('([A-Za-z]+)\.',expand=False)
            ic(dataset['Title'])
        return this

    @staticmethod
    def pclass_ordinal(this)->object:
        return this

    @staticmethod
    def sex_nominal(this)->object:
        return this

    @staticmethod
    def age_ratio(this)->object:
        return this

    @staticmethod
    def fare_ratio(this)->object:
        return this

    @staticmethod
    def embarked_nominal(this)->object:
        return this



    @staticmethod
    def kwargs_sample(**kwargs)->None:
        ic(type(kwargs))
        {print(''.join(f'key:{i},val:{j}'))for i,j in kwargs.items()}#key:name,val:이순신