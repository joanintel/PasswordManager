#PSD Manager - CLI Password Manager

A secure, encrypted command-line password manager written in Python. Store, retrieve, and manage your passwords with military-grade encryption.

##Features

- **AES-256-GCM Encryption** - Industry standard authenticated encryption
- **PBKDF2 Key Derivation** - 200,000 iterations to resist brute-force attacks
- **Session Caching** - Stay authenticated for 10 minutes (configurable)
- **Password Generation** - Create strong, random passwords
- **Clipboard Integration** - Copy passwords without displaying on screen
- **Vault Statistics** - Analyze password strength across your vault
- **Master Password Change** - Re-encrypt entire vault with new key
- **Zero Knowledge** - Master password never stored anywhere

## Installation

# Clone the repository
git clone  https://github.com/joanintel/PasswordManager 
cd PasswordManager

# Install dependencies
pip install pyperclip pycryptodome

# Make it executable (optional)
chmod +x pm
