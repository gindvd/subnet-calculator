import pytest

from calculator import *

@pytest.mark.parametrize("maybe_valid_ip, expected_result", [
    ("192.168.2.108", True),
    ("255.255.240.0", True),
    ("10.0.256.10", False),
    ("10.-1.0.0", False),
    ("a.b.c.d", False),
    ("10.0.0", False),
])

def test_is_ipv4_address(maybe_valid_ip, expected_result):
    assert is_ipv4_address(maybe_valid_ip) == expected_result


@pytest.mark.parametrize("random_ip_addr, subnet_mask, expected_result", [
    ("192.168.2.108", "255.255.0.0", "192.168.0.0"),
    ("10.10.0.0", "255.0.0.0", "10.0.0.0"),
    ("10.1.256.10", "255.255.255.0", "10.1.256.0"),
    ("172.18.1.15", "255.255.240.0", "172.16.0.0"),

])

def test_calculate_network_addr(random_ip_addr, subnet_mask, expected_result):
    assert calculate_network_addr(random_ip_addr, subnet_mask) == expected_result