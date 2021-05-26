import base64, datetime

id = "782777035898617886"
a = id.encode("UTF-8")
s = base64.b64encode(a)

print("=======token=======")
print(str(s).split("'")[1])

date = datetime.datetime.utcfromtimestamp(((int(id) >> 22) + 1420070400000) / 1000)

print("=======생성일=======")
print(date)




#import hashlib
#h = hashlib.sha256()
#h.update(b'1234')
#result = h.hexdigest()
#print(result)