import os 
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        
        try:
            # Read the dataset
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe")
            
            # Ensure that the directory for saving the files exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) #checks folder path on file path
            
            # Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train test split initiated")
            
            # Split the data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            # Save the training and testing data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)

# Main execution
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()


""" 
If your project directory only has a main directory named artifacts and all files under this directory 
(train.csv, test.csv, raw.csv) are stored in the same directory, it may be enough to just check the train_data_path's directory. 
Because the main directory (artifacts) already exists and all files are located under this directory.
"""