def DatabaseInfo():
    import pyodbc

    # SQL Server 접속
    server = 'LAPTOP-JBH2BCOG'
    # Database 이름
    database = 'PlayingCards'
    # 사용자 이름
    username = 'address'
    # 비밀번호
    password = 'adad'

    # 접속 코드
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    # 커서 생성
    curosor = cnxn.cursor()

    return cnxn, curosor
