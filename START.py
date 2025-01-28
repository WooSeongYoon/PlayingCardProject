import tkinter as tk
from tkinter import simpledialog
import time
from DBIN import DatabaseInfo

cnxn, curosor = DatabaseInfo()

User_insert_query = """
INSERT INTO UserTable (UserID, UserName, WinnerCount, LoseCount)
VALUES (?, ?, ?, ?);
"""
Game_insert_query = """
INSERT INTO GameTable (GameID, User1ID, User2ID, SartPoint, SartUsePoint, Time)
VALUES (?, ?, ?, ?, ?, ?);
"""
select_User_query = """
SELECT *
FROM UserTable
WHERE UserID = ?
"""
select_Game_query="""
SELECT *
FROM GameTable
WHERE GameID = ?
"""

class MainProgram:
    def __init__(slef):
        slef.root = tk.Tk()

        slef.upper_frame = tk.Frame(slef.root)

        slef.upper_txt = tk.Text(slef.upper_frame, width=30, height=40, state=tk.DISABLED)
        slef.scrollbar = tk.Scrollbar(slef.upper_frame, command=slef.upper_txt.yview)

        slef.button_new = tk.Button(slef.root, text="프로그램 시작", command = slef.get_player_info)

    # 화면에 값 반환 함수
    def update_display(slef, message):
        slef.upper_txt.config(state=tk.NORMAL)
        slef.upper_txt.insert(tk.END, message)
        slef.upper_txt.config(state=tk.DISABLED)
        slef.upper_txt.yview_moveto(1.0)
        slef.root.update()

    def GUI(slef):
        slef.root.geometry("500x700+750+200")
        slef.upper_frame.pack()
        slef.upper_txt.pack(side=tk.LEFT, fill=tk.Y)
        slef.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        slef.button_new.pack()

        slef.root.mainloop()

    # 유저 정보 함수
    def get_player_info(self):
        Names = []  # 사용자 이름
        ID = []     # 사용자 ID
        UserNum = 1 # 사용자 번호

        userNum = simpledialog.askinteger("플레이어 수", "플레이어 수를 입력하세요(2):", minvalue=2, maxvalue=2)
        
        while True:
            # 사용자 아이디와 이름 입력
            userID = simpledialog.askstring(f"플레이어 {UserNum} 아이디", f"플레이어 {UserNum} 아이디 입력해주세요.")
            userName = simpledialog.askstring(f"플레이어 {UserNum} 이름", f"플레이어 {UserNum} 이름 입력해주세요.")
            
            # 아이디가 있는지 확인
            curosor.execute(select_User_query, userID)
            row = curosor.fetchone()
            if row is None:   # 아이디가 없으면 실행
                Names.append(userName)
                ID.append(userID)

                self.update_display("신규 이용자 성공\n")
                self.update_display(f"플레이어{UserNum} 아이디: {userID}\n")
                self.update_display(f"플레이어{UserNum} 이름: {userName}\n")

                curosor.execute(User_insert_query, userID, userName, 0, 0)
                cnxn.commit()
                UserNum += 1
                if UserNum > userNum:
                        break
            else:   # 아이디가 있으면 실행
                if row[1] == userName:
                    Names.append(userName)
                    ID.append(userID)

                    self.update_display("기존 이용자 성공\n")
                    self.update_display(f"플레이어{UserNum} 아이디: {ID[UserNum-1]}\n")
                    self.update_display(f"플레이어{UserNum} 이름: {Names[UserNum-1]}\n")
                    UserNum += 1
                    if UserNum > userNum:
                        break
                else:
                    self.update_display(f"플레이어 {UserNum} 이름 불일치!\n")
                    continue
                
        self.update_display("\n")
        self.root.after(1000, self.GameTable, ID)

        # 게임 테이블 함수
    def GameTable(self, ID, player_cards):
        GameID = simpledialog.askstring("게임 테이블 아이디 입력", "테이블 아이디 입력해주세요.")
        self.update_display(f"게임 아이디: {GameID}\n")

        curosor.execute(select_Game_query, GameID)
        row = curosor.fetchone()
        if row is None:
            point = simpledialog.askinteger("게임 시작 포인트", "게임 시작 포인트 입력해주세요.(1 ~ 1000000)", minvalue=1, maxvalue=1000000)
            startingPoint = simpledialog.askinteger("시작 필수 포인트", f"시작 필수 포인트 입력해주세요.(0 ~ {point})", minvalue=0, maxvalue=point)
            now = time.localtime()
            now_time = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
            
            self.update_display(f"게임 시작 포인트: {point}\n")
            self.update_display(f"시작 필수 포인트: {startingPoint}\n")
            self.update_display(f"{now_time}에 신규 게임 테이블 생성\n")
            self.update_display("\n")

            curosor.execute(Game_insert_query, GameID, ID[0], ID[1], point, startingPoint, 0, 0, now_time)
            cnxn.commit()
            # 유저 카드 확인 단계
            self.root.after(1000, player_receive_cards, GameID, ID)

        else:
            if row[1] == ID[0] and row[2] == ID[1]:
                self.update_display(f"{GameID} 게임 테이블 연결\n")
                self.update_display("\n")
                # 유저 카드 확인 단계
                self.root.after(1000, player_receive_cards, GameID, ID)
            else:
                self.update_display(f"이미 {GameID} 게임 테이블이 있습니다.\n")
                self.update_display("다시 정해주세요.\n")
                self.update_display("\n")
                # 게임 테이블 입력 단계
                self.root.after(1000, self.GameTable, ID)
