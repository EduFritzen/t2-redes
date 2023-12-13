import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
        skt.connect(('8.8.8.8', 32320))
        with open("music.txt", "rb") as file:
            while file.readable():
                data = file.read(10)
                if data:
                    skt.send(data)

if __name__ == '__main__':
    main()