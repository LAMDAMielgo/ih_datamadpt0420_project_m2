from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso

import pandas as pd
import numpy as np
# --------------------------------------------------------------
CLEAN_DATA_PATH = '../data/clean/diamonds_purged.csv'

TRAIN_DATA_PATH = '../data/train'
PREDICTION_DATA_PATH = '../data/predict/diamonds_predict.csv'

NUM_FEATS = []
CAT_FEATS = []
FEATS = NUM_FEATS + CAT_FEATS
TARGET = 'price'
# --------------------------------------------------------------
def getting_feats(df):
    """
    Funtion for categorizing df data
    """
    for col, element in zip(df.columns, df.dtypes):
        if element == 'int64' or element == 'float64':
            NUM_FEATS.append(col)
        elif element == 'object':
            CAT_FEATS.append(col)

    print(f" NUM_FEATS: \t {NUM_FEATS} ")
    print(f" CAT_FEATS: \t {CAT_FEATS} ")
    print(f" ·· Getting Features Lists Done")
    return NUM_FEATS, CAT_FEATS

def getting_prepocessor(NUM_FEATS, CAT_FEATS):
    numeric_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='median')),
                                          ('scaler', StandardScaler())])
    categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                                              ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, NUM_FEATS),
                                                   ('cat', categorical_transformer, CAT_FEATS)])
    return preprocessor

# --------------------------------------------------------------

diamonds = pd.read_csv(CLEAN_DATA_PATH)

getting_feats(diamonds)
preprocessor_diamonds = getting_prepocessor(NUM_FEATS, CAT_FEATS)

# TRAIN A SIMPLE MODEL
diamonds_train, diamonds_test = train_test_split(diamonds)

# CHECK MODEL PERFORMANCE ON TEST AND TRAIN DATA

# CHECK MODEL PERFORMANCE USING CROSS VALIDATION

# OPTIMIZE MODEL USING GRID SEARCH