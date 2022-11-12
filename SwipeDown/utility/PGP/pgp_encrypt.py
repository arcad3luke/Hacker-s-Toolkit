import gnupg
import os

gpg = gnupg.GPG('./gpg')

path = './file_to_encrypt'
file = './file.txt'

with open(path + file, 'rb') as f:
    status = gpg.encrypt_file(f, ['Hacker\'s Toolkit'], output=path + file + '.encrypted')

print(status.ok)
print(status.stderr)