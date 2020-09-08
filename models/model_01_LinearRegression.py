from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder

from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_squared_error, r2_score


import pandas as pd
import numpy as np
# --------------------------------------------------------------
CLEAN_DATA_PATH = '../data/clean/diamonds_purged.csv'

TRAIN_DATA_PATH = '../data/train'
PREDICTION_DATA_PATH = '../data/predict/diamonds_predict.csv'
# --------------------------------------------------------------
def getting_feats(df):
    """
    Function for categorizing df data
    """
    NUM_FEATS, CAT_FEATS, FEATS = [], [], []

    for col, element in zip(df.columns, df.dtypes):
        if (element == 'int64' or element == 'float64') and col != 'price':
            NUM_FEATS.append(col)
        elif element == 'object':
            CAT_FEATS.append(col)

    FEATS = NUM_FEATS + CAT_FEATS
    print(f" NUM_FEATS: \t {NUM_FEATS} ")
    print(f" CAT_FEATS: \t {CAT_FEATS} ")
    print(f" FEATS: \t {FEATS} ")
    print(f" ·· Getting Features Lists Done")
    return NUM_FEATS, CAT_FEATS, FEATS


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
print(diamonds.head(3))
NUM_FEATS, CAT_FEATS, FEATS = getting_feats(diamonds)
TARGET = 'price'
# --------------------------------------------------------------
preprocessor_diamonds = getting_prepocessor(NUM_FEATS, CAT_FEATS)
diamonds_train, diamonds_test = train_test_split(diamonds)  # splits at 25-75 ratio

# ------------------------ Model 1
model = Pipeline(steps=[('preprocessor', preprocessor_diamonds),
                        ('regressor', BaggingRegressor())])

param_grid = {
    'preprocessor__num__imputer__strategy': ['mean', 'median'],
    'regressor__n_estimators': [28, 32, 40, 56, 64, 72, 81],
    'regressor__max_features': [8,16,28,32],
    }

grid_search = RandomizedSearchCV(model, param_grid,
                                 cv = 5, verbose = 10,
                                 scoring = 'neg_root_mean_squared_error',
                                 n_jobs = -1, n_iter = 28)

grid_search.fit(diamonds[FEATS], diamonds[TARGET]) # No necesito el train_test_split aquí porque es Cross Validation
print(f"Best params: {grid_search.best_params_}")
print(f"Best RMSE: {grid_search.best_score_}")

# Getting metrics
y_test = grid_search.predict(diamonds_test[FEATS])
y_train = grid_search.predict(diamonds_train[FEATS])

print('·· RMSE')
print(f" test error: \t {mean_squared_error(y_pred = y_test, y_true=diamonds_test[TARGET], squared=False)} $")
print(f"train error: \t {mean_squared_error(y_pred = y_train, y_true=diamonds_train[TARGET], squared=False)} $")
print('\n·· R2')
print(f" test error: \t {r2_score(y_pred = y_test, y_true=diamonds_test[TARGET])}  -> 0..1")
print(f"train error: \t {r2_score(y_pred = y_train, y_true=diamonds_train[TARGET])} -> 0..1")

