# -*- coding: utf-8 -*-
from tkinter import *

import Constant as Cons
import MainFunction as Mf


class window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # Set Title
        parent.title('SL-640 Uncooled Type Command Test Tool')
        parent.geometry(f'{Cons.WINDOWS_SIZE["x"]}x{Cons.WINDOWS_SIZE["y"]}+'
                        f'{Cons.WINDOWS_POSITION["x"]}+{Cons.WINDOWS_POSITION["y"]}')
        parent.config(padx=30, pady=30)
        parent.resizable(width=False, height=False)

        # Set UI
        # Get the Network Information from User Input
        def get_network_info():
            print('called net info')
            Cons.host_ip = ip_txt_fld.get()
            Cons.port = port_txt_fld.get()
            Cons.rtsp_port = rtsp_txt_fld.get()
            print(Cons.host_ip, Cons.port, Cons.rtsp_port)

        # TODO: (2024.02.14) Send a specified command for sequentially
        def search_command():
            query = search_txt_fld.get().lower()
            selected_item = []
            for item in Cons.command_array:
                if query in item[0].lower():
                    print(item[0])
                    selected_item.append(item)
                    print('searching is completed')
            Mf.make_table(parent, column_count, Cons.treeview_cell_width, column_name, 0, 160, selected_item)
            self.update()

        # Set Information
        validator_lbl = Label(text='Validator Name', width=Cons.left_label_size, bg=Cons.my_color['fg'], anchor='w')
        validator_lbl.grid(row=0, column=0)
        self.validator_txtfld = Entry(width=Cons.right_text_fd_size, bg=Cons.my_color['spare_fir'])
        self.validator_txtfld.grid(row=0, column=1)

        model_lbl = Label(text='Model Name', width=Cons.left_label_size, bg=Cons.my_color['fg'], anchor='w')
        model_lbl.grid(row=1, column=0)
        self.model_txt_fld = Entry(width=Cons.right_text_fd_size, bg=Cons.my_color['spare_fir'])
        self.model_txt_fld.grid(row=1, column=1)

        fw_lbl = Label(text='FW Info', width=Cons.left_label_size, bg=Cons.my_color['fg'], anchor='w')
        fw_lbl.grid(row=2, column=0)
        self.fw_txt_fld = Entry(width=Cons.right_text_fd_size, bg=Cons.my_color['spare_fir'])
        self.fw_txt_fld.grid(row=2, column=1)

        # Set Network Information
        ip = Cons.ip_lbl_info
        ip_txt = Cons.ip_txt_fld_info
        port = Cons.port_lbl_info
        port_txt = Cons.port_txt_fld_info
        rtsp = Cons.rtsp_lbl_info
        rtsp_txt = Cons.rtsp_txt_fld_info

        ip_lbl = Mf.make_element(x=ip['x'], y=ip['y'],
                                 h=ip['h'], w=ip['w'], element='Label',
                                 bg=ip['bg'], text=ip['text'], anchor='w')
        ip_txt_fld = Mf.make_element(x=ip_txt['x'], y=ip_txt['y'],
                                     h=ip_txt['h'], w=ip_txt['w'], element='Entry',
                                     bg=ip_txt['bg'])

        port_lbl = Mf.make_element(x=port['x'], y=port['y'],
                                   h=port['h'], w=port['w'], element='Label',
                                   bg=port['bg'], text=port['text'], anchor='w')
        port_txt_fld = Mf.make_element(x=port_txt['x'], y=port_txt['y'],
                                       h=port_txt['h'], w=port_txt['w'], element='Entry',
                                       bg=port_txt['bg'])

        rtsp_lbl = Mf.make_element(x=rtsp['x'], y=rtsp['y'],
                                   h=rtsp['h'], w=rtsp['w'], element='Label',
                                   bg=rtsp['bg'], text=rtsp['text'], anchor='w')
        rtsp_txt_fld = Mf.make_element(x=rtsp_txt['x'], y=rtsp_txt['y'],
                                       h=rtsp_txt['h'], w=rtsp_txt['w'], element='Entry',
                                       bg=rtsp_txt['bg'])

        register_btn = Mf.make_element(x=Cons.register_btn['x'], y=Cons.register_btn['y'],
                                       h=Cons.register_btn['h'], w=Cons.register_btn['w'], element='Button',
                                       bg=Cons.register_btn['bg'], text=Cons.register_btn['text'],
                                       anchor='center',
                                       command=get_network_info)

        # Set Searching a command UI
        search_txt_fld = Mf.make_element(x=Cons.search_txt_fld_info['x'], y=Cons.search_txt_fld_info['y'],
                                         h=Cons.search_txt_fld_info['h'], w=Cons.search_txt_fld_info['w'],
                                         bg=Cons.search_txt_fld_info['bg'], element='Entry')
        query_txt = search_txt_fld.get()
        search_btn = Mf.make_element(x=Cons.search_btn['x'], y=Cons.search_btn['y'],
                                     h=Cons.search_btn['h'], w=Cons.search_btn['w'], element='Button',
                                     text=Cons.search_btn['text'],
                                     anchor='center', command=search_command)

        # Set Command Table
        column_name = Cons.column_array
        column_count = len(column_name)
        cmd_data = Cons.command_array

        Mf.make_table(parent, column_count, Cons.treeview_cell_width, column_name, 0, 160, cmd_data)


if __name__ == '__main__':
    root = Tk()
    window(root)

    root.mainloop()
