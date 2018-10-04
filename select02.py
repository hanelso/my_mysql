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
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    # 3. SQL문 실행
    sql = '''
    select * from pet;
'''
    count = cursor.execute(sql)

    # 4. 결과 받아오기(fetch)
    while True:
        row = cursor.fetchone()
        if row is None:
            break

        print(row)

    # 5. 자원 정리
    cursor.close()
    # conn.commit() #이건 sql문이 insert인 경우 db에 올려주는 과정
    conn.close()

    # 6. 결과 출력
    print(count)

except MySQLdb.Error as e:
    print("Error %d: %s" %(e.args[0],e.args[1]))