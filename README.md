# 23-2_CardProject
트럼프 카드를 AI기술을 사용하여 식별 및 분류하고 포커 게임 정보를 데이터베이스에 저장하는 프로그램이다.   
개발 인원: 우성윤, 김민호, 김충현, 박이산   
시연 영상: https://youtu.be/8ZgTw1cgxm4   

## 개발 배경
<img src="https://github.com/user-attachments/assets/dfaa481d-28f0-4996-9505-ef32db6c03f5" width="600" height="400"/>

## 설계 및 구현
<img src="https://github.com/user-attachments/assets/da63c015-b35e-442a-a0c6-5b861588c352" width="600" height="250"/>

### YOLOv5 모델
<img src="https://github.com/user-attachments/assets/30116fb7-1b8e-4ea6-9e32-f2423ae9609d" width="600" height="250"/>

- 전처리 과정
<img src="https://github.com/user-attachments/assets/e9c664f2-68f1-43b7-bedd-e5aae7cf88f2" width="600" height="250"/>

본 이미지는 사용될 실험 환경을 구현할 수 있을 정도의 수준까지 구현시켜 프로그램의 작동 방식 중 전처리가 된 이미지를 반으로 자르는 처리 과정을 기반으로 이미지 생성을 저장시킬 때의 이미지를 데이터 셋에 삽입시켜 정확도를 높이기 위해 다음과 같은 훈련 데이터 증강 과정을 거쳤습니다.   
그렇게 train 12,448장, valid 5,329장, test 2,052장의 데이터셋을 직접 제작했습니다.

### CNN 모델
문자 CNN에 전체 25,956장: train 20,236장, valid 3,796장, test 1,924장   
문양 CNN에 전체 25,765장: train 20,045장, valid 3,796장, test 1,924장으로 구성되었고,   
각각 100 epoch만큼 훈련시켰습니다.   
<img src="https://github.com/user-attachments/assets/9d79f8f3-040b-46cf-840d-da1acce8f028" width="500" height="250"/>

훈련 결과에서는 loss값 0.0189, accuracy 0.9965가 나왔습니다.   

### 데이터베이스
- E-R 다이어그램
<img src="https://github.com/user-attachments/assets/b88865ff-68c8-4013-8a39-2d5900078109" width="500" height="250"/>

- 저장 결과
<img src="https://github.com/user-attachments/assets/86a49f39-b63a-401e-9a2e-640cf380b1a3" width="500" height="300"/>

## 프로그램 실행
![image](https://github.com/user-attachments/assets/c3f882ad-72b9-4bec-9805-122b1c2fc936)

## 성과
- 2023.09.27. | [대구대학교 Linc3.0] 80만원 지원금 선정
- 2023.11.01. | [대구대학교 공학교육혁신센터] 180만원 지원금 선정
- 2023.12.12. | [대구대학교 Linc3.0] 캡스톤디자인 장려상
