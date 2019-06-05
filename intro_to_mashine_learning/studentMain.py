""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.

    The objective of this exercise is to recreate the decision
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """
""" Завершите код в ClassifyNB.py с помощью sklearn
    Наивный байесовский классификатор для классификации данных местности.

    Цель этого упражнения - воссоздать решение
    границу, найденную в видео урока, и сделать сюжет, который
    наглядно показывает границы решения """


from prep_terrain_data import makeTerrainData
from Class_vis import prettyPicture, output_image
from ClassifyNB import classify

import matplotlib
import numpy as np
import matplotlib.pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
### тренировочные данные (features_train, label_train) имеют смешанные точки «быстро» и «медленно»
### вместе - разделите их, чтобы мы могли дать им разные цвета на диаграмме рассеяния,
### и визуально идентифицировать их

grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]


# You will need to complete this function imported from the ClassifyNB script.
# Be sure to change to that code tab to complete this quiz.
# Вам нужно будет завершить эту функцию, импортированную из скрипта ClassifyNB.
# Обязательно перейдите на эту вкладку кода, чтобы завершить этот тест.

clf = classify(features_train, labels_train)
pred = clf.predict(features_test)

### draw the decision boundary with the text points overlaid
### нарисуйте границу решения с наложенными текстовыми точками

prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
