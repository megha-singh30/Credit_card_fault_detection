import os, sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Data ingestion begins')

        try:
            df = pd.read_csv(os.path.join('notebooks','creditCardFraudData.csv'))
            logging.info('Data read as pandas dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path)

            logging.info('Raw data created')

            X = df.drop(['default payment next month'],axis=1)
            y = df['default payment next month']

            train_data,test_data = train_test_split(df,test_size=0.3,random_state=33)
            #os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            #os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Ingestion of train and test data completed!')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            logging.info('Exception occured at Data ingestion stage')
            CustomException(e,sys)

    