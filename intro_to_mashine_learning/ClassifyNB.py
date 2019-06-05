def classify(features_train, labels_train):
    ### импортировать модуль sklearn для GaussianNB
    ### создать классификатор
    ### подогнать классификатор по функциям обучения и меткам
    ### вернуть классификатор соответствия


    ### твой код идет сюда!

    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    return clf
