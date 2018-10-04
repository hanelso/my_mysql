from My_PetSQLModule import petdb

ret = petdb.delete('파트라슈')
print('delete test:', ret)

# insert test
ret = petdb.insert({'name': '파트라슈', 'owner': '네로', 'species': 'dog', 'gender': 'm', 'cirth': '1980-01-02', 'death': '0000-00-00'})
print('insert test:', ret)

result = petdb.fetchbyname('파트라슈')
print(result)



