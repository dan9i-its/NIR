#!/usr/bin/env python
# coding: utf-8


import sys
#import ssl
import time
import signal
import socket
#import certifi
import threading
import re
import argparse
import json
import random

with open("log.txt", "w") as f:
    f.write("")

def signal_handler(sig, frame):
    print('Proxy is Stopped.')
    sys.exit(0)

def write(*content, prt=False):
    if prt : 
        if len(content[0])<100:
            print(*content)
        else:
            print("This message is too long not print in cmd but will store at log.txt.")
    if type(content[0])==bytes:
        content = b" ".join(content)
    else:
        content = bytes(" ".join(content), encoding="utf-8")
    with open("log.txt", "ab") as f:
        f.write(content+b"\n")  

class Proxy:
    def __init__(self, port=7777, ip='127.0.0.1', sessions=[]):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a tcp socket
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reuse the socket
        self.ip = ip
        self.port = port
        self.sessions = sessions
#         self.host = socket.gethostbyname(socket.gethostname())+":%s"%self.port
        self.sock.bind((self.ip, self.port))
        self.sock.listen(10)
        print("Proxy Server Is Start, See log.txt get log.")
        print("Press Ctrl+C to Stop.")
        start_multirequest = threading.Thread(target=self.multirequest)
        start_multirequest.setDaemon(True)
        start_multirequest.start()
        while 1:
            time.sleep(0.01)
            signal.signal(signal.SIGINT, signal_handler)
    
    def get_random_cred(self):
        if len(self.sessions) >= 1:
            max_len = len(self.sessions)
            random_number = random.randint(0, max_len-2)
            return self.sessions[random_number]
        else:
            return None
        
    def multirequest(self):
        while True:
            (clientSocket, client_address) = self.sock.accept() # establish the connection
            client_process = threading.Thread(target=self.main, args=(clientSocket, client_address))
            client_process.setDaemon(True)
            client_process.start()
            
    def main(self, client_conn, client_addr): # client_conn is the connection by proxy client like browser.
        origin_request = client_conn.recv(4096)

        request = origin_request.decode(encoding="utf-8") # get the request from browser
        print("REQUESTS")
        print(request)
        first_line = request.split("\r\n")[0] # parse the first line
        url = first_line.split(" ")[1] # get url
        #url = "https://google.com:443"
        http_pos = url.find("://")
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos + 3):]
        webserver = ""
        port = -1
        port_pos = temp.find(":")
        flag = 0
        webserver_pos = temp.find("/") # find end of web server
        print("TEMP IS")
        print(temp)
        if webserver_pos == -1:
            webserver_pos = len(temp)
        if port_pos == -1 or webserver_pos < port_pos: # default port
            port = 80
            webserver = temp[:webserver_pos]
        else: # specific port
            flag = 1
            print("SPECIFIC PORT")
            # first_occurrence = temp.find('/')  # кастомный порт 
            # second_occurrence = temp.find('/', first_occurrence + 1) 
            # index = temp.find('/', second_occurrence + 1)
            if "8000" in temp[(port_pos + 1):]:    #костыль
                port = 8000
            else:
                port = int(temp[(port_pos + 1):])
            print(port)
            webserver = temp[:port_pos]
            print(webserver)
        if not flag:
            match = re.search(r'Host: \S+', request)
            print("MATCH is"+str(match))
            result = match.group(0)[6:]
            print(result)
            index = result.find(':')
            port = int(result[index+1:])
            print("PORT "  + str(port))

        write("Connected by", str(client_addr))
        write("ClientSocket", str(client_conn))
        write("Browser Request:")
        write(request)
        server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_conn.settimeout(1000)
        try:
            server_conn.connect((webserver, port)) # "server_conn" connect to public web server, like www.google.com:443.
        except: # socket.gaierror: [Errno 11001] getaddrinfo failed
            client_conn.close()
            server_conn.close()
            print("ERROR " + str(webserver) + "  port" + str(port))
            return
        if port==443:
            client_conn.send(b"HTTP/1.1 200 Connection established\r\n\r\n")
            client_conn.setblocking(0)
            server_conn.setblocking(0)
            write("Connection established")
            # now = time.time()
            client_browser_message = b""
            website_server_message = b""
            error = ""
            print(origin_request)
            while 1:
                # if time.time()-now>1: # SET TIMEOUT
                    # server_conn.close()
                    # client_conn.close()
                    # break
                try:
                    reply = client_conn.recv(1024)
                    if not reply: break
                    server_conn.send(reply)
                    client_browser_message += reply
                except Exception as e:
                    pass
                    # error += str(e)
                try:
                    reply = server_conn.recv(1024)
                    if not reply: break
                    client_conn.send(reply)
                    website_server_message += reply
                except Exception  as e:
                    pass
            # error += str(e)
            write("Client Browser Message:")
            write(client_browser_message+b"\n")
            write("Website Server Message:")
            write(website_server_message+b"\n")
            # write("Error:")
            # write(error+"\n")
            server_conn.shutdown(socket.SHUT_RDWR)
            server_conn.close()
            client_conn.close()
            return
        print(origin_request)
        print("PORT: ", str(port))
        ####### здесь нужен код подмены куки в origin_request
        ###########
        encoded_bytes = origin_request
        decoded_string = encoded_bytes.decode('utf-8')

        print("AAAA")
        if 'http://127.0.0.1' in decoded_string:   #### костыль
            print("CHANGE LOCALHOST")
            creds = self.get_random_cred()
            print("CREDS IS")
            print(creds)
            decoded_string = encoded_bytes.decode('utf-8')
            d = decoded_string.replace("http://127.0.0.1:8000", '',1)
            #d = d.replace("sessionid=wg1x80nno4h7azp20zxztnizu1rzht3n;", 'sessionid=SHOPA')
            if creds:

                index1 = d.find("csrftoken")
                old_csrf = d[index1:index1+42]
                index1 = d.find("sessionid")
                old_session = d[index1:index1+42]
                print("REQ BEFORE")
                print(d)
                try:
                    index1 = d.find("csrfmiddlewaretoken")
                    if index1 > 1:
                        csrfmiddlewaretoken = d[index1+20:index1+84]
                        print("I CHANGE ")
                        print(csrfmiddlewaretoken)
                        #d = d.replace(csrfmiddlewaretoken, creds.get("csrf_middle_ware"))
                        print("AFTER CHANGE")
                        print(d)
                except Exception as err:
                    pass
                
                print("OLD SESSION")
                print(old_session)
                d = d.replace(old_session, creds.get("sessionid"))
                print(d)
                d = d.replace(old_csrf, creds.get("csrftoken"))
            origin_request = d.encode('utf-8')

            print(origin_request)
        server_conn.sendall(origin_request)
        write("Website Host Result:")
        while 1:
            # receive data from web server
            data = server_conn.recv(4096)
            try:
                write(data.decode(encoding="utf-8"))
            except:
                write(data)
            if len(data) > 0:
                client_conn.send(data)  # send to browser/client
            else:
                break
        server_conn.shutdown(socket.SHUT_RDWR)
        server_conn.close()
        client_conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='proxy')
    parser.add_argument('--url', default='127.0.0.1')
    parser.add_argument('--port', default='7777')
    parser.add_argument('--sessions', default=None)
    args = parser.parse_args()
    Sessions = []
    ses = []
    try:
        with open(args.sessions,'r') as file:
            ses = file.read().split('\n')
    except Exception as err:
        print(err)
    for i in ses:
        fiels = i.split(' ')
        if len(fiels)>=3:
            Sessions.append({'sessionid':fiels[0],'csrftoken':fiels[1],'csrf_middle_ware':fiels[2]})
    # Путь к директории, в которой нужно искать файлы
    #print(Sessions)
    Proxy(sessions=Sessions)