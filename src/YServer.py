import socket
import threading

def main():
    # 服务器地址和端口号
    SERVER_ADDRESS = ''  # 使用空字符串表示本机地址
    SERVER_PORT = int(input("设置服务器端口（1与65535之间）："))
    # 创建服务端套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定地址和端口号
    server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
    print(f"服务器地址为：{socket.gethostbyname(socket.gethostname())}:{SERVER_PORT}")
    # 开始监听客户端连接
    server_socket.listen()
    print("服务器已开启！\n------------------------------")
    # 保存所有连接的客户端套接字
    clients = []

    # 接收客户端的消息
    def handle_client(client_socket, client_address):
        try:
            nickname = client_socket.recv(1024).decode()
            # 将客户端加入到列表中
            clients.append(client_socket)
            # 给所有客户端发送欢迎消息
            for client in clients:
                client.send(f"{nickname} 进入聊天室".encode())
            while True:
                # 接收客户端的消息
                message = client_socket.recv(1024).decode()
                for client in clients:
                    client.send(f"{nickname}: {message}".encode())
        except:
            # 客户端连接断开
            print("有用户离开……")
            clients.remove(client_socket)
            client_socket.close()
            for client in clients:
                client.send(f"{nickname} 离开聊天室".encode())

    # 循环接受客户端连接
    while True:
        # 等待客户端连接
        client_socket, client_address = server_socket.accept()
        print("有新用户连接……")
        # 新建线程处理客户端的消息
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
if __name__ == '__main__':
    print("欢迎来到Y聊天室服务端！")
    try:
        main()
    except:
        print("出现错误！")
