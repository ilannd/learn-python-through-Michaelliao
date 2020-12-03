import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM指定使用面向流的TCP协议
s.connect(('127.0.0.1', 9999)) # 参数是一个tuple，包含地址和端口号
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
