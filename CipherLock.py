from cryptography.fernet import Fernet
import os
import json
import getpass

class PasswordManager:
    def __init__(self, key_file='key.key', data_file='passwords.json'):
        self.key_file = key_file
        self.data_file = data_file
        self.key = self.load_key()
        self.fernet = Fernet(self.key)
        self.data = self.load_data()

    def load_key(self):
        """Load the encryption key from a file or generate a new one."""
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key
        else:
            with open(self.key_file, 'rb') as f:
                return f.read()

    def load_data(self):
        """Load the password data from a file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self):
        """Save the password data to a file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def encrypt(self, plaintext):
        """Encrypt a plaintext string."""
        return self.fernet.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        """Decrypt a ciphertext string."""
        return self.fernet.decrypt(ciphertext.encode()).decode()

    def add_password(self, website, username, password):
        """Add a new password entry."""
        encrypted_password = self.encrypt(password)
        self.data[website] = {
            'username': username,
            'password': encrypted_password
        }
        self.save_data()
        print(f"Password for {website} added.")

    def get_password(self, website):
        """Retrieve a password entry."""
        if website in self.data:
            encrypted_password = self.data[website]['password']
            username = self.data[website]['username']
            decrypted_password = self.decrypt(encrypted_password)
            print(f"Website: {website}")
            print(f"Username: {username}")
            print(f"Password: {decrypted_password}")
        else:
            print(f"No password found for {website}.")

    def list_accounts(self):
        """List all stored account names."""
        if self.data:
            print("Stored accounts:")
            for website in self.data.keys():
                print(f"- {website}")
        else:
            print("No stored accounts.")

    def delete_password(self, website):
        """Delete a password entry."""
        if website in self.data:
            del self.data[website]
            self.save_data()
            print(f"Password for {website} deleted.")
        else:
            print(f"No password found for {website}.")

def main():
    master_password = getpass.getpass("Enter your master password: ")
    # In a real application, you would securely verify the master password.

    manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. List all accounts")
        print("4. Delete a password")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password: ")
            manager.add_password(website, username, password)
        elif choice == '2':
            website = input("Enter the website: ")
            manager.get_password(website)
        elif choice == '3':
            manager.list_accounts()
        elif choice == '4':
            website = input("Enter the website: ")
            manager.delete_password(website)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
