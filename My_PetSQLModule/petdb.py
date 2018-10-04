# pet table에 CRUD 함수를 정의한 모듈
import MySQLdb

from My_PetSQLModule.petdb_conf import CONNECTION_LOCAL


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

# (C)RUD
def insert(pet):
    try:
        conn = connect()
        cursor = conn.cursor()

        sql = '''
            insert
                into pet
            values('{0}','{1}','{2}','{3}','{4}','{5}')
        '''.format(pet['name'], pet['owner'], pet['species'],pet['gender'],pet['cirth'],pet['death'])

        count = cursor.execute(sql)

        cursor.close()
        conn.commit()
        conn.close()

        # 6. 결과 출력
        return count == 1

    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return False


# C(R)UD
def fetchbyname(name):
    try:
        conn = connect()
        cursor = conn.cursor()

        sql = '''
                select *
                    from pet
                    where name = '%s'
               ''' %(name)

        cursor.execute(sql)

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        # 6. 결과 출력
        return row

    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return False

# CR(U)D
def update(pet):
    try:
        conn = connect()
        cursor = conn.cursor()

        sql = '''
            update pet
                set gender = '%s',
                    cirth = '%s'
                where death = '0000-00-00'
        '''% ( pet['gender'], pet['cirth'])

        cursor.execute(sql)

        cursor.close()
        conn.commit()
        conn.close()

        return True

    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return False

# CRU(D)
def delete(name):
    try:
        conn = connect()
        cursor = conn.cursor()

        sql = '''
            delete 
                from pet 
                where name = '%s'
        '''% (name)

        count = cursor.execute(sql)

        cursor.close()
        conn.commit()
        conn.close()

        # 6. 결과 출력
        return count == 1

    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return False
