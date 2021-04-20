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
