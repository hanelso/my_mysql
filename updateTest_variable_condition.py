import MySQLdb

from My_PetSQLModule.petdb_conf import CONNECTION_LOCAL

# sql문의 업데이트 하는데 있어서 set의 갯수를 미리 정하지 않고 가변적으로 가능하게 만들기 위한 test!!

def connect():
    try:
        conn = MySQLdb.connect(
            host=CONNECTION_LOCAL['host'],
            port=CONNECTION_LOCAL['port'],
            user=CONNECTION_LOCAL['user'],
            password=CONNECTION_LOCAL['password'],
            db=CONNECTION_LOCAL['db'],
            charset=CONNECTION_LOCAL['charset']
        )

        return conn

    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return False

try:
    conn = connect()
    cursor = conn.cursor()

    # sql = '''
    #     update pet
    #         set gender = '%s',
    #             cirth = '%s'
    #         where death = '0000-00-00'
    # ''' % (pet['gender'], pet['cirth'])

    table_datas = {'gender':'f','cirth': '2000-00-00'}
    print(list(table_datas))

    sql = '''
        update pet
            set 
            '''
    # sql문의 업데이트 하는데 있어서 set의 갯수를 미리 정하지 않고 가변적으로 가능하게 만들기 위한 반복문.
    for index,dicto in enumerate(table_datas.keys()):       # 딕셔너리로 받은 key값을 dicto에 받음
        print(dicto, type(dicto))                           # dicto의 값 확인
        print(table_datas[dicto], type(table_datas[dicto])) # dicto의 value값 확인
        sql += dicto + ' = \'' + table_datas[dicto]+'\''    # sql문에 dicto = (dicto의 value값) 의 형식으로 추가
        if index == len(list(table_datas))-1:               # 만약 모든 update사항을 끝마치면 ,를 찍지않고 break
            break
        sql += ',\n'                                        # 아직 남은 update사항이 있을경우

    cursor.execute(sql)

    cursor.close()
    conn.commit()
    conn.close()

except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))