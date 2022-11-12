import gnupg
import os

gpg = gnupg.GPG('./gpg')
gpg.encoding = 'utf-8'

key_input = gpg.gen_key_input(
    name_email = 'Hacker\'s Toolkit',
    passphrase = 'Hacker\'s Toolkit',
    key_type = 'RSA',
    key_length = 4096
)

key = gpg.gen_key(key_input)

print(key)