from httplib2 import Http
from urllib.parse import urlencode



url = 'https://notify-api.line.me/api/notify'
token = <<TOKEN>>' #ขอข้ามขั้นตอนการหา Token นะครับ(น่าจะหาได้)
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg = {'message':'Hello LINE Notify สวัสดีชาวโลก'}
response = Http().request(url,
                 "POST",
                 headers=headers,
                 body=urlencode(msg)
)
print(response)

