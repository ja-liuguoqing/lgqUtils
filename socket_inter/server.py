import socket
import datetime

HOST='0.0.0.0'
PORT=3434

# {AF_INET:IPv4, AF_INET6:IPv6}
# {SOCK_STREAM:TCP, SOCK_DGRAM:UDP}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#使用IPv4和TCP协议创建一个socket
s.bind((HOST,PORT))
s.listen(10)
conn_list = list()
while True:
    conn, addr = s.accept()
    conn_list.append(conn)

print(f"链接地址: {addr}" )
dt = datetime.datetime.now()
message = dt.strftime("%Y-%m-%d %H:%M:%S")
conn.send(message.encode('utf-8'))
print(f"发送消息给{addr}完毕")
conn.close()