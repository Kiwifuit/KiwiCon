import argparse
from morse_code import encrypt, decrypt
parser = argparse.ArgumentParser(prog="morse.exe", description="Encode Plaintext to Morse and Vise Versa", epilog="Note that either \"-d\" or \"-e\" or their verbose counterparts MUST be present")
parser.add_argument("-d", "--decode", help="Decodes Text", action="store_false")
parser.add_argument("-e", "--encode", help="Encodes text", action="store_true")
parser.add_argument("text", help="Text to be Encoded/Decoded")
args = parser.parse_args()
encodeDecode = args.text
if args.encode:
    print(encrypt(encodeDecode))
else:
    print(decrypt(encodeDecode))