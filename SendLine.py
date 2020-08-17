'''
import upip
upip.install('urequests')
'''
import lib.urequests
def sendline(sms):
  
  token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  ## Change to Your Token
 
  msg =str('message=%s'%sms)
  header = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
  page = urequests.post('https://notify-api.line.me/api/notify',headers = header,data = msg)
  print('Back missage',page.text)
  
sendline('hello')
