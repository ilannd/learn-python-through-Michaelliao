import socket
import threading
import time

# TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。
# 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了.

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 注意这里的，UDP不能以流的形式发送数据。
s.bind(('127.0.0.1', 9999))   # 绑定端口

# 不需要调用listen()方法，而是直接接收来自任何客户端的数据
# s.listen(5)
# print('Waiting for connection....')

# UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定
print('Building UDP on 9999')

'''def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)'''

while True:
    data, addr = s.recvfrom(1024)
    # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端
    # 注意这里省掉了多线程，因为这个例子很简单

    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello,%s!' % data, addr)
    # t = threading.Thread(target=tcplink, args=(sock, addr))
    # t.start()
