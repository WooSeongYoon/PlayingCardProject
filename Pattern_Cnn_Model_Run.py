import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

def PATTTERN_CNN_MODEL(player):
    print("PATTTERN_CNN 실행")
    PatternList = []
    folder = "./rluns/detect/"
    Pattern_Model_PATH = './TrainModel/Pattern_Accuracy_Max_CNN100_Ver1.1.h5'
    model_Pattern = load_model(Pattern_Model_PATH)

    if player == 1:
        for j in range(1, 3):
            Pattern = [0, 0, 0, 0]
            j = str(j)
            file = folder + "exp" + j + "/crops/Pattern/"
            file_list = os.listdir(file)
            file_count = len(file_list)

            for i in range(0, file_count):
                img_Pattern = cv2.imread(file + file_list[i], cv2.IMREAD_GRAYSCALE)
                img_Pattern = cv2.resize(img_Pattern, (28, 28))
                cv2.threshold(img_Pattern, 70, 255, cv2.THRESH_BINARY, img_Pattern)
                img_Pattern = img_Pattern.reshape(1, 28, 28, 1)
                img_Pattern = img_Pattern / 255.0
                predict_Pattern = model_Pattern.predict(img_Pattern)

                if np.argmax(predict_Pattern) == 0:
                    Pattern[0] += 1
                elif np.argmax(predict_Pattern) == 1:
                    Pattern[1] += 1
                elif np.argmax(predict_Pattern) == 2:
                    Pattern[2] += 1
                elif np.argmax(predict_Pattern) == 3:
                    Pattern[3] += 1

            if np.argmax(Pattern) == 0:
                Pat = "Clover"
            elif np.argmax(Pattern) == 1:
                Pat = "Diamond"
            elif np.argmax(Pattern) == 2:
                Pat = "Heart"
            elif np.argmax(Pattern) == 3:
                Pat = "Spade"
            
            PatternList.append(Pat)
        return PatternList
    
    elif player == 2:
        for j in range(3, 5):
            Pattern = [0, 0, 0, 0]
            j = str(j)
            file = folder + "exp" + j + "/crops/Pattern/"
            file_list = os.listdir(file)
            file_count = len(file_list)

            for i in range(0, file_count):
                img_Pattern = cv2.imread(file + file_list[i], cv2.IMREAD_GRAYSCALE)
                img_Pattern = cv2.resize(img_Pattern, (28, 28))
                cv2.threshold(img_Pattern, 80, 255, cv2.THRESH_BINARY, img_Pattern)
                img_Pattern = img_Pattern.reshape(1, 28, 28, 1)
                img_Pattern = img_Pattern / 255.0
                predict_Pattern = model_Pattern.predict(img_Pattern)

                if np.argmax(predict_Pattern) == 0:
                    Pattern[0] += 1
                elif np.argmax(predict_Pattern) == 1:
                    Pattern[1] += 1
                elif np.argmax(predict_Pattern) == 2:
                    Pattern[2] += 1
                elif np.argmax(predict_Pattern) == 3:
                    Pattern[3] += 1

            if np.argmax(Pattern) == 0:
                Pat = "Clover"
            elif np.argmax(Pattern) == 1:
                Pat = "Diamond"
            elif np.argmax(Pattern) == 2:
                Pat = "Heart"
            elif np.argmax(Pattern) == 3:
                Pat = "Spade"

            PatternList.append(Pat)
        return PatternList
    
    print("PATTTERN_CNN 실행 완료")
