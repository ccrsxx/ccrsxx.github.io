import os
import secrets
import subprocess

class License:

    def __init__():
        os.chdir(os.getenv('userprofile') + 'Desktop\ccrsxx.github.io')
    
    @staticmethod
    def create_keys(keys=secrets.token_urlsafe(16)):
        with open('random.txt', 'w') as f:
            f.write(keys)
        subprocess.call(["git", "acp", f'adding {keys} to database'])

    @staticmethod
    def del_keys():
        with open('random.txt', 'w') as f:
            pass
        subprocess.call(["git", "acp", f'removing all keys from database'])

