import pytest

from calculator import *


@pytest.mark.parametrize("maybe_valid_ip, expected_result", [
    ("192.168.2.108", True),
    ("255.255.240.0", True),
    ("10.0.256.10", False),
    ("10.300.0.0", False),
    ("10.-1.0.0", False),
    ("a.b.c.d", False),
    ("10.0.0", False),
])

def test_is_ipv4_address(maybe_valid_ip, expected_result):
    assert is_ipv4_address(maybe_valid_ip) == expected_result


@pytest.mark.parametrize("random_ip_addr, subnet_mask, expected_result", [
    ("192.168.2.108", "255.255.0.0", "192.168.0.0"),
    ("10.1.230.10", "255.255.255.0", "10.1.230.0"),
    ("172.18.1.15", "255.240.0.0", "172.16.0.0"),
    ("10.10.0.0", "255.0.0.0", "10.0.0.0"),
])

def test_calculate_network_addr(random_ip_addr, subnet_mask, expected_result):
    assert calculate_network_addr(random_ip_addr, subnet_mask) == expected_result


@pytest.mark.parametrize("host_size, expected_result", [
    (1, "255.255.255.255"),
    (128, "255.255.255.128"),
    (256, "255.255.255.0"),
    (65536, "255.255.0.0"),
    (2**20, "255.240.0.0"),
    (4294967296, "0.0.0.0"),
])

def test_host_size_to_subnet_mask(host_size, expected_result):
    assert host_size_to_subnet_mask(host_size) == expected_result


@pytest.mark.parametrize("network_addr, subnet_mask, expected_result", [
    ("192.168.0.0", "255.255.0.0", "192.168.255.255"),
    ("10.1.230.0", "255.255.255.0", "10.1.230.255"),
    ("172.16.0.0", "255.240.0.0", "172.31.255.255"),
    ("10.00.0.0", "255.0.0.0", "10.255.255.255"),
])

def test_get_broadcast_addr(network_addr, subnet_mask, expected_result):
    assert get_broadcast_addr(network_addr, subnet_mask) == expected_result


@pytest.mark.parametrize("ip_addr_1, subnet_mask, ip_addr_2, expected_result", [
    ("192.168.10.25", "255.255.0.0", "192.168.255.5", True),
    ("10.1.230.3", "255.255.255.0", "10.1.230.35", True),
    ("172.18.7.250", "255.240.0.0", "172.24.94.25", True),
    ("10.64.5.67", "255.224.0.0", "10.19.14.28", False),
])

def test_get_broadcast_addr(ip_addr_1, subnet_mask, ip_addr_2, expected_result):
    assert check_same_network(ip_addr_1, subnet_mask, ip_addr_2) == expected_result