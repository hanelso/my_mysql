import MySQLdb

try :
    # 1. 연결
    conn = MySQLdb.connect(
        host = '127.0.0.1',
        port=3306,
        user = 'webdb',
        password='webdb',
        db='webdb',
        charset='utf8'
    )
    # 2. 커서 생성
    cursor = conn.cursor()

    # 3. SQL문 실행
    sql = '''
    insert
        into pet
    values('마음이','찬이','dog','m','1994-02-10','0000-00-00');
'''
    count = cursor.execute(sql)

    # 5. 자원 정리
    cursor.close()
    conn.commit() #이건 sql문이 insert인 경우 db에 올려주는 과정
    conn.close()

    # 6. 결과 출력
    print(count)

except MySQLdb.Error as e:
    print("Error %d: %s" %(e.args[0],e.args[1]))