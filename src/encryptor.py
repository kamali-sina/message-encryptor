import os
import cryptocode
from sys import argv

ENCRYPT = ["-e", "--encrypt"]
DECRYPT = ["-d", "--decrypt"]
MAKEKEY = ["-mk", "--make-key"]
KEYNAME = "key.txt"
ENCODING = "UTF-8"

class Encyptor():
    def __init__(self, argv) -> None:
        if (len(argv) < 2):
            self.exit_with_help()
        self.init_key()
        self.command = argv[1]
        self.path = ""
        try:
            self.path = argv[2]
        except:
            pass
    
    def init_key(self):
        if (not os.path.exists(KEYNAME)):
            self.exit_no_key()
        with open (KEYNAME, "r") as file:
            self.key = file.read()

    def exit_with_help(self):
        print("usage:")
        print("\tpython3 encryptor.py --<encrypt|decrypt> <path to file>")
        exit()
    
    def exit_no_key(self):
        print("ERROR: no key was found. Place a key.txt file in the same directory as the encryptor to use.")
        print("HELP: to generate a key, use --make-key")
        exit()
    
    def exit_no_file(self):
        print("ERROR: file does not exist!")
        exit()
    
    def exit_invalid_key(self):
        print("ERROR: key file was invalid!")
        exit()
    
    def print_result(self, result, pretty=False):
        if (pretty):
            print("\n*****result*****\n")
            print(result)
            print("\n")
        else:
            print(result)
    
    def make_key(self):
        key = "somerandomkey"
        with open(KEYNAME, "wb") as file:
            file.write(key)
        print(f"key has been generated in {KEYNAME}")
    
    def encrypt(self):
        with open(self.path, "r") as file:
            data = file.read()
            encoded_text = cryptocode.encrypt(data, self.key)
            self.print_result(encoded_text)
    
    def decrypt(self):
        with open(argv[2], "r") as file:
            data = file.read()
            decoded_text = cryptocode.decrypt(data, self.key)
            self.print_result(decoded_text)
    
    def run(self):
        if (self.command in MAKEKEY):
            self.make_key()
            return

        if (self.path == ""):
            self.exit_with_help()
        if (not os.path.exists(self.path)):
           self.exit_no_file()

        if (self.command in ENCRYPT):
            self.encrypt()
        elif (self.command in DECRYPT):
            self.decrypt()
        else:
            self.exit_with_help()

if __name__ == "__main__":
    encryptor = Encyptor(argv)
    encryptor.run()
