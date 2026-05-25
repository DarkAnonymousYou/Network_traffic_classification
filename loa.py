import dill
from sklearn.utils.validation import check_X_y, check_array
from sklearn.utils.validation import check_X_y, check_array
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mutual_info_score
import numpy as np
from sklearn.metrics import accuracy_score
with open('hybrid_model.pkl', 'rb') as file:
    loaded_model = dill.load(file)
s=loaded_model.predict([[51123,445,0,0,66,66,0,1,0,1,0]])
print(s)