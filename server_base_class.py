﻿#!/usr/bin/env python
import socket
import operator
import logging
import server_logger as server_log




class ServerBaseClass:


   def calculate_received_data(self, user_data):
       """
       Description: Calculating arithmetic operation according to user input
       :param user_data: string with user input numbers and operation sign
       :return: result (int)
       """
       result = 0
       ops = {
           '+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv
       }
       server_log.server_log(function_name=ServerBaseClass.calculate_received_data.__name__,
                             message="Calculating arithmetic operation according to user input")
       operation_list = user_data.split()
       try:
           result = ops[operation_list[1]](int(operation_list[0]), int(operation_list[2]))
       except Exception as e:
           server_log.server_log(level=logging.error(f"Calculation failed with: {e}"))
       return result


   def create_connection_to_server(self):
       """
       Description: Creating connection to client
       :return: clientConnection (client connection)
       """
       SERVER_IP = "10.100.102.52"
       SERVER_PORT = 8080
       server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server_log.server_log(function_name=ServerBaseClass.create_connection_to_server.__name__,
                             message="Starting listening to the client side")
       try:
           server_socket.bind((SERVER_IP, SERVER_PORT))
       except Exception as e:
           server_log.server_log(level=logging.error(f"Failed to connect to server: {e}"))
       server_socket.listen(1)
       server_log.server_log(message="Server started")
       server_log.server_log(message="Waiting for client request")
       clientConnection, clientAddress = server_socket.accept()
       server_log.server_log(message=f"Connected client : {clientAddress}")
       return clientConnection


   def receive_user_data(self, connection):
       """
       Description: Receiving user input from the client server
       :param connection: client connection
       :return: user-data (str)
       """
       server_log.server_log(function_name=ServerBaseClass.receive_user_data.__name__,
                             message="Equation received")
       data = connection.recv(1024)
       user_data = data.decode()
       return user_data


   def send_calculation_result_to_user(self, user_data, connection):
       """
       Description: Calling calculation function and printing log to Server logger
       :param user_data: string with user input numbers and operation sign
       :return: None
       """
       server_log.server_log(function_name=ServerBaseClass.receive_user_data.__name__,
                             message="Sending the result to user")
       connection.send(str(self.calculate_received_data(user_data)).encode())




server_obj = ServerBaseClass()
connection = server_obj.create_connection_to_server()
user_data = server_obj.receive_user_data(connection)
server_obj.send_calculation_result_to_user(user_data, connection)
connection.close()
