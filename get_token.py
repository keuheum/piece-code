import base64, datetime

id = "your discord id"
a = id.encode("UTF-8")
s = base64.b64encode(a)

print("=======token=======")
print(str(s).split("'")[1])

date = datetime.datetime.utcfromtimestamp(((int(id) >> 22) + 1420070400000) / 1000)

print("=======create=======")
print(date)
