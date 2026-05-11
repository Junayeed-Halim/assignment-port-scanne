import socket
import sys

# The ports we need to scan (as required by the assignment)
ports = [80, 443, 22, 25, 53]

# Check that the user provided an IP address as a command-line argument
if len(sys.argv) != 2:
	print("Usage: python port_scanner.py <IP address>")
	sys.exit(1)

ip_address = sys.argv[1]

print(f"Scanning {ip_address}...")
print("-" * 30)

for port in ports:
	try:
		# Create a new socket for each port
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# Set timeout to 100ms (0.1 seconds)
		sock.settimeout(0.1)

		# Try to connect; success means the port is open
		sock.connect((ip_address, port))
		print(f"Port {port} is OPEN")
	except Exception as e:
		# Connection failed — report exception
		print(f"Port {port} is CLOSED (exception: {e})")
	finally:
		try:
			sock.close()
		except Exception:
			pass
