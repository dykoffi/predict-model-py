import pandas as pd
from joblib import load

from model import Item

def pred_func(arguments:Item):
    filename = 'final_model.sav'
    last = dict(arguments)
    X_ = pd.DataFrame(last , index = range(1)).values
    loaded_model = load(open(filename, 'rb'))
    pred = loaded_model.predict(X_)
    if pred > 0:
        return "CLIENT SOLVABLE"
    else :
        return "CLIENT NON SOLVABLE"



