import socket
import threading
def main():
    # 定义服务器地址和端口号
    SERVER_ADDRESS = input("请输入服务器地址: ")
    SERVER_PORT = int(input("请输入服务器端口号: "))
    # 创建客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
    # 输入昵称
    print("连接成功！")
    nickname = input("请输入你的昵称: ")
    # 发送昵称到服务器
    client_socket.send(nickname.encode())
    print("------------------------------")
    # 接收消息的线程函数
    def receive():
        while True:
            try:
                # 接收数据
                message = client_socket.recv(1024).decode()
                # 打印数据
                print(message)
            except:
                # 出现异常，说明连接已经关闭
                print("连接已经关闭")
                client_socket.close()
                break
    # 启动接收消息的线程
    threading.Thread(target=receive).start()
    # 发送消息的循环
    while True:
        # 获取输入
        message = input()
        # 发送数据
        client_socket.send(message.encode())
if __name__ == '__main__':
    print("欢迎来到Y聊天室客户端！")
    while True:
        try:
            main()
        except:
            print("出现错误！")
        print("------------------------------")
