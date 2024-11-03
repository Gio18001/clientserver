import socket

# upload function
def send_file(file_name, host, port):
    # attempts connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.sendall(f'UPLOAD {file_name}'.encode()) # sends data preceded by UPLOAD
    with open(file_name, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    client_socket.close()
    print('File sent.')

# download function
def download_file(file_name, host, port):
    # attempts connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.sendall(f'DOWNLOAD {file_name}'.encode()) # sends data preceded by DOWNLOAD
    response = client_socket.recv(1024)

    # downloads data if file is on server
    if response == b'OK':
        with open(f'downloaded_{file_name}', 'wb') as f:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)
        print('File downloaded.')
    else:
        print('File not found on server.')

# info function
def get_file_info(file_name, host, port):
    # attempts connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.sendall(f'INFO {file_name}'.encode()) # sends data preceded by INFO
    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()

# main
if __name__ == '__main__':
    # server info
    cont = True
    hostip = '0.0.0.0'
    port = 5001

    # tries to open ipfile.txt for IP to host server
    try:
        with open('ipfile.txt', 'r') as file:
           hostip = file.read().strip()
    except FileNotFoundError: # if file does not exist, it asks for the host IP and saves to a file so it doesn't need to be put in every time
        hostip = input("No IP file found. What is host IP? ") # get IP from user

        with open('ipfile.txt', 'w') as file:
             file.write(hostip) # create file with IP in it

    print("Server IP: " + hostip)

    while cont:
        x = int(input("\n1. Upload File\n2. Download File\n3. File Info\n4. Quit\n")) # menu options

        # match system for different options. Unrecognised commands are automatically ignored
        match x:
            case 1: # upload
                i = input("Name of file to upload: ")
                send_file(i, hostip, port) 
            case 2: # download
                i = str(input("Name of file to download: "))
                download_file(i, hostip, port)
            case 3: # info
                i = str(input("Name of file on server to check info: "))
                get_file_info(i, hostip, port)
            case 4: # quit
                cont = False