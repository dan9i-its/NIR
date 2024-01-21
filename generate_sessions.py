import requests
import re
from bs4 import BeautifulSoup


num_users = 5900
base_username = "user_"
base_password = "password_" 
base_email = "test_email@mail.ru"
users = []
pattern_csrftoken = r'(csrftoken=[\w]+;)'
pattern_sessionid = r'(sessionid=[\w]+;)'
url = 'http://127.0.0.1:8000/accounts/login/?next=main:index'
for i in range(num_users):
    if i < 5900:
        print(i)
        username = base_username+str(i)
        email = str(i)+base_email
        password = base_password+str(i)
        response = requests.get(url)
        #print(response.headers)
        cookies = response.headers.get('Set-Cookie')
        csrftoken = result = re.search(pattern_csrftoken, cookies)
      # print(csrftoken.group(1))
      #  print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
     #   print(csrf_token)

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36',
            'Cookie': csrftoken.group(1)
        }
        data = {
            'csrfmiddlewaretoken': csrf_token,
            'username': username,
            'password': password
        }

        response = requests.post(url, headers=headers, data=data, allow_redirects=False)
       # print(response.text)
      #  print(response.headers)
        cookies = response.headers.get('Set-Cookie')
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            csrftoken = re.search(pattern_csrftoken, cookies).group(1) # нада 
        
            session_id = re.search(pattern_sessionid, cookies).group(1) # нада 
            csrf_middle_ware = soup.find('input', {'name': 'csrfmiddlewaretoken'})
        except Exception as err:
            pass

      #  print(csrftoken)
     #   print(session_id)

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36',
            'Cookie': csrftoken + ' ' + session_id
        }
        response = requests.get('http://127.0.0.1:8000/accounts/login/?next=main:index', headers=headers, allow_redirects=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_middle_ware = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
       # print(csrf_middle_ware)




        users.append(session_id +' ' +csrftoken+' '+ csrf_middle_ware)
    #print("----------------------------------------------------------------------")
   # print(users)
with open("/Users/d.bezrukov/Documents/NIR/sessions", 'w') as file:
    for user in users:
        file.write(user+"\n")