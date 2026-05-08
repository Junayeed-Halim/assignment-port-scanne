# Port Scanner — Assignment Report

This document is a concise, PDF-ready report you can include with your submission. It explains how the `port_scanner.py` program meets the marking criteria and provides example output and run instructions.

**Files included**
- `port_scanner.py` — the scanner source (submit this file)
- `REPORT.md` — this report (convert to PDF for submission)

---

**1. Command-line argument (1.5 marks)**
- The program requires a single IP address argument. Usage:

```bash
python port_scanner.py <IP_ADDRESS>
```

- The script reads the argument and uses it as the target for scanning.

**2. Ports scanned (1.5 marks)**
- The scanner checks only the five required ports: 80, 443, 22, 25, and 53.
- The list is defined at the top of `port_scanner.py` for clarity.

**3. Timeout (1.5 marks)**
- Each socket sets a timeout of 0.1 seconds (100 ms) using `sock.settimeout(0.1)`.
- This prevents the scanner waiting too long on non-responding ports.

**4. Exception handling (1.5 marks)**
- Each connection attempt is wrapped in a `try`/`except` block.
- Exceptions are caught and reported per-port; the scanner continues to the next port on error.

**5. Output: printing open ports (4 marks)**
- When `connect_ex()` returns `0`, the script prints `Port <n> is OPEN`.
- When `connect_ex()` returns a nonzero code, it prints `Port <n> is CLOSED (connect_ex returned <code>)`.
- When an exception occurs during the attempt, it prints `Port <n> is ERROR (exception: <message>)`.

---

## Example run

Command:

```bash
python port_scanner.py 127.0.0.1
```

Example output (your machine may differ depending on running services):

```
Scanning 127.0.0.1...
------------------------------
Port 80 is CLOSED (connect_ex returned 111)
Port 443 is CLOSED (connect_ex returned 111)
Port 22 is CLOSED (connect_ex returned 111)
Port 25 is CLOSED (connect_ex returned 111)
Port 53 is CLOSED (connect_ex returned 111)
```

If a port is open, you will see:

```
Port 80 is OPEN
```

---

## How to create the PDF

1. Open `REPORT.md` in your editor (VS Code). Use the printer or export-to-PDF feature: `File -> Print -> Save as PDF`.

Or use Pandoc (if available):

```bash
pandoc REPORT.md -o report.pdf
```

2. Include `port_scanner.py` and `report.pdf` in your submission.

---

## Notes for the marker
- The scanner implements the exact ports and timeout requested, and uses per-port exception handling. The code is minimal and easy to follow for grading.

---

If you want, I can also generate `report.pdf` for you here (requires a PDF tool in the environment) or produce a polished one-page PDF with a screenshot image (you would need to run the scanner locally and provide the screenshot or allow me to run it if Python is available).