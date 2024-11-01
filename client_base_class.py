#!/usr/bin/env python
import socket
import logging
import client_logger as client_log


class ClientBaseClass:
   SERVER_IP = "10.100.102.52"
   SERVER_PORT = 8080
   def create_connection_to_server(self):
       """
       Description: Creating connection to server
       :return: client_socket (server connection)
       """
       client_log.client_log(function_name=ClientBaseClass.create_connection_to_server.__name__, message="Connecting to the server side")
       client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       try:
           client_socket.connect((self.SERVER_IP, self.SERVER_PORT))
       except Exception as e:
           client_log.client_log(level=logging.error(f"Failed to connect to server: {e}"))
       return client_socket


   def get_data_from_user(self):
       """
       Description: Receiving user input from the user
       :return: user-data (str)
       """
       client_log.client_log(function_name=ClientBaseClass.get_data_from_user.__name__, message="Getting input from user")
       valid_input = False
       valid_math_operators = ["+", "-", "/", "*"]
       while not valid_input:
           first_number = input("Enter your first number:")
           valid_input = first_number.isnumeric()
           if not valid_input:
               client_log.client_log(level=logging.warning("Invalid number"))
               print("Invalid number")
       valid_input = False
       while not valid_input:
           math_operator = input("Enter your arithmetic operator:")
           valid_input = True if math_operator in valid_math_operators else False
           if not valid_input:
               client_log.client_log(level=logging.warning("Invalid operator"))
               print("Invalid operator")
       valid_input = False
       while not valid_input:
           second_number = input("Enter your second number:")
           valid_input = second_number.isnumeric()
           if not valid_input:
               client_log.client_log(level=logging.warning("Invalid number"))
               print("Invalid number")
       user_data = first_number + ' ' + math_operator + ' ' + second_number
       return user_data


   def print_calculation_result(self, result):
       """
       Description: Printing calculation result on the client side
       :param result: string with user input numbers and operation sign
       :return: None
       """
       client_log.client_log(function_name=ClientBaseClass.print_calculation_result.__name__,
                             message="Printing out the result of the calculation")
       print(f"The result of the calculation is:{result}")


   def send_user_data_to_server(self, user_data, connection):
       """
       Description: Sending user input to server
       :param user_data: string with user input numbers and operation sign
       :param connection: client connection to server
       :return: None
       """
       client_log.client_log(function_name=ClientBaseClass.send_user_data_to_server.__name__,
                             message="Sending user input to the server")
       connection.send(user_data.encode())


   def receive_calculation_result(self, connection):
       """
       Description: Receiving calculation result from the server
       :param connection: connection to the server
       :return: None
       """
       client_log.client_log(function_name=ClientBaseClass.receive_calculation_result.__name__,
                             message="Calculation answer was received")
       result = connection.recv(1024)
       self.print_calculation_result(result.decode())




client_obj = ClientBaseClass()
connection = client_obj.create_connection_to_server()
user_data = client_obj.get_data_from_user()
client_obj.send_user_data_to_server(user_data, connection)
client_obj.receive_calculation_result(connection)
connection.close()
