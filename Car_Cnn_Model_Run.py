import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

def CAR_CNN_MODEL(player):
    folder = "./runs/detect/"
    Car_Model_PATH = './TrainModel/Car_Accuracy_Max_CNN100_Ver1.1.h5'
    print("CAR_CNN 실행")
    CarList = []
    model_Car = load_model(Car_Model_PATH)
    try:
        if player == 1:
            for j in range(1, 3):
                Car = [0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0, 0, 0]
                j = str(j)
                file = folder + "exp" + j + "/crops/Character/"
                file_list = os.listdir(file)
                file_count = len(file_list)

                for i in range(0, file_count):
                    img_Car = cv2.imread(file + file_list[i], cv2.IMREAD_GRAYSCALE)
                    img_Car = cv2.resize(img_Car, (28, 28))
                    cv2.threshold(img_Car, 90, 255, cv2.THRESH_BINARY, img_Car)
                    img_Car = img_Car.reshape(1, 28, 28, 1)
                    img_Car = img_Car / 255.0
                    predict_Car = model_Car.predict(img_Car)

                    if np.argmax(predict_Car) == 0:
                        Car[0] += 1
                    elif np.argmax(predict_Car) == 1:
                        Car[1] += 1
                    elif np.argmax(predict_Car) == 2:
                        Car[2] += 1
                    elif np.argmax(predict_Car) == 3:
                        Car[3] += 1
                    elif np.argmax(predict_Car) == 4:
                        Car[4] += 1
                    elif np.argmax(predict_Car) == 5:
                        Car[5] += 1
                    elif np.argmax(predict_Car) == 6:
                        Car[6] += 1
                    elif np.argmax(predict_Car) == 7:
                        Car[7] += 1
                    elif np.argmax(predict_Car) == 8:
                        Car[8] += 1
                    elif np.argmax(predict_Car) == 9:
                        Car[9] += 1
                    elif np.argmax(predict_Car) == 10:
                        Car[10] += 1
                    elif np.argmax(predict_Car) == 11:
                        Car[11] += 1
                    elif np.argmax(predict_Car) == 12:
                        Car[12] += 1

                if np.argmax(Car) == 0:
                    num = "A"
                elif np.argmax(Car) == 1:
                    num = "10"
                elif np.argmax(Car) == 2:
                    num = "J"
                elif np.argmax(Car) == 3:
                    num = "Q"
                elif np.argmax(Car) == 4:
                    num = "K"
                elif np.argmax(Car) == 5:
                    num = "2"
                elif np.argmax(Car) == 6:
                    num = "3"
                elif np.argmax(Car) == 7:
                    num = "4"
                elif np.argmax(Car) == 8:
                    num = "5"
                elif np.argmax(Car) == 9:
                    num = "6"
                elif np.argmax(Car) == 10:
                    num = "7"
                elif np.argmax(Car) == 11:
                    num = "8"
                elif np.argmax(Car) == 12:
                    num = "9"

                CarList.append(num)
            return CarList
        
        elif player == 2:
            for j in range(3, 5):
                Car = [0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0, 0, 0]
                j = str(j)
                file = folder + "exp" + j + "/crops/Character/"
                file_list = os.listdir(file)
                file_count = len(file_list)

                for i in range(0, file_count):
                    img_Car = cv2.imread(file + file_list[i], cv2.IMREAD_GRAYSCALE)
                    img_Car = cv2.resize(img_Car, (28, 28))
                    cv2.threshold(img_Car, 90, 255, cv2.THRESH_BINARY, img_Car)
                    img_Car = img_Car.reshape(1, 28, 28, 1)
                    img_Car = img_Car / 255.0
                    predict_Car = model_Car.predict(img_Car)

                    if np.argmax(predict_Car) == 0:
                        Car[0] += 1
                    elif np.argmax(predict_Car) == 1:
                        Car[1] += 1
                    elif np.argmax(predict_Car) == 2:
                        Car[2] += 1
                    elif np.argmax(predict_Car) == 3:
                        Car[3] += 1
                    elif np.argmax(predict_Car) == 4:
                        Car[4] += 1
                    elif np.argmax(predict_Car) == 5:
                        Car[5] += 1
                    elif np.argmax(predict_Car) == 6:
                        Car[6] += 1
                    elif np.argmax(predict_Car) == 7:
                        Car[7] += 1
                    elif np.argmax(predict_Car) == 8:
                        Car[8] += 1
                    elif np.argmax(predict_Car) == 9:
                        Car[9] += 1
                    elif np.argmax(predict_Car) == 10:
                        Car[10] += 1
                    elif np.argmax(predict_Car) == 11:
                        Car[11] += 1
                    elif np.argmax(predict_Car) == 12:
                        Car[12] += 1

                if np.argmax(Car) == 0:
                    num = "A"
                elif np.argmax(Car) == 1:
                    num = "10"
                elif np.argmax(Car) == 2:
                    num = "J"
                elif np.argmax(Car) == 3:
                    num = "Q"
                elif np.argmax(Car) == 4:
                    num = "K"
                elif np.argmax(Car) == 5:
                    num = "2"
                elif np.argmax(Car) == 6:
                    num = "3"
                elif np.argmax(Car) == 7:
                    num = "4"
                elif np.argmax(Car) == 8:
                    num = "5"
                elif np.argmax(Car) == 9:
                    num = "6"
                elif np.argmax(Car) == 10:
                    num = "7"
                elif np.argmax(Car) == 11:
                    num = "8"
                elif np.argmax(Car) == 12:
                    num = "9"
                    
                CarList.append(num)
            return CarList
    except:
        print("카드를 인식하지 못했습니다.")
    print("CAR_CNN 실행 완료")
