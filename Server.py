import socket, json

INTERFACE = '127.0.0.1'
PORT = 1060
SEPARATOR = "@"
BUFFSIZE = 4096


class Server:
    def __init__(self, interface, port):
        self.interface = interface
        self.port = port

    def bind(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.interface, self.port))
        sock.listen(1)
        print('Listening at', sock.getsockname())
        while True:
            sc, sockname = sock.accept()
            print('We have accepted connection from ', sockname)
            print('Receiving mode, file size and json/key file size:')
            received = sc.recv(BUFFSIZE).decode()
            mode, f_size, k_size = received.split(SEPARATOR)
            f_size, k_size = int(f_size), int(k_size)

            print('Receiving file data from client:')
            filedata = sc.recv(f_size).decode()
            print("Receiving {} data from client.".format('json' if mode == 'change_text' else 'key'))
            kjdata = sc.recv(k_size).decode()
            if mode=="change_text":
                kjdata = json.loads(kjdata)

            result = ""
            if str(mode) == "change_text":
                result = self.change_text(filedata, kjdata)
            else:
                result = self.encode_decode(filedata, kjdata)
                print(result)


            print('Sending result to the client:')
            sc.sendall(bytes(result.encode()))
            sc.close()
            print('File sent, session closed.')

    def change_text(self, text, json):
        for key in json:
            text = text.replace(key, json[key])
        return text


    def encode_decode(self, text, key):
        return "".join(chr(ord(text[i]) ^ ord(key[i%len(key)])) for (i) in range(len(text)))

def main():
    Server(INTERFACE, PORT).bind()

if __name__ == '__main__':
    main()