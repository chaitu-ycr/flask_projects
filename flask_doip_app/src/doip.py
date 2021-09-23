import socket
from platform import system

from flask_doip_app.src.doip_config import doip_target_ecu

doip_payload_types = {
    0x0000: "generic DoIP header negative acknowledge",
    0x0001: "vehicle identification request message",
    0x0002: "vehicle identification request",
    0x0003: "vehicle identification request message with VIN",
    0x0004: "Vehicle announcement message/vehicle identification response",
    0x0005: "routing activation request",
    0x0006: "routing activation response",
    0x0007: "alive check request",
    0x0008: "alive check response",
    0x4001: "DoIP entity status request",
    0x4002: "DoIP entity status response",
    0x4003: "diagnostic power mode information request",
    0x4004: "diagnostic power mode information response",
    0x8001: "diagnostic message",
    0x8002: "Diagnostic message positive acknowledgement",
    0x8003: "diagnostic message negative acknowledgement"
}

# doip_tester_tcp_socket object
doip_tester_tcp_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# doip_tester_tcp_socket.bind((doip_tester['address'], doip_tester['tcp_port']))
doip_tester_tcp_socket.connect((doip_target_ecu['address'], doip_target_ecu['tcp_port']))
doip_tester_tcp_socket.close()

# doip_tester_udp_socket object
doip_tester_udp_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
# doip_tester_udp_socket.bind((doip_tester['address'], doip_tester['udp_port']))
doip_tester_udp_socket.connect((doip_target_ecu['address'], doip_target_ecu['udp_port']))
doip_tester_udp_socket.close()

os_platform = system()
if os_platform == 'Windows':
    print(os_platform)
elif os_platform == 'Linux':
    print(os_platform)
elif print(os_platform) == 'Darwin':
    print(os_platform)
else:
    print(os_platform)
