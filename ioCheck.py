import ipaddress as ips


def private_ip_check(ip):
    try:
        ip_obj = ips.ip_address(ip)
        return ip_obj.is_private
    except ValueError:
        return False


def get_net_range(cidr):
    try:
        network = ips.ip_network(cidr, strict=False)
        return network.network_address, network.broadcast_address
    except ValueError:
        return None


def ip_in_network(ip, network):
    try:
        network_object = ips.ip_network(network, strict=False)
        ip_object = ips.ip_address(ip)
        return ip_object in network_object
    except ValueError:
        return False


def generate_ip_in_network(network):
    try:
        network_object = ips.ip_network(network, strict=False)
        return [str(ip) for ip in network_object.hosts()]
    except ValueError:
        return []


def int_to_ipv4(integer):
    try:
        return str(ips.IPv4Address(integer))
    except ValueError:
        return None


ipv4int = 3232235777
ip = "192.168.1.1"
cidr = "10.151.108.0/23"
network = "192.168.1.1/30"

print(f'Is {ip} private? - {private_ip_check(ip)}')
network_range = get_net_range(cidr)
ips_in_net = generate_ip_in_network(network)

if network_range:
    print(f'Network range: {network_range[0]} - {network_range[1]}')

print(f'Is {ip} in {cidr}? {ip_in_network(ip, cidr)}')

print(f'IP addresses in {network}: {ips_in_net}, \nnumber of hosts: {len(ips_in_net)}')

print(f'Integer {ipv4int} -> IP v4 {int_to_ipv4(ipv4int)}')
