# InspyredMemos

A lightweight, client-server memo application for quick note-taking and message sharing.

## Overview

InspyredMemos is a simple yet effective memo application that consists of two main components:

- **Server**: A socket-based server that receives, stores, and manages memos
- **Client**: A user-friendly GUI application for creating and sending memos to the server

## Features

- 🚀 **Simple Architecture**: Clean client-server design using Python sockets
- 🖥️ **Cross-Platform GUI**: Built with PySimpleGUI for consistent experience across platforms
- 🔒 **Secure**: Includes cryptography and authentication capabilities
- 📝 **Real-time**: Instant memo transmission from client to server
- 🗃️ **Database Support**: SQLAlchemy integration for persistent storage
- 📁 **Smart Configuration**: Automatic directory management and configuration handling

## Installation

### Prerequisites

- Python 3.11 or higher
- Poetry (recommended) or pip

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/tayjaybabee/InspyredMemos.git
cd InspyredMemos

# Install dependencies
poetry install

# Activate the virtual environment
poetry shell
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/tayjaybabee/InspyredMemos.git
cd InspyredMemos

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Usage

### Starting the Server

The memo server listens for incoming connections and stores received memos.

```python
from inspyred_memo_server import MemoServer

# Create and start server with default settings (127.0.0.1:65432)
server = MemoServer()
server.start()

# Or customize host and port
server = MemoServer(host='0.0.0.0', port=8080)
server.start()
```

**Command line usage:**

```bash
# Start server with default settings
python -m inspyred_memo_server

# Or run directly
python inspyred_memo_server/__init__.py
```

### Using the Client

The client provides a simple GUI for sending memos to the server.

```python
from inspyred_memo_client import MemoClientWindow

# Create and run client with auto-build
client = MemoClientWindow(auto_build=True)
client.run()

# Or customize server connection
client = MemoClientWindow(host='192.168.1.100', port=8080, auto_build=True)
client.run()
```

**Command line usage:**

```bash
# Start client GUI
python -m inspyred_memo_client

# Or run directly
python inspyred_memo_client/__init__.py
```

### Client GUI Instructions

1. **Enter Memo**: Type your memo in the text input field
2. **Send**: Click the "Send" button to transmit your memo to the server
3. **Exit**: Click "Exit" to close the application

## Configuration

InspyredMemos automatically manages configuration directories and files using the `AppDirs` class. The application will create necessary directories for:

- Configuration files
- Cache data
- Log files
- User data

Default locations follow platform conventions:
- **Linux/macOS**: `~/.local/share/InspyredMemos/`, `~/.config/InspyredMemos/`
- **Windows**: `%APPDATA%\InspyredMemos\`, `%LOCALAPPDATA%\InspyredMemos\`

## Dependencies

Core dependencies include:

- **PySimpleGUI** (^5.0.3): GUI framework for the client application
- **SQLAlchemy** (^2.0.28): Database ORM for memo storage
- **bcrypt** (^4.1.2): Password hashing and authentication
- **cryptography** (^42.0.5): Encryption and security features
- **platformdirs** (^4.2.0): Cross-platform directory management
- **rich** (^13.7.1): Enhanced terminal output and formatting
- **keyring** (^24.3.1): Secure credential storage
- **itsdangerous** (^2.1.2): Secure data serialization
- **inspy-logger** (3.0.3): Advanced logging capabilities

## Development

### Project Structure

```
InspyredMemos/
├── inspyred_memo_server/          # Server implementation
│   ├── __init__.py               # Main server class
│   ├── config/                   # Configuration management
│   ├── database/                 # Database models and handlers
│   ├── utils/                    # Utility functions and helpers
│   └── ...
├── inspyred_memo_client/          # Client implementation
│   └── __init__.py               # GUI client application
├── pyproject.toml                # Project dependencies and metadata
└── README.md                     # This file
```

### Running Tests

```bash
# With Poetry
poetry run pytest

# With pip
python -m pytest
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Version

Current version: **1.0.0-dev.1**

## License

This project is developed by Inspyre Softworks. For licensing information, please contact the authors.

## Authors

- **Inspyre Softworks** - [https://inspyre.tech](https://inspyre.tech)
- **Taylor-Jayde Blackstone** - <t.blackstone@inspyre.tech>

## Links

- **Documentation**: [https://InspyredMemos.readthedocs.io/en/latest](https://InspyredMemos.readthedocs.io/en/latest)
- **PyPI Package**: [https://pypi.org/project/InspyredMemos](https://pypi.org/project/InspyredMemos)
- **GitHub Repository**: [https://github.com/Inspyre-Softworks/](https://github.com/Inspyre-Softworks/)

## Support

For support, bug reports, or feature requests, please open an issue on the GitHub repository or contact the development team at Inspyre Softworks.

---

*Built with ❤️ by the Inspyre Softworks team*