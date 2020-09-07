from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

import pandas as pd
pd.options.display.max_columns = 35
pd.options.display.max_rows = 25
# -------------------------------------------------------------- GLOBAL VARIABLES
CLEAN_DATA_PATH = '../data/clean/diamonds_cleaned.csv'
TRAIN_DATA_PATH = '../data/train'
NUM_FEATS = []
CAT_FEATS = []
COLS_TO_DROP = ['color_num', 'clarity_num', 'cut_num', 'carat_range', 'table_range', 'color_range', 'Unnamed: 0']
# --------------------------------------------------------------
def save_df_to_csv(df, path, name):
    print(f' ·· Saving df in {path} as {name}')
    path = './' + f'{path}'
    return df.to_csv(f'{path}/{name}.csv')

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

def data_for_hypothesis_testing(df, NUM_FEATS, CAT_FEATS, path, name):
    cat_df = pd.get_dummies(df[CAT_FEATS])
    num_df = df.loc[:, NUM_FEATS]
    df = pd.concat([cat_df, num_df])
    save_df_to_csv(df, path = path, name = name)
    print(f" ·· Saved df for Hypothesis Testing")
# --------------------------------------------------------------
diamonds = pd.read_csv(CLEAN_DATA_PATH)

# Adding another col and dropping cols that were olny necessary for Tableau
diamonds['T/D_ratio'] = diamonds['table'] / diamonds['depth']
diamonds.drop(columns=COLS_TO_DROP, axis=1, inplace=True)

# Feats Lists and preprocessing
getting_feats(diamonds)
getting_prepocessor(NUM_FEATS, CAT_FEATS)
data_for_hypothesis_testing(diamonds, NUM_FEATS, CAT_FEATS, path = TRAIN_DATA_PATH, name = 'diamonds_train_ht')

# Saving
save_df_to_csv(diamonds, path=TRAIN_DATA_PATH, name='diamonds_train_main')
print(diamonds.head(3))




