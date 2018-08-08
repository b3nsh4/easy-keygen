#!usr/bin/python3

import os
import sys
import argparse
from cryptography.hazmat.primitives import serialization as key_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend as easy_backend

GNU nano 2.9.8                                                                                         banner.py

#somecolors
lightgreen='\033[92m'
clear ='\033[0m'
print(lightgreen+"""


 +-+-+-+-+-+-+-+-+-+-+-+
 |e|a|s|y|-|k|e|y|g|e|n|
 +-+-+-+-+-+-+-+-+-+-+-+
               by-bensh4

""")

rsa_key=rsa.generate_private_key(
    backend=easy_backend(), #its default_backend itself!
    public_exponent=65537,  #default and suggested exponent
    key_size=2048
    )

dsa_key=dsa.generate_private_key(
    backend=easy_backend(),
    key_size=2048
    )

#now serializing the keys generated!

rsa_private_key=rsa_key.private_bytes(
    key_serialization.Encoding.PEM,
    key_serialization.PrivateFormat.PKCS8,
    key_serialization.NoEncryption()
    )


'''
AT ANY POINT IF YOU WANT TO ADD A PASSPHRASE EXPLICITLY TO YOUR KEY,
YOU COULD ADD IT BY REPLACING 'key_serialization.NoEncryption' ABOVE WITH
'key_serialization.BestAvailableEncryption(b'giveapassword')'

SINCE WE ARE USING PKCS8 HERE,IF YOU STILL ENCRYPT THE PRIVATE_KEY,
IT WOULD BE IN THIS FORMAT.

-----BEGIN ENCRYPTED PRIVATE KEY-----
     BASE64 ENCODED DATA
-----END ENCRYPTED PRIVATE KEY-----

FOR MORE ABOUT PKCS ENCODING: https://tls.mbed.org/kb/cryptography/asn1-key-structures-in-der-and-pem

'''


dsa_private_key=dsa_key.private_bytes(
    key_serialization.Encoding.PEM,
    key_serialization.PrivateFormat.PKCS8,
    key_serialization.NoEncryption()
    )


'''
NOW WE ARE GENERATING THE PUBLIC KEYS ONE BY ONE.
LET'S FIRST MAKE RSA'''


rsa_public_key=rsa_key.public_key().public_bytes(
    key_serialization.Encoding.PEM,
    key_serialization.PublicFormat.SubjectPublicKeyInfo
    )

#DSA public_key

dsa_public_key=dsa_key.public_key().public_bytes(
    key_serialization.Encoding.PEM,
    key_serialization.PublicFormat.SubjectPublicKeyInfo
    )


'''
NOW WE ARE GOING TO GENERATE PUBLICKEYS IN OPENSSH FORMAT.

'''

rsa_openssh_pub_key=rsa_key.public_key().public_bytes(
    key_serialization.Encoding.OpenSSH,
    key_serialization.PublicFormat.OpenSSH
    )

'''

DSA IN OPENSSH FORMAT

'''

dsa_openssh_pub_key=dsa_key.public_key().public_bytes(
    key_serialization.Encoding.OpenSSH,
    key_serialization.PublicFormat.OpenSSH
    )
#print(dsa_openssh_pub_key)

print(help(dsa_openssh_pub_key))


'''
CURRENTLY THIS SCRIPT IS IN BETA STAGE.BUT YOU COULD GO AHEAD
AND GENERATE THE KEYS THAT YOU NEED.BTW IF YOU FACE ANY WARPPING 
PROBLEMS IN LINE;YOU COULD PARSE IT BY USING

                with open('file.txt','wb') as writer:
                   for parse in the key:
                      writer.write(i+str.encode('\n')

NOW THIS WOULD FIX THE WARPPING.

THIS TOOL IS STILL UNDER DEVELOPMENT.FEEL FREE TO CONTRIBUTE! :-) 
'''
