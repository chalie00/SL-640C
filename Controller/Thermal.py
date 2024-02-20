import socket
import logging

from Model import Constant as Cons

from socket import AF_INET, SOCK_STREAM

from View import Dialog


# Sending Command with hex
# TODO: (2024.02.14) was applied socket time out
# TODO: (2024.02.15) Dialog box was applied when network error take place
def send_data(send_cmd, root_view):
    host = Cons.host_ip
    input_port = Cons.port
    port = int(0) if Cons.port == '' else int(input_port)
    buf_size = Cons.buf_size
    client = socket.socket(AF_INET, SOCK_STREAM)
    try:
        client.settimeout(3)
        client.connect((host, port))
        # client.send(bytearray([0xff, 0x00, 0x21, 0x13, 0x00, 0x01, 0x35]))
        # client.send(bytes([0xff, 0x00, 0x21, 0x13, 0x00, 0x01, 0x35]))
        client.send(bytes(send_cmd))
        reply = client.recv(buf_size)
        print(reply)
    except socket.error as err:
        print(f'network error:{err}')
        dialog_txt = f'Network Error \n Please check a network info.\n {err}'
        Dialog.DialogBox(root_view, dialog_txt)
        logging.error(err)
    finally:
        client.close()
