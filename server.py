import socket
import os
from datetime import datetime

def start_server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    #Main scan loop to check for incoming requests
    while True:
        conn, addr = server_socket.accept()
        print(f'Connection from {addr}')
        
        command = conn.recv(1024).decode()
        
        # data preceded with UPLOAD will upload data to server
        if command.startswith("UPLOAD"):
            filename = command.split()[1] # Takes file name from data
            print(f'Uploading file: {filename}')
            with open(filename, 'wb') as f: # Creates a file with the same data
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print('File uploaded.')

        #data preceded with DOWNLOAD will download from server to client
        elif command.startswith("DOWNLOAD"):
            filename = command.split()[1] # Takes file name from data
            print(f'Downloading file: {filename}')
            if os.path.exists(filename):
                conn.sendall(b'OK')
                with open(filename, 'rb') as f:
                    while (data := f.read(1024)):
                        conn.sendall(data) # sends all the data for the client to download
                print('File downloaded.')
            else:
                conn.sendall(b'NOT FOUND') # sends not found if file is not on server

        # data preceded with info gets file info from the server and send to the client
        elif command.startswith("INFO"):
            filename = command.split()[1] # Takes file name from data
            print(f'Getting info for file: {filename}')
            if os.path.exists(filename):
                file_info = {
                    'type': filename.split('.')[-1],  # Get the file extension
                    'size': os.path.getsize(filename),  # File size in bytes
                    'date_added': datetime.fromtimestamp(os.path.getctime(filename)).isoformat()  # Date added
                }
                response = f"Type: {file_info['type']}, Size: {file_info['size']} bytes, Date Added: {file_info['date_added']}" # format for readability
                conn.sendall(response.encode()) # sends file info to client
            else:
                conn.sendall(b'NOT FOUND') # sends not found if file is not on server

        conn.close()

if __name__ == '__main__':
    start_server()