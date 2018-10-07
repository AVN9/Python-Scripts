import random
import queue
import threading

def main():
    keywordslist = input("Insert your keyswords seperated by a space: ").split(" ")
    if Confirm(keywordslist) == False:
        main()
    q = queue.Queue()
    g = Generator(keywords=keywordslist,q=q)
    filename = GetFilename()
    w = Writer(filename, q)
    print("This might take a while depending of your keyword size so go get a cup of water or something else.")
    w.start()
    g.start()

class Writer(threading.Thread):

    def __init__(self, filename, q):
        super().__init__()
        self.filename = filename
        self.q = q

    def run(self):
        with open(self.filename, "w") as f:
            while True:
                m = self.q.get()
                if m == "exitthreadnow":
                    print("Done!")
                    print("Made with love by Luís Duarte. Bye have a nice day ^^")
                    break
                f.write(m + "\n")

def GetFilename():
    filename = input("Insert the path of the new file: ")
    if Confirm(filename) == False:
        GetFilename()
    else:
        return filename

def Confirm(thingtoconfirm):
    confirmation = input("Are you sure that " + str(thingtoconfirm) + " is correct? (y/n): ")
    if  confirmation == "y" or confirmation == "Y":
        return True
    else:
        return False

class Generator(threading.Thread):
    seperators = ["-", " ", ".", "", "_",":"]
    suffix = ["", "123", "321", "!", "!!", "1", "2", "123456" ".", "*", "@", "..", ";"]
    numbersforletters = {'a': '4', 'g': '6', 's': '5', 'b': '8', 't': '7', 'z': '2', 'i': '1', 'o': '0', 'e': '3', 'q': '9', 'A': '4', 'G': '6', 'S': '5', 'B': '8', 'T': '7', 'Z': '2', 'I': '1', 'O': '0', 'E': '3', 'Q': '9'}

    def __init__(self, keywords, q):
        super().__init__()
        self.keywords = keywords
        self.q = q

    def run(self):
        for i in self.keywords:
            self.q.put(i)
        for num, i in enumerate(self.keywords):
            for e in self.seperators:
                for l in self.suffix:
                    for t in self.suffix:
                        self.q.put(t + i + l)
                        for m in self.keywords:
                            self.q.put(t + i + e + m + l)
                            for n in self.keywords:
                                self.q.put(t + i + e + m + e + n + l)
        self.q.put("exitthreadnow")

    


if __name__ == "__main__":
    main()