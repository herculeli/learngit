import chardet
f = open('../all_person_name_path/lihanqi_20190319_driving_test.edf','rb')
f1 = open('../all_person_name_path/lihanqi_20190319_driving_test_tr.edf','w')
lis1=f.readlines()
for i in range (0,len(lis1)):
	res = lis1[i].decode('ISO-8859-1')
	res = res.encode('utf-8')
	print(res)
	f1.writelines(res)
f.close()
f1.close()