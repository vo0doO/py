def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ вычислить точность вашего наивного байесовского классификатора """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### использовать обученный классификатор для прогнозирования меток для тестовых функций
    pred = clf.predict(features_test)


    ### рассчитать и вернуть точность данных испытаний
    ### это немного отличается от примера,
    ### где мы просто печатаем точность
    ### вам может понадобиться импортировать модуль sklearn
    ### точность = количесто контрольных точек которые мы предсказали правильно / общее количество контрольных
    ### точек теста
    accuracy = clf.score(features_test, labels_test)
    from sklearn.metrics import accuracy_score
    accuracy2 = accuracy_score(pred, labels_test)
    return accuracy, accuracy2
