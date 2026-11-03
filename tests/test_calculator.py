from src.calculator import *

def test_ipv4_mask_length():
    assert ipv4_mask_len("255.255.255.255") == 32, "Incorrect calculation o fsubnet mask length."
    assert ipv4_mask_len("255.255.255.0") == 24, "Incorrect calculation o fsubnet mask length."
    assert ipv4_mask_len("255.255.224.0") == 19, "Incorrect calculation o fsubnet mask length."
    assert ipv4_mask_len("255.128.0.0") == 9, "Incorrect calculation o fsubnet mask length."
    assert ipv4_mask_len("0.0.0.0") == 0, "Incorrect calculation o fsubnet mask length."

def test_host_size():
    assert get_host_size(32) == 1, "Not calculating correct number of hosts!"
    assert get_host_size(24) == 256, "Not calculating correct number of hosts!"
    assert get_host_size(19) == 8192, "Not calculating correct number of hosts!"
    assert get_host_size(13) == 524288, "Not calculating correct number of hosts!"
    assert get_host_size(0) == 4294967296, "Not calculating correct number of hosts!"

if __name__ == "__main__":
    test_ipv4_mask_length()
    test_host_size()