import socket
import ssl

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET表示选择IPV4
s = ssl.wrap_socket(socket.socket())
# 新浪强制HTTPS协议访问 所以 80端口改443端口 socket 改 ssl
# s.connect(('www.sina.com.cn', 80))
s.connect(('www.sina.com.cn', 443))
# 下面的GET / HTTP/1.1这里面的空格是必须的，GET后面的空格删除了会400 Bad Request,HTTP前面的空格删除了会直接报错
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
buffer = []
d = s.recv(1024)
while d:
    buffer.append(d)
    d=s.recv(1024)

'''while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break'''
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)




