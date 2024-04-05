import socket
import PySimpleGUI as sg
import inspect


class MemoClientWindow:
    __auto_build = False
    __blueprint = None
    __built = False
    __running = False
    __title = 'Memo Client'
    __window = None
    __no_titlebar = False
    __instance_name = 'MemoClientWindow'
    __template_logger = None

    def __init__(self, host='127.0.0.1', port=65432, auto_build=False):
        self.host = host
        self.port = port
        self.__auto_build = auto_build
        self.__blueprint = [
            [sg.Text('Enter your memo:')],
            [sg.InputText(key='memo', size=(40, 1))],
            [sg.Button('Send'), sg.Button('Exit')]
        ]
        if self.__auto_build:
            self.build()

    def build(self):
        if self.__built:
            raise Exception('Window has already been built!')
        self.__window = sg.Window(self.__title, self.__blueprint, no_titlebar=self.__no_titlebar)
        self.__built = True

    def send_memo(self, memo):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(memo.encode('utf-8'))

    def run(self):
        if not self.__built:
            self.build()
        self.__running = True
        while self.__running:
            event, values = self.__window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            elif event == 'Send':
                memo = values['memo']
                if memo.strip():
                    self.send_memo(memo)
                    sg.popup('Memo sent!', keep_on_top=True)
        self.__window.close()


if __name__ == '__main__':
    client_window = MemoClientWindow(auto_build=True)
    client_window.run()
