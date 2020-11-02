import socket, argparse, json, os, sys
import Server

INTERFACE = '127.0.0.1'
PORT = 1060
SEPARATOR = "@"
BUFFSIZE = 4096

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self, mode, textfile, kjfile):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        print('Client has been assigned socket name:', sock.getsockname())
        fsize = os.path.getsize(textfile)
        kjsize = os.path.getsize(kjfile)
        print('Sending mode, text file and {} file size to server:'.format("json" if mode=="change_text" else "key"))
        sock.send(f"{mode}{SEPARATOR}{fsize}{SEPARATOR}{kjsize}".encode())
        with open(textfile, "r") as f:
            textdata = f.read()
            print(textdata)
            print("Sending text file as bytes to server:")
            sock.sendall(bytes(textdata.encode()))
            print((textdata.encode()))
            f.close()
        with open(kjfile, "r") as f:
            kjdata = f.read() if mode == "encode_decode" else json.dumps(f)
            print(f'Sending {"json" if mode=="change_text" else "key"} file as  bytes to server:')
            sock.sendall(bytes(kjdata.encode()))
            f.close()

        print('Receiving result from Server:')
        received = sock.recv(fsize).decode()
        print('Server replied with:', str(received))
        sock.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices={'change_text', 'encode_decode'})
    parser.add_argument('t_file')
    parser.add_argument('k_file')
    args = parser.parse_args()
    print("smth")
    Client(INTERFACE, PORT).connect(args.mode, args.t_file, args.k_file)


if __name__ == '__main__':
    # Server.main()
    main()