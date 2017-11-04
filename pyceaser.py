# include standard modules
import argparse

# initiate the parser
parser = argparse.ArgumentParser(description = "Ceaser Cipher In Python")  
parser.parse_args()

class PyCeaser():
    def __init__(self,msg = None,shf = None,enc = None, silent = None):
        print("  ____         ____                         ")
        print(" |  _ \ _   _ / ___|___  __ _ ___  ___ _ __ ")
        print(" | |_) | | | | |   / _ \/ _` / __|/ _ \ '__|")
        print(" |  __/| |_| | |__|  __/ (_| \__ \  __/ |   ")
        print(" |_|    \__, |\____\___|\__,_|___/\___|_|   ")
        print("        |___/                               \n\n")
        if msg == None:
            msg = input("Enter Message:\n  >")
        if shf == None:
            shf = int(input("Enter Shift:\n  >"))
        if enc == None:
            enc = input("Encode or Decode (e/d):\n  >").lower()
            if enc == "e":
                enc = True
            else:
                enc = False
        if silent == None:
            silent = input("Silent? (y/n):\n  >").lower()
            if silent == "n":
                silent = True
            else:
                silent = False                
        # Alphabet #
        self.alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!1234567890<>?,./:@~;'#{}[]£$%^&*()_+=-|\/¬` "
        # Shift #
        self.shift = shf
        # Verbose Output #
        self.silent = silent
        # Give Output Of Operation #
        if silent == False:
            print("  Message: "+str(msg))
            print("  Shift: "+str(shf),"\n")
        # Message #
        if enc == True:
            self.msg = self.encode(msg) # Converts to numerical values and adds shift
        else:
            self.msg = self.decode(msg) # Converts to numerical values and subtracts shift
    def encode(self,msg):
        x = ""
        for i in msg:
            num = self.alpha.index(i)
            value = num + self.shift
            while value >= len(self.alpha): # Corrects any overflow
                value = value - len(self.alpha)
            let = self.alpha[value]
            # Prints Workings #
            if self.silent == False:
                if num < 10:
                    num = "0"+str(num)
                if value < 10:
                    value = "0"+str(value)
                print("  - '"+str(i)+"': "+str(num)+"   -->   "+str(num)+" + "+str(self.shift)+" = "+str(value)+": '"+str(let)+"'")
            x = x + str(let)
        print("")
        return x
    def decode(self,msg):
        x = ""
        for i in msg:
            num = self.alpha.index(i)
            value = num - self.shift
            while value < 0: # Corrects any overflow
                value = value + len(self.alpha)
            let = self.alpha[value]
            # Prints Workings #
            if self.silent == False:
                if num < 10:
                    num = "0"+str(num)
                if value < 10:
                    value = "0"+str(value)
                print("  - '"+str(i)+"': "+str(num)+"   -->   "+str(num)+" - "+str(self.shift)+" = "+str(value)+": '"+str(let)+"'")
            x = x + str(let)
        print("")
        return x
PyCeaser()


