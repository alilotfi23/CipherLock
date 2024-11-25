# CipherLock

CipherLock is a simple yet secure command-line password manager written in Python. It helps you safely store, retrieve, and manage your passwords by encrypting sensitive information.

## Features

- **Secure Password Storage**: Encrypts passwords using symmetric encryption to ensure security.
- **Add New Passwords**: Save usernames and passwords for various websites or services.
- **Retrieve Passwords**: Quickly access stored passwords.
- **List Accounts**: View all stored account entries.
- **Delete Passwords**: Remove passwords when no longer needed.
- **Master Password Protection**: Access all features with a master password.

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/alilotfi23/CipherLock.git
   cd cipherlock
   ```

2. **Install Dependencies**

   Install the required Python libraries using pip:

   ```bash
   pip install cryptography
   ```

## Usage

1. **Run the Password Manager**

   Execute the script from the command line:

   ```bash
   python cipherlock.py
   ```

2. **Interact with CipherLock**

   After running the script, you will be prompted to enter your master password. Once entered, you can choose from the following options:

   - **Add a New Password**: Enter the website, username, and password to store them securely.
   - **Retrieve a Password**: Enter the website to fetch the username and decrypted password.
   - **List All Accounts**: Display all stored websites/accounts.
   - **Delete a Password**: Enter the website to remove the associated entry.
   - **Quit**: Exit the password manager.

3. **Master Password**

   Upon launching the application, you will be prompted to enter a master password. This master password is required to access and manage your stored passwords.

## Security Considerations

- **Key File**: An encryption key is stored in `key.key`. Ensure this file is kept secure, as it is essential for decrypting your passwords.
- **Data File**: Passwords are stored in `passwords.json` in an encrypted format. Protect this file from unauthorized access.
- **Master Password**: Implement additional measures, such as hashing and secure storage, for the master password in a production environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve CipherLock.
