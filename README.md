![Screenshot (782)](https://github.com/user-attachments/assets/64e4e4f7-b816-4c66-b1e5-7720d021cb4d)


## Project Firefly ✨

Project Firefly: A Swiss-Army Knife Payload Generator for Penetration Testing

Project Firefly is an innovative, menu-based software solution designed to streamline and enhance the effiency of reverse
shells generation for penetration testing. Firefly offers an intuitive interface that simplifies the creation of reverse shell 
payloads from its

- User-Friendly Interface

- Customizable Payload Options and Flexibility

- Rapid Deployment


## WARNING: Ethical Use of Project Firefly
Project Firefly is a tool designed to automate reverse shell generation for pentesting. Due to the Ngrok tunneling feature, please note 
that unauthorized usage of payloads is illegal, and this tool is designed for **educational** and **authorized testing purposes only**. 
It is strictly prohibited to use this tool to gain unauthorized access to computer systems, networks, data, or engage in any harmful actions. 
By using Project Firefly, you acknowledge that you are responsible for your own actions and agree to use this tool ethically and responsibly.


## Set Up 🛠️

1. Kali Linux VM 
2. Ngrok (not compulsary)

## Install and Set Up ngrok 🛠️
Install Ngrok for Linux here: **https://ngrok.com/download** (x86-64)
You will need to sign up for an account to get unique auth token

command to extract: sudo tar xvzf ~/Downloads/ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin

add the auth token: ngrok config add-authtoken "insert token here"

enable http tunnel: ngrok http "port number"

