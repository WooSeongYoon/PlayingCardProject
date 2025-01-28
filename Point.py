from DBIN import DatabaseInfo
cnxn, curosor = DatabaseInfo()

select_Game_query="""
SELECT *
FROM GameTable
WHERE GameID = ?
"""
select_Round_query="""
SELECT User1Batting1, User2Batting1, User1Batting2, User2Batting2, User1Batting3, User2Batting3, User1Batting4, User2Batting4
FROM RoundTable
WHERE GameID = ?
"""

# 남은 포인트 계산
def PointCount(GameID):
    User1Point = 0
    User2Point = 0
    Count = 0
    
    curosor.execute(select_Game_query, GameID) # GameID로 변경
    row = curosor.fetchone()
    StartUserPoint = row[3]
    StartUsePoint = row[4]

    curosor.execute(select_Round_query, GameID) # GameID로 변경
    row = curosor.fetchone()
    while row:
        Count += 1
        User1Point += row[0] + row[2] + row[4] + row[6]
        User2Point += row[1] + row[3] + row[5] + row[7]
        row = curosor.fetchone()
    User1Point = StartUserPoint - (User1Point + StartUsePoint * Count)   # 지급 포인트 - 배팅 포인트 + 시작 포인트 * 라운드 수
    User2Point = StartUserPoint - (User2Point + StartUsePoint * Count)   # 지급 포인트 - 배팅 포인트 + 시작 포인트 * 라운드 수

    return User1Point, User2Point, Count

