# Chat Server

## Overview

This repository contains a **Chat Server** implementation in Python, featuring both terminal and GUI-based versions. The chat server allows multiple clients to communicate with each other via a centralized server. The terminal implementation uses dynamic command-line features, while the GUI version provides an intuitive graphical interface.

## Features

1. **Terminal Version**:
   - Interactive chat using the terminal.
   - Enhanced display with colors and effects (using the `termcolor` library).
   - Fully documented with `pydoc` for `server.py` and `client.py`.

2. **GUI Version**:
   - User-friendly graphical interface for chat.
   - Simplified interactions for non-technical users.

3. **Multi-Client Communication**:
   - Supports multiple clients connected to a single server.

## Project Structure

```
├── gui_version               # Contains the GUI-based chat implementation
│   ├── client_gui.py         # GUI client-side code
│   ├── server_gui.py         # GUI server-side code
│
├── terminal_version          # Contains the terminal-based chat implementation
│   ├── client_terminal.py    # Terminal client-side code
│   ├── server_terminal.py    # Terminal server-side code
│   ├── pydoc_server.py       # Pydoc documentation for server
│   ├── pydoc_client.py       # Pydoc documentation for client
```

## Prerequisites

- Python 3.x
- `termcolor` library (for terminal version):
  ```bash
  pip install termcolor
  ```

## Installation and Usage

### Clone the Repository
```bash
git clone https://github.com/kevincogan/Chat_Server.git
cd Chat_Server
```

### Terminal Version
1. Navigate to the `terminal_version` directory:
   ```bash
   cd terminal_version
   ```
2. Start the server:
   ```bash
   python server_terminal.py
   ```
3. Start the client(s):
   ```bash
   python client_terminal.py
   ```

### GUI Version
1. Navigate to the `gui_version` directory:
   ```bash
   cd gui_version
   ```
2. Start the server:
   ```bash
   python server_gui.py
   ```
3. Start the client(s):
   ```bash
   python client_gui.py
   ```

## Videos

### Terminal Version
- [Part 3 Terminal Video](https://drive.google.com/file/d/176DYRfAwk7PdeWFtLVPIfyxeHT7gS5JA/view?usp=sharing)
- [Part 4 Terminal Video](https://drive.google.com/file/d/1mV55u_VQvJE3-90H-guwQikYfCPC5p0A/view?usp=sharing)

### GUI Version
- [Part 3 GUI Video](https://drive.google.com/file/d/1YfGhSzMa6jPVp96jTfZO_rQWCE1h9bP_/view?usp=sharing)
- [Part 4 GUI Video](https://drive.google.com/file/d/1mV55u_VQvJE3-90H-guwQikYfCPC5p0A/view?usp=sharing)

## Dependencies

- **`termcolor`**: Provides text color and dynamic effects for terminal display.
  Install it with:
  ```bash
  pip install termcolor
  ```

## Notes

- The `pydoc` documentation for the terminal version is separated from the main codebase.
- Both versions are designed to work on local networks.

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and push them to your fork.
4. Open a pull request describing your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Experience seamless chat with this Python-based Chat Server implementation. Happy chatting!

