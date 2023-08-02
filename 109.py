import os

user = os.getlogin()
os.system(f"net user {user} 456")
