# Inspyred Memos

A note-taking application built with Python featuring a client-server architecture with user authentication, encrypted database storage, and a PySimpleGUI-based client interface.

## Features

- **Client-Server Architecture**: Socket-based communication for memo transmission
- **User Authentication**: Secure password hashing with bcrypt
- **Database Encryption**: SQLAlchemy ORM with Fernet encryption for sensitive data
- **GUI Client**: PySimpleGUI-based interface for easy memo creation and sending
- **Email Verification**: Token-based email verification system for user accounts
- **Cross-Platform**: Supports Windows, Linux, and macOS

## Requirements

- Python 3.11 or higher
- Poetry (for dependency management) or pip

## Installation

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

# Install dependencies
pip install -r requirements.txt  # or install from pyproject.toml
pip install pysimplegui bcrypt sqlalchemy cryptography platformdirs rich keyring itsdangerous inspy-logger
```

## Configuration

### Environment Variables

For production use, set the following environment variables:

```bash
# Secret key for email verification tokens (REQUIRED for production)
export INSPYRED_MEMOS_SECRET_KEY="your-secret-key-here"

# Optional: Database configuration
export INSPYRED_MEMOS_DB_URL="sqlite:///path/to/your/database.db"
```

### Directory Structure

The application uses platform-specific directories for configuration, data, and logs:

- **Linux**: `~/.local/share/InspyredMemosServer/`, `~/.config/InspyredMemosServer/`, `~/.local/state/InspyredMemosServer/log/`
- **macOS**: `~/Library/Application Support/InspyredMemosServer/`, etc.
- **Windows**: `%LOCALAPPDATA%\InspyredMemosServer\`, etc.

## Usage

### Starting the Server

```python
from inspyred_memo_server import MemoServer

# Create and start the server (default: localhost:65432)
server = MemoServer()
server.start()

# Or specify custom host and port
server = MemoServer(host='0.0.0.0', port=8080)
server.start()
```

**Command line:**

```bash
python -m inspyred_memo_server
```

### Using the GUI Client

```python
from inspyred_memo_client import MemoClientWindow

# Create and run the client window
client = MemoClientWindow(host='127.0.0.1', port=65432, auto_build=True)
client.run()
```

**Command line:**

```bash
python -m inspyred_memo_client
```

The GUI client provides:
- Text input field for memo entry
- Send button to transmit memos to the server
- Exit button to close the application

### Working with Users

```python
from inspyred_memo_server.database.user import User, Base, sessionmaker
from sqlalchemy import create_engine

# Create database engine and session
engine = create_engine('sqlite:///memos.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user
user = User()
user.username = "john_doe"
user.set_password("SecurePassword123!")

# Add to database
session.add(user)
session.commit()

# Verify password
if user.check_password("SecurePassword123!"):
    print("Password correct!")
```

### Email Verification

```python
from inspyred_memo_server.database.email import UserVerification

# Initialize with SMTP settings
verifier = UserVerification(
    mail_server='smtp.gmail.com',
    mail_port=587,
    mail_user='your-email@gmail.com',
    mail_password='your-app-password',
    verification_url_base='http://yourapp.com/verify'
)

# Generate verification token
token = verifier.generate_verification_token('user@example.com')

# Send verification email
verifier.send_verification_email('user@example.com', token)

# Verify token (valid for 1 hour by default)
email = verifier.verify_token(token)
if email:
    print(f"Token valid for: {email}")
else:
    print("Token invalid or expired")
```

### Configuration Management

```python
from inspyred_memo_server.config.dirs import APP_DIRS
from inspyred_memo_server.log_engine.config import LogConfig

# Access application directories
print(f"Data directory: {APP_DIRS.data_dir}")
print(f"Config directory: {APP_DIRS.config_dir}")
print(f"Log directory: {APP_DIRS.log_dir}")

# Configure logging
log_config = LogConfig(log_level='DEBUG')
print(f"Log file: {log_config.log_file_path}")
```

## Project Structure

```
InspyredMemos/
├── inspyred_memo_server/       # Server-side components
│   ├── __init__.py            # MemoServer class
│   ├── database/              # Database models and encryption
│   │   ├── user/              # User authentication
│   │   ├── email.py           # Email verification
│   │   └── crypt/             # Database encryption
│   ├── config/                # Configuration management
│   │   ├── dirs/              # Directory management
│   │   └── email.py           # Email configuration
│   ├── log_engine/            # Logging configuration
│   ├── errors/                # Custom exceptions
│   └── utils/                 # Utility functions and decorators
│
├── inspyred_memo_client/       # GUI client
│   └── __init__.py            # MemoClientWindow class
│
├── pyproject.toml             # Project dependencies
└── README.md                  # This file
```

## Security Notes

- **Passwords**: User passwords are hashed using bcrypt before storage
- **Database**: Sensitive data is encrypted using Fernet encryption with keys stored in system keyring
- **Email Verification**: Tokens are time-limited (1 hour default) and cryptographically signed
- **SMTP Credentials**: Store SMTP passwords in environment variables, not configuration files
- **Secret Keys**: Always set `INSPYRED_MEMOS_SECRET_KEY` environment variable in production

## Development

### Running Tests

```bash
# No test suite currently implemented
# Tests will be added in future releases
```

### Code Style

The project follows Python best practices:
- Type hints where applicable
- Comprehensive docstrings
- Secure coding practices (validated with CodeQL)

## Troubleshooting

### Keyring Errors

If you encounter keyring-related errors:

```bash
# Install a keyring backend
pip install keyrings.alt
```

### Import Errors

Ensure all dependencies are installed:

```bash
poetry install
# or
pip install -e .
```

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Please ensure:
- Code follows existing style conventions
- Security best practices are maintained
- Documentation is updated for new features

## Author

**Taylor B.** (tayjaybabee@gmail.com)  
**Inspyre Softworks**

## Version

Current version: **0.1.0** (Development Release)
