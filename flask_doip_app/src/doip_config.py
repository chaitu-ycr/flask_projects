from configparser import ConfigParser

# Load DoIP configuration from *.ini file
doip_config = ConfigParser()
doip_config.read("doip_config.ini")
# DoIP Tester
doip_tester = {
    'address': doip_config.get("doip_tester", "address"),
    'tcp_port': int(doip_config.get("doip_tester", "tcp_port")),
    'udp_port': int(doip_config.get("doip_tester", "udp_port")),
    'logical_address': int(doip_config.get("doip_tester", "logical_address"), 16),
}
# DoIP Target ECU
doip_target_ecu = {
    'address': doip_config.get("doip_target_ecu", "address"),
    'multicast_address': doip_config.get("doip_target_ecu", "multicast_address"),
    'tcp_port': int(doip_config.get("doip_target_ecu", "tcp_port")),
    'udp_port': int(doip_config.get("doip_target_ecu", "udp_port")),
    'logical_address_phys': int(doip_config.get("doip_target_ecu", "logical_address_phys"), 16),
    'logical_address_funct': int(doip_config.get("doip_target_ecu", "logical_address_funct"), 16),
}
