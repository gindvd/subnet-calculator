"""
Subnet Calculator functions

A collection of functions to calculate the size of a subnets, 
determine the subnet an ip address belongs in, and calculate various
details of the network.

These functions only use the base Python function with no use of built in, 
or other third party libraries for educational purposes

Created by: David Gingerich
"""


def is_ipv4_address(dotquad: str) -> bool:
    """ Checks if dotted decimal IP address is valid """
    octets = dotquad.split(".")

    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False
        
        octet = int(octet)
        if 0 > octet > 255:
            return False
    
    return True


def starting_network(dotquad: str, network_bits: int) -> int:
    """
    Returns integer of lowest network that the given ip address could be in

    Ex: IP 10.10.10.12 with subnet mask 255.255.248.0 returns 10.10.0.0 as integer
    """
    if not is_ipv4_address(dotquad):
        raise ValueError(f"Invalid netmask: {dotquad}")
    
    if network_bits == 32:
        return dotquad_to_int(dotquad)
    
    elif network_bits == 0:
        return 0

    octet_idx = network_bits // 8
    octets = [int(octet) for octet in dotquad.split(".")]

    for i in range(octet_idx, 4):
        octets[i] = 0

    return octets[0] << 24 | octets[1] << 16 | octets[2] << 8 | octets[3] 


def dotquad_to_int(dotquad: str) -> int:
    """
    Returns integer that equals the ipv4 binary

    Example:
    "255.255.255.255" -> 4294967296
    """
    if not is_ipv4_address(dotquad):
        raise ValueError(f"Invalid netmask: {dotquad}")
    
    a, b, c, d = (int(octet) for octet in dotquad.split("."))
    # Integer representation of all 32 bits of subnet mask
    return a << 24 | b << 16 | c << 8 | d


def validate_subnet_mask(mask: int) -> int:
    """
    Validates if subnet mask is valid

    Returns the number of consecutive 0 bits on the right
    """
    # Count the number of consecutive 0 bits at the right
    m = mask & -mask
    right0bits = -1

    while m:
        m >>= 1
        right0bits += 1

    # Verify that all the bits to the left are 1's
    if mask | ((1 << right0bits) - 1) != 0xffffffff:
        raise ValueError(f"Invalid netmask:  /{dotquad}")
    
    return right0bits


def ipv4_mask_len(dotquad: str) -> tuple[int, int]:
    """
    Takes a dotted decimal subnet mask and returns the number
    of network bits and host bits
    """
    
    # Integer representation of all 32 bits of subnet mask
    mask: int = dotquad_to_int(dotquad)

    if mask == 0:
        return 0

    right0bits = validate_subnet_mask(mask)

    return 32 - right0bits, right0bits


def cidr_notation_to_netmask(prefix: int) -> str:
    """
    Converts CIDR slash notation /(0 - 32) to a dotted decimal subnet mask
    """
    if 0 > prefix > 32:
        raise ValueError(f"Invalid CIDR prefix:  /{prefix}")
    
    mask_int: int = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
    binary_str: str = format(mask_int, 'b') # Converts to string of binary

    octets: list[str] = [str(int(binary_str[i:i+8], 2)) for i in range(0, 32, 8)]

    return ".".join(octets)


def int_to_dotquad(ip_int: int) -> str:
    """ Converts integer representation of ip address to dotquad string """
    binary_str = format(ip_int, 'b')
    
    # Adds missing 0s to start of binary string for easier conversion
    str_len = len(binary_str)
    if str_len != 32:
        binary_str = ("0" * (32 - str_len)) + binary_str
    
    octets: list[str] = [str(int(binary_str[i:i+8], 2)) for i in range(0, 32, 8)]

    return ".".join(octets)


def get_host_size(host_bits: int) -> int:
    """
    Takes the host_bits count (number of contiguous 0s in the subnet mask),
    returns the amount of ip address in that network

    """
    if 0 > host_bits > 32:
        raise ValueError(f"Invalid number of host bits:  /{host_bits}")

    return 2 ** host_bits


def calculate_network_addr(ip_addr: str, subnet_mask: str) -> str:
    """
    Calculates the network address a given ip with given subnet mask is in
    """
    network_addr: str = "0.0.0.0/0" 
    network_bits, host_bits = ipv4_mask_len(subnet_mask)

    # network range to check what network the given ip address is in
    increment = 1 << host_bits

    if increment == 1:
        return ip_addr
    
    ip_int: int = dotquad_to_int(ip_addr)
    network_int: int = starting_network(ip_addr, network_bits)

    while True:
        next_network = network_int + increment

        if network_int <= ip_int < next_network:
            network_addr = int_to_dotquad(network_int)
            break
        
        network_int = next_network

    return network_addr


def host_size_to_subnet_mask(host_size: int) -> str:
    """ Takes subnet size and converts into dotquad subnet mask """
    mask: int = 0xffffffff ^ (~host_size)

    _ = validate_subnet_mask(mask)

    octect_bin: int = 0b11111111

    a = mask >> 24 # Gets first 8 bits
    b = (mask >> 16) & octect_bin # Gets bits 9 to 16
    c = (mask >> 8) & octect_bin # Gets bits 17 to 24
    d = mask & octect_bin # Get last 8 bits

    return f"{str(a)}.{str(b)}.{str(c)}.{str(d)}"


def calculate_subnet(
    network_addr: str, subnet_mask: str, hosts_per_subnet: list[int]
) -> tuple(list[str], list[str]):
    """
    Divides a network into subnets

    Parameters:
        network_addr - he network to be divided into subnets
        subnet_mask - subnet mask of the divided network

        hosts_per_subnet - list of number of needed hosts per subnet
                         - length of list is the number of subnets required
    
    Return:
        subnets - list of network addresses for each subnet
        netmask - list of subnet mask for each subnet
    
    """
    if not is_ipv4_address(network_addr):
        raise ValueError(f"Invalid network address: {network_addr}")

    _, host_bits = ipv4_mask_len(subnet_mask)

    # The total number of available hosts on the iven network
    available_hosts = get_host_size(host_bits) - 2

    # Total number of hosts plus the network addr and broadcast addr for each subnet
    total_hosts = sum(hosts_per_subnet) + (2 * len(hosts_per_subnet))

    if total_hosts > available_hosts:
        raise ValueError(f"{network_addr} {subnet_mask} cannot be divided into specified subnets!")

    # Sort subnets fro largest to smallest
    hosts_per_subnet.sort(reverse=True)

    subnet_addr: int = dotquad_to_int(network_addr)

    subnets: list[str] = []
    netmasks: list[str] = []

    for hosts in hosts_per_subnet:
        m = 1

        while m < hosts:
            m << 1
        
        subnets.append(int_to_dotquad(subnet_addr))
        netmasks.append(host_size_to_subnet_mask(m))
    
        subnet_addr += m

    return subnets, netmasks


def get_broadcast_addr(network_addr: str, subnet_mask: str) -> str:
    """ Gets the broadcast address (last IP address) of a subnet """
    if not is_ipv4_address(network_addr):
        raise ValueError(f"Invalid network address: {network_addr}")

    _, host_bits = ipv4_mask_len(subnet_mask)

    mask = ~(1 << host_bits) # Inverted host bits

    net_addr_int = dotquad_to_int(network_addr)

    broadcast_int = net_addr_int + mask # Gets the last ip address in the subnet

    return int_to_dotquad(broadcast_int)
