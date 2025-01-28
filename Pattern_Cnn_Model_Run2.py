import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

def PATTTERN_CNN_MODEL(number):
    folder = "./runs/detect/"
    Pattern_Model_PATH = './TrainModel/Pattern_Accuracy_Max_CNN100_Ver1.1.h5'
    model_Pattern = load_model(Pattern_Model_PATH)
    Pattern = [0, 0, 0, 0]
    number = str(number)
    
    print("PATTTERN_CNN 실행")
    try:
        file = folder + "exp" + number + "/crops/Pattern/"
        file_list = os.listdir(file)
        file_count = len(file_list)

        if file_count == 0:
            Pat = "Error"
            raise

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

        print("PATTTERN_CNN 실행 완료")
        return Pat

    except:
        print("카드(문양)를 인식하지 못했습니다.")
        return Pat
