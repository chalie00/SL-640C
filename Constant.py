from tkinter import *

import MainFunction as Mf

# Set the Application Size, Position with System Resolution
SYS_RESOLUTION = {'x': 1920, 'y': 1080}
WINDOWS_SIZE = {'x': 800, 'y': 800}
WINDOWS_POSITION = {"x": int((SYS_RESOLUTION['x'] - WINDOWS_SIZE['x']) / 2),
                    "y": int((SYS_RESOLUTION['y'] - WINDOWS_SIZE['y']) / 2)}

POPUP_SIZE = {'x': int(WINDOWS_SIZE['x'] / 2), 'y': int(WINDOWS_SIZE['y'] / 4)}
POPUP_POSITION = {'x': int(WINDOWS_POSITION['x'] + WINDOWS_SIZE['x'] / 2 - POPUP_SIZE['x'] / 2),
                  'y': int(WINDOWS_POSITION['y'] + WINDOWS_SIZE['y'] / 2 - POPUP_SIZE['y'] / 2)}

my_color = {
    'bg': '#FFF8E3',  # Beige
    'fg': '#F3D7CA',  # Peach
    'spare_fir': '#F5EEE6',  # Gray
    'spare_sec': '#E6A4B4',  # Pink
    'noti_bg': '#FFFC9B',  # Yellow
    'noti_txt': '#FFA447'  # Orange
}

# Command File Position
cmd_path = rf'Command/Command.xlsx'

# Network information element position and size
left_label_size = int(WINDOWS_SIZE['x'] * 0.01875)
right_text_fd_size = int(WINDOWS_SIZE['x'] * 0.01875)

ip_lbl_info = {'x': WINDOWS_SIZE['x'] / 2, 'y': WINDOWS_SIZE['y'] / 200,
               'h': WINDOWS_SIZE['y'] / 40, 'w': WINDOWS_SIZE['x'] / 8,
               'bg': my_color['fg'], 'text': 'IP Address'}
ip_txt_fld_info = {'x': ip_lbl_info['x'] + ip_lbl_info['w'] + 5, 'y': ip_lbl_info['y'] - 3,
                   'h': ip_lbl_info['h'] + 6, 'w': ip_lbl_info['w'] * 2.5, 'bg': my_color['spare_fir']}

port_lbl_info = {'x': ip_lbl_info['x'], 'y': ip_lbl_info['y'] + ip_lbl_info['h'] + 10,
                 'h': WINDOWS_SIZE['y'] / 40, 'w': WINDOWS_SIZE['x'] / 8,
                 'bg': my_color['fg'], 'text': 'Port No'}
port_txt_fld_info = {'x': ip_txt_fld_info['x'], 'y': ip_txt_fld_info['y'] + ip_txt_fld_info['h'] + 4,
                     'h': ip_lbl_info['h'] + 6, 'w': ip_lbl_info['w'] * 2.5, 'bg': my_color['spare_fir']}

rtsp_lbl_info = {'x': port_lbl_info['x'], 'y': port_lbl_info['y'] + port_lbl_info['h'] + 10,
                 'h': WINDOWS_SIZE['y'] / 40, 'w': WINDOWS_SIZE['x'] / 8,
                 'bg': my_color['fg'], 'text': 'RTSP Port'}
rtsp_txt_fld_info = {'x': port_txt_fld_info['x'], 'y': port_txt_fld_info['y'] + port_txt_fld_info['h'] + 4,
                     'h': ip_lbl_info['h'] + 6, 'w': ip_lbl_info['w'] * 2.5, 'bg': my_color['spare_fir']}

register_btn = {'x': rtsp_txt_fld_info['x'] + rtsp_txt_fld_info['w'] / 4,
                'y': rtsp_txt_fld_info['y'] + rtsp_txt_fld_info['h'] + 4,
                'h': ip_lbl_info['h'] + 6, 'w': (ip_lbl_info['w'] * 2.5) / 2,
                'bg': my_color['bg'], 'text': 'Register'}

# Searching UI element position and size
search_txt_fld_info = {'x': 0, 'y': register_btn['y'] + register_btn['h'] + 10,
                       'h': ip_lbl_info['h'] + 6, 'w': WINDOWS_SIZE['y'] * 4 / 5,
                       'bg': my_color['spare_fir']}
search_btn = {'x': search_txt_fld_info['x'] + search_txt_fld_info['w'] + 5, 'y': search_txt_fld_info['y'],
              'h': search_txt_fld_info['h'], 'w': WINDOWS_SIZE['y'] * 1 / 10,
              'bg': my_color['spare_sec'], 'fg': my_color['fg'] , 'text': 'Search'}

# Network Information form User Input
host_ip: str = ""
port: int = 0  # Default 32000
rtsp_port: int
buf_size = 4096

# CMD Table(treeview) info
treeview_pos = {'x': 1, 'y': rtsp_txt_fld_info['y'] + 20}
treeview_cell_width = int(WINDOWS_SIZE['x'] * 0.2825)

normal_coord = {
    'x': 0,
    'y': 0,
}

# Table Data
column_array = ['Function', 'Command', 'Remark']
# 0xff, 0x00, 0x21, 0x13, 0x00, 0x01, 0x35
# command_array = [('Color Mode Gray', 'ff002113000034'),
#                  ('Color Mode Rainbow', 'ff002113000135'),
#                  ('Color Mode Iron', 'ff002113000236'),
#                  ('Color Mode Jet', 'ff002113000337'),
#                  ]
command_array = Mf.get_data_from_csv(cmd_path)
