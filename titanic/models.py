import numpy as np
import pandas as pd
from icecream import ic
from context.domains import Dataset
from context.models import Model

class TitanicModels(object):
    model=Model()
    ds=Dataset()


    def preprocess(self,train_fname,test_fname):
        this = self.ds
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare',
                   'Cabin', 'Embarked']
        # 데이터셋은 Train, Test, Validation 3종류로 나뉜다
        this.train = that.new_dframe(train_fname)
        this.test= that.new_dframe(test_fname)
        this.id =this.test['PassengerId']
        this.label=this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        #Entity에서 Object로 전환
        this=self.drop_feature(this,'Cabin', 'Parch', 'Ticket', 'SibSp')
        #self.kwargs_sample(name='이순신') kwargs 샘플... 타이타닉 흐름과 무관
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')
        '''
        this=self.create_train(this)
        this=self.pclass_ordinal(this)
        
        '''
        self.df_info(this)
        return this

    @staticmethod
    def id_info(this):
        ic(f'9. id의 타입 {type(this.id)}\n')
        ic(f'9. id의 상위 3개 {type(this.id[:3])}\n')

    @staticmethod
    def df_info(this):
        [print(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

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
    def extract_title_from_name(this) -> None:
        for these in [this.train, this.test]:
            these['Title'] = these.Name.str.extract('([A-Za-z]+)\.', expand=False)
        # ic(this.train.head(5))
        return this

    @staticmethod
    def remove_duplicate(this)->None:
        a=[]
        for dataset in [this.train,this.test]:
            a+=list(set(dataset['Title']))
        a = list(set(a))
        #print(f'>>>{a}')
        '''
                ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
                'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
                Royal : ['Countess', 'Lady', 'Sir']
                Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
                Mr : ['Mlle']
                Ms : ['Miss']
                Master
                Mrs
                '''
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        gender_maping={'male':0,'female':1}
        for these in [this.train,this.test]:
            these['Gender'] = these['Sex'].map(gender_maping)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarked_mapping={'S':1,'C':2,'Q':3}
        this.train=this.train.fillna({'Embarked':'S'})
        for these in [this.train,this.test]:
            these['Embarked']=these['Embarked'].map(embarked_mapping)
        return this

    @staticmethod
    def pclass_ordinal(this)->object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in train, test:
            # pd.cut() 을 사용하시오. 다른 곳은 고치지 말고 다음 두 줄만 코딩하시오
            these['AgeGroup'] = pd.cut(these['Age'], bins, right=True, labels=labels)  # pd.cut() 을 사용
            these['AgeGroup'] = these['AgeGroup'].map(age_mapping)  # map() 을 사용
        return this


    @staticmethod
    def fare_ratio(this) -> object:
        for these in [this.train,this.test]:
            these['FareBand'] = these['Fare'].fillna(1)
            these['FareBand'] = pd.qcut(these['FareBand'], 4)
            # print(f'qcut 으로 bins 값 설정 {this.train["FareBand"].head()}')
            bins = [-1, 8, 15, 31, np.inf]

        return this



    @staticmethod
    def kwargs_sample(**kwargs)->None:
        ic(type(kwargs))
        {print(''.join(f'key:{i},val:{j}'))for i,j in kwargs.items()}#key:name,val:이순신

