
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np 
from typing import Any, Union,Dict
import os
import json


def loadmodel(logger):
    """Get the model"""
    TRAINED_MODEL_FILEPATH = f"model/model_pkl"
    logger.info(f"model path:{TRAINED_MODEL_FILEPATH}")
    logger.info("loading model")
    with open(TRAINED_MODEL_FILEPATH , 'rb') as f:
        clfdt = pickle.load(f)
    logger.info("returning model object")    
    return clfdt  

def preprocessing(df:np.ndarray,logger):
    """ Applies preprocessing techniques to the raw data"""
    ## in template keep this False by default, if its there then the return result will be other than False
    logger.info("applying standardard scaler")
    scaler = StandardScaler()
    data_df = scaler.fit_transform(df)
    logger.info("applied scaling successfully")
    return data_df
    
def predict(features: np.ndarray,model:Any,logger) -> Dict[str, str]:
    """Predicts the results for the given inputs"""
    try:
        logger.info("model prediction")
        prediction = model.predict(features)
        probabilities = model.predict_proba(features)[0]
    except Exception as e:
        logger.info(e)
        return(e)
    
    return prediction
