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
        '''
        this=self.create_train(this)
        this=self.name_nominal(this)
        this=self.sex_nominal(this)
        this=self.age_ratio(this)
        this=self.embarked_nominal(this)
        this=self.pclass_ordinal(this)
        this=self.fare_ratio(this)
        '''
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        ic(f'1. Train의 타입 {type(this.train)}\n')
        ic(f'2. Train의 컬럼 {this.train.columns}\n')
        ic(f'3. Train의 상위1개 {this.train.head(1)}\n')
        ic(f'4. Train의 null의 개수 {this.train.isnull().sum()}\n')
        ic(f'5. Test의 타입 {type(this.test)}\n')
        ic(f'6. Test의 컬럼 {this.test.columns}\n')
        ic(f'7. Test의 상위1개 {this.test.head(1)}\n')
        ic(f'8. Test의 null의 개수 {this.test.isnull().sum()}\n')
        ic(f'9. id의 타입 {type(this.id)}\n')
        ic(f'9. id의 상위 10개 {type(this.id[:10])}\n')
        print('*'*100)


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
        #[i.drop(list(feature), axis = 1)for i in [this.train, this.test]]
        # 리스트로 형태를 바꿔주는게 a
        a=[i for i in feature]
        this.train=this.train.drop(a, axis=1)
        this.test=this.test.drop(a,axis=1)

        '''
        this.train = this.train.drop([i for i in feature], axis=1)
        this.test = this.test.drop([i for i in feature], axis=1)
        '''
        return this

    '''categori=>
        nominal(이름) vs ordinal(순서)
        quantitative=>(숫자)
        interval(상대) vs ratio(절대적인기준)'''

    @staticmethod
    def pclass_ordinal(this)->object:

        return this

    @staticmethod
    def name_nominal(this)->object:
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