import logging

def server_log(function_name='', level=logging.DEBUG, message=" "):
   logging.basicConfig(
       level=level,
       format="SERVER: %(asctime)s %(levelname)s %(message)s",
       datefmt="%Y-%m-%d %H:%M:%S",
       filename="server.log"
   )
   if len(function_name) > 1:
       logging.debug(f"Function {function_name} Enter")
       logging.info(f"{message}")
       logging.debug(f"Function {function_name} Exit")
   else:
       logging.info(f"{message}")
