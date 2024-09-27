# Add necessary python library
from cryptography.fernet import Fernet  # Importing Fernet encryption from cryptography library
import os  # Importing os module for file operations
import json  # Importing json module for JSON handling
import getpass  # Importing getpass module for secure password input

class PasswordManager:
    def __init__(self, key_file='key.key', data_file='passwords.json'):
        self.key_file = key_file  # File to store encryption key
        self.data_file = data_file  # File to store password data
        self.key = self.load_key()  # Loading encryption key
        self.fernet = Fernet(self.key)  # Creating Fernet instance with the key
        self.data = self.load_data()  # Loading password data from file

    def load_key(self):
        """Load the encryption key from a file or generate a new one."""
        if not os.path.exists(self.key_file):
            # Generate a new key if key file does not exist
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key
        else:
            # Load key from file if it exists
            with open(self.key_file, 'rb') as f:
                return f.read()

    def load_data(self):
        """Load the password data from a file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)  # Load JSON data from file
        return {}  # Return empty dictionary if file does not exist

    def save_data(self):
        """Save the password data to a file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)  # Save JSON data to file with indentation

    def encrypt(self, plaintext):
        """Encrypt a plaintext string."""
        return self.fernet.encrypt(plaintext.encode()).decode()  # Encrypt plaintext

    def decrypt(self, ciphertext):
        """Decrypt a ciphertext string."""
        return self.fernet.decrypt(ciphertext.encode()).decode()  # Decrypt ciphertext

    def add_password(self, website, username, password):
        """Add a new password entry."""
        encrypted_password = self.encrypt(password)  # Encrypt password
        self.data[website] = {
            'username': username,
            'password': encrypted_password
        }  # Store encrypted password with website and username
        self.save_data()  # Save updated data to file
        print(f"Password for {website} added.")  # Confirm password addition

    def get_password(self, website):
        """Retrieve a password entry."""
        if website in self.data:
            encrypted_password = self.data[website]['password']
            username = self.data[website]['username']
            decrypted_password = self.decrypt(encrypted_password)  # Decrypt stored password
            print(f"Website: {website}")
            print(f"Username: {username}")
            print(f"Password: {decrypted_password}")  # Print retrieved password
        else:
            print(f"No password found for {website}.")  # Handle if website not found

    def list_accounts(self):
        """List all stored account names."""
        if self.data:
            print("Stored accounts:")
            for website in self.data.keys():
                print(f"- {website}")  # Print each stored website
        else:
            print("No stored accounts.")  # Handle if no accounts are stored

    def delete_password(self, website):
        """Delete a password entry."""
        if website in self.data:
            del self.data[website]  # Delete password entry
            self.save_data()  # Save updated data to file
            print(f"Password for {website} deleted.")  # Confirm deletion
        else:
            print(f"No password found for {website}.")  # Handle if website not found

def main():
    master_password = getpass.getpass("Enter your master password: ")
    # In a real application, you would securely verify the master password.

    manager = PasswordManager()  # Create instance of PasswordManager

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. List all accounts")
        print("4. Delete a password")
        print("5. Quit")

        choice = input("Enter your choice: ")  # User menu choice input

        if choice == '1':
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password: ")  # Securely input password
            manager.add_password(website, username, password)  # Call method to add password
        elif choice == '2':
            website = input("Enter the website: ")
            manager.get_password(website)  # Call method to retrieve password
        elif choice == '3':
            manager.list_accounts()  # Call method to list all stored accounts
        elif choice == '4':
            website = input("Enter the website: ")
            manager.delete_password(website)  # Call method to delete password
        elif choice == '5':
            break  # Exit loop and end program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choice

if __name__ == "__main__":
    main()  # Call main function if script is executed directly
