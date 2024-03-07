"""
author: @Álvaro Cañas

Regresión logística para predecir la supervivencia de los pasajeros del Titanic.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

train = "C:/Users/mame/Documents/proyectos/IABD/SBD/titanic/train.csv"
test = "C:/Users/mame/Documents/proyectos/IABD/SBD/titanic/test.csv"
target = "C:/Users/mame/Documents/proyectos/IABD/SBD/titanic/gender_submission.csv"

train = pd.read_csv(train)
test = pd.read_csv(test)
target = pd.read_csv(target)

train.head()
test.head()