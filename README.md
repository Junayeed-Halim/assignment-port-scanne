# Port Scanner Assignment

A simple TCP port scanner that checks if specific ports are open on a target IP address.

## Features

- **Command-line IP argument**: Pass the target IP address as a command-line argument
- **Fixed port list**: Scans only ports 80, 443, 22, 25, and 53 (HTTP, HTTPS, SSH, SMTP, DNS)
- **100ms timeout**: Sets a 0.1 second timeout for each connection attempt
- **Exception handling**: Uses try-catch blocks to handle connection failures
- **Clear output**: Displays which ports are open or closed with error details

## Usage

```bash
python port_scanner.py <IP_ADDRESS>
```

### Example

```bash
python port_scanner.py 127.0.0.1
```

### Example Output

```
Scanning 127.0.0.1...
------------------------------
Port 80 is CLOSED (exception: [Errno 111] Connection refused)
Port 443 is CLOSED (exception: [Errno 111] Connection refused)
Port 22 is CLOSED (exception: [Errno 111] Connection refused)
Port 25 is CLOSED (exception: [Errno 111] Connection refused)
Port 53 is CLOSED (exception: [Errno 111] Connection refused)
```

If a port is open (e.g., a web server running on port 8000):

```
Port 80 is OPEN
```

## Requirements Met

1. **Command-line argument**: IP address passed via `sys.argv[1]`
2. **Port scanning**: Scans only ports [80, 443, 22, 25, 53]
3. **Timeout**: Set to 0.1 seconds (100ms) per port
4. **Exception handling**: Uses try-catch to handle connection errors
5. **Output**: Prints open/closed status for each port

## How It Works

1. Validates that an IP address is provided as a command-line argument
2. For each port in the list:
   - Creates a new socket
   - Sets the timeout to 100ms
   - Attempts to connect using `connect_ex()`
   - Catches exceptions if the connection fails
   - Reports the port status