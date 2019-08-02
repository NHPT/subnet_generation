# subnet_generation
You can enter standard subnet IP and segment, such as:

Python 3 subnet_generation.py 192.168.0.0/24 192.168.1.1-255, which can generate all IP in the range and write to the result.txt file; you can also enter irregular subnet IP such as:

Python 3 subnet_generation.py 192.168.1.123/24, which can correct the subnet to 192.168.1.0/24 and then generate all IP in the range;

You can input a lot of parameters, as long as they meet the requirements, such as:

Python 3 subnet_generation.py 192.168.0.0-128 123.123.123.12/24 10.10.200-255..
