# Overview

This is a very simple server-client file transfer system. The client will take files from its directory location and send them to the server, which will store them in its directory location.

There are options to upload files from client to server, download files from server to client, and check info on files on the server, such as file type, size, and date added to server.

Download the server.py program on the server device, and the client.py program on any devices you want to connect to the server.
If you are testing the promgram on one machine, make sure the server.py and client.py programs are in different folders.

[Software Demo Video](https://youtu.be/QENxAMQmsAE)

# Network Communication

The programs follow a client/server architecture as opposed to peer-to-peer so that the server can just remain active and clients can access it when needed.

TCP is used for the programs, and it uses port 5001.

Requests are given to the server as "{REQUEST TYPE} {Filename}" so that the right function is done and the server can look for the file on download and info requests.

# Development Environment

Visual Studio Code was used to write the programs in Python.

# Useful Websites

* [Realpython](https://realpython.com/python-sockets/)
* [Geeksforgeeks](https://www.geeksforgeeks.org/socket-programming-python/#)

# Future Work

* The program requires a good understanding of how it works to use, I want to add more user friendly features and better error handling
* Some problems were encountered when files were named a certain way or contained certain things. I think it has something to do with tranfer formatting
* Adding the ability to set port via a settings file similar to the IP