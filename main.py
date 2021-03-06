import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import guiformodel as gm
data = pd.read_csv("car.data.txt")

#converts into integer values
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
doors = le.fit_transform(list(data["doors"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"

#converts atributes to a list
x = list(zip(buying, maint, doors, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

#hyper parameter
model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

names = ["unacc", "acc", "good", "vgood"]


predicted = model.predict(x_test)


#storing variables for gui stuff
buyingunique = (list(dict.fromkeys(buying)))
buyingunique.sort()
maintunique = list(dict.fromkeys((maint)))
maintunique.sort()
doorsunique = list(dict.fromkeys((doors)))
doorsunique.sort()
personsunique = list(dict.fromkeys((persons)))
personsunique.sort()
lugbootunique = list(dict.fromkeys((lug_boot)))
lugbootunique.sort()
safetyunique = list(dict.fromkeys((safety)))
safetyunique.sort()

gm.opengui()