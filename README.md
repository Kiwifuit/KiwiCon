# KiwiCon
A console program (originally made in Batch) reworked because I am not advanced in Batch

# Hello there!
Hello. And welcome to this GitHub repo.

This time, instead of writing the software and then creating a repo, I will update the repo as I go along with this project.

In case you are wondering, the day I am writing this part is April 20, 2021, and this is day one

Day One
-----------------
Day one. Everything gotta start with something.

I started with creating the functions that I'll need. `morse.py` and `hash.py` for now.

Also, I just learned about `argparse` so yea

So this is the code for `morse.py`. I will make `hash.py` later:
```py
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
```
_You were expecting beautiful and organized Python Code, but it was me, Dirty, Programmer-style code_

So, if you know your stuff and understand what that code does, good, then cool.
For those people who don't, this is what it does:
```
>> Gets that little dude called "argparse"
>> Gets another little dude called "morse_code" and yes, it converts plaintext to morse. I am only doing this bc nostalgia
>> Make variable called "parser" and give it the fucking ArgumentParser thingy. This is the "root" of the program to which arguments (not the irl ones bc those are stupid as fuck) are made
>> [The three lines below it] basically mean that we take "parser, the ArgumentParser of the west" and load a couple arguments so our program has a purpose unlike us
>> Make variable "args" and parse "parser"
```
Now, I can hear your brain go _But Kiwi, why `if args.encode:`?_

Well, since we made this little boi called `args` earlier, yeah? Well Mr.`args` here is now the captain, so yea.
Basically, as far as a 13-year old's brain can handle, `args.encode` is there because:
a) I made it so that if `-e` or `--encode` is passed it passes a `True`, then it encode. Else, decode. `encodeDecode` is just for saif n stuff but hey, Python is [multi-paradigm](https://askinglot.com/what-is-meant-by-multi-paradigm)

And umm yea, I got school . So I gotta update the repo quick or me mom go kill kill.

Ight cya

Edit: I also forgot that I already have the source for the console, so yea

now **cya**

Edit Edit: Thank you to my buddy (not gonna name him ofc) for pointin a _minor_ flaw in this README.

_How many times do I have to "cya" before I can **actually** get out of here?_

Day Two
---------
Today's another day (at least for me lol)

So that means another day of Documentation/Journal thingy idk

So for today, I started learning Lua (LMAOOOO). I haven't changed the repo much.

But I am motivated so yea...I brought the `hash.py` file I talked about yesterday and decided: _More Doctor's Code, please_ so I did just that:
```py
import argparse
import hashlib
hasher = argparse.ArgumentParser(prog="hash.exe", description="Hashing Algorithms bundled into one file", )
hasher.add_argument("-t", "--type", type=int, help="Type of hashing algorithm you want to use")
hasher.add_argument("text", help="The text you want to encrypt/hash")

args = hasher.parse_args()
```
__Of course__ it's not yet done. I still got some of that keystrokes left, brb in a while...

Back! And I have a plan  thingy with this one:
```
0 = shake_128
1 = shake_256
2 = BLAKE2b (x64 OSs)
3 = BLAKE2s (x86 OSs)
4 = SHA-1
5 = SHA-256 (Parkour)
6 = SHA-512 (EXTRA Parkour)
7 = Base16
8 = Base32
9 = Base64
```

Yeah, that is some complex plan. Better start working on it...

Hello and I am back lol. This is genuinely the most scared I am getting (I think):
```py
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
```

All I know what this does is that for `hashlib`, I hash using hash algorithm, then digest it???? I dunno

For `Base64`, All I know is only recieved from [the module's documentation](https://docs.python.org/3/library/base64.html).

Also, forgot to say at this point but I'm using VSCode from the start of the `Day Two` header. And that's because I got [GitHub for Desktop](https://desktop.github.com)

Anyways, I got that luchies to take, so cya later in the afternoon when I got the time I guess

# Day three
Yeah, I know that I haven't updated this repo for a while, sorry about that.

I got a ton of stuff going on irl so please wait for a while I guess I dunno really...

Just wannna tell you that I'll be back in a while, no coding stuff for today. Also I got special examinations for today since I scored low in some of my subjects and I'd like to make said subject's grades higher or something idk wtf im talking about