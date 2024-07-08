import sys
import pandas as pd
from source.commons import load_object
from source.exception import UserException
from source.logger import logging

class PredicPipeline:
    def __init__(self):
        pass
    
    logging.info('Preprocessing user input and making predictions')
    def predict(self,features):
        model_path = 'elements\model.pkl'
        preprocessor_path = 'elements\preprocessor.pkl'
        # loaeding objects
        model = load_object(model_path)
        preprocessor = load_object(preprocessor_path)
        
        data_processed = preprocessor.transform(features)
        prediction = model.predict(data_processed)
        
        return prediction
logging.info('This class is responsible for mapping all the inputs from html to flask')
class UserData:
    def __init__(self,gender,location,gamegenre,ingamepurchases,gamedifficulty,
                 sessionsperweek,avgsessiondurationminutes,playerlevel,achievementsunlocked):
        self.gen = gender
        self.loc = location
        self.game = gamegenre
        self.purch = ingamepurchases
        self.diff = gamedifficulty
        self.sess = sessionsperweek
        self.dur = avgsessiondurationminutes
        self.level = playerlevel
        self.ach = achievementsunlocked
        
    # let's write a function that returns the user input as a pandas dataframe
    def get_data_as_df(self):
        try:
            user_data = {
                "gender":[self.gen],
                "location":[self.loc],
                "gamegenre":[self.game],
                "ingamepurchases":[self.purch],
                "gamedifficulty":[self.diff],
                "sessionsperweek":[self.sess],
                "avgsessiondurationminutes":[self.dur],
                "playerlevel":[self.level],
                "achievementsunlocked":[self.ach]
            }
            return pd.DataFrame(user_data)
        except Exception as e:
            raise UserException(e,sys)
        