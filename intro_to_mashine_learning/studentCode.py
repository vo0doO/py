from Class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from classify import NBAccuracy

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

def submitAccuracy():
    accuracy, accuracy2 = NBAccuracy(features_train, labels_train, features_test, labels_test)
    return accuracy, accuracy2


print(submitAccuracy())
