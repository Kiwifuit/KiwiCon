import argparse
import hashlib
import base64
hasher = argparse.ArgumentParser(prog="hash.exe", description="Hashing Algorithms bundled into one file", )
hasher.add_argument("-t", "--type", type=int, help="Type of hashing algorithm you want to use")
hasher.add_argument("text", help="The text you want to encrypt/hash")

args = hasher.parse_args()
if args.type == 0:
    msg = hashlib.shake_128(args.text).hexdigest()
if args.type == 1:
    msg = hashlib.shake_256(args.text).hexdigest()
if args.type == 2:
    msg = hashlib.blake2b(args.text).hexdigest()
if args.type == 3:
    msg = hashlib.blake2s(args.text).hexdigest()
if args.type == 4:
    msg = hashlib.sha1(args.text).hexdigest()
if args.type == 5:
    msg = hashlib.sha256(args.text).hexdigest()
if args.type == 6:
    msg = hashlib.sha512(args.text).hexdigest()
if args.type == 7:
    msg = base64.b16encode(args.text)
if args.type == 8:
    msg = base64.b32encode(args.text)
if args.type == 9:
    msg = base64.b64encode(args.text)
print(msg)