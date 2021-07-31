#Encryption and decryption using base64
import base64
sitename = '나는 문어 꿈을 꾸는 문어~'
sitename_bytes = sitename.encode('utf-8')
sitename_base64 = base64.b64encode(sitename_bytes)
sitename_base64_str = sitename_base64.decode('utf-8')
print(sitename_base64_str)

sitename_bytes = base64.b64decode(sitename_base64_str)
sitename = sitename_bytes.decode('utf-8')
print(sitename)
