from time import sleep

import serial
import serial.tools.list_ports

outON = 1
outOFF = 0


class ArduinoUno:
    """
    Using 'ArduinoUno' class we can connect(), disconnect(), write_data(), read_data(), set_digital_output(),
    get_digitalOrAnalog_input_sts()
    """

    def __init__(self, baud_rate=9600, timeout=0.1):
        self.timeout = timeout
        self.port = None
        self.serialUno = None
        self.baud_rate = baud_rate
        self.serial_data_received = None
        self.serial_data_sent = None
        self.port_list = list(serial.tools.list_ports.comports())

    def update_port_list(self):
        self.port_list = list(serial.tools.list_ports.comports())

    def connect(self, portName=None):
        if portName is None:
            for port in self.port_list:
                if "VID:PID=2341:0043" in port[2]:
                    self.port = port[0]
                    self.serialUno = serial.Serial(port=self.port, baudrate=self.baud_rate, timeout=self.timeout)
                    sleep(2)
                    return True
            print('Arduino Uno COM port not found, Check connection and try again')
        else:
            self.serialUno = serial.Serial(port=portName, baudrate=self.baud_rate, timeout=self.timeout)
            sleep(2)
            if self.serialUno is None:
                return False
            else:
                return True
        return False

    def disconnect(self):
        if self.serialUno is None:
            return False
        else:
            return_value = self.serialUno.close()
            return return_value

    def write_data(self):
        if self.serialUno is not None:
            self.serialUno.write(self.serial_data_sent.encode())
            sleep(1)
            return True
        else:
            if self.connect():
                self.serialUno.write(self.serial_data_sent.encode())
                sleep(1)
                return True
            else:
                return False

    def read_data(self):
        """Reads serial data sent by arduino and returns it as string"""
        sleep(1)
        if self.serialUno is not None:
            while self.serialUno.inWaiting() == 0:
                pass
            for i in range(5):
                self.serial_data_received = self.serialUno.readline()
            return self.serial_data_received.decode()
        else:
            if self.connect():
                for i in range(5):
                    self.serial_data_received = self.serialUno.readline()
                return self.serial_data_received.decode()

    def set_digital_output(self, do_data=None):
        """set Arduino digital outputs using this function.
        @:param do_data = '100000' --> DO8 is HIGH / '001101' --> DO10, DO11, DO13 is HIGH and other pins are LOW
        """
        if do_data is not None:
            self.serial_data_sent = do_data
            self.write_data()
        else:
            self.serial_data_sent = '000000'
            self.write_data()

    def get_digitalOrAnalog_input_sts(self, input_name='DI3'):
        """get Arduino digital/Analog input status using this function.
        @:param input_name=DI2/DI3/DI4/DI5/DI6/DI7/AI0/AI1/AI2/AI3/AI4/AI5
        """
        data = self.read_data()
        data = data.strip('\r\n')
        data = data.strip('>')
        data = data.replace('DIsts=', '')
        data = data.replace('AIsts=', '')
        data = data.replace('DOsts=', '')
        data = data.strip('<')
        data = data.split(',')
        uno_data = {'DI2': data[0][0], 'DI3': data[0][1], 'DI4': data[0][2], 'DI5': data[0][3], 'DI6': data[0][4],
                    'DI7': data[0][5],
                    'AI0': data[1], 'AI1': data[2], 'AI2': data[3], 'AI3': data[4], 'AI4': data[5], 'AI5': data[6],
                    'DO8': data[7][0], 'DO9': data[7][1], 'DO10': data[7][2], 'DO11': data[7][3], 'DO12': data[7][4],
                    'DO13': data[7][5]}
        for key in uno_data:
            if key is input_name:
                return uno_data[key]
