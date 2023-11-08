import datetime
import os

def tth(self):
    dat = str(datetime.datetime.now()).split(" ")
    calendar = dat[0].split("-")
    time = dat[1].split(":")
    instance = calendar+time
    outset = {}
    for a in range(len(instance)):
        outset[a] = instance[a]

    if os.path.getsize("tth.txt") == 0:
        pass
    else:
        with open("tth.txt","r") as file:
            if int(file.readlines()[-1:][0][0]) == 0:
                return "Haven't close your last session dummy, will have to do it manually."
            else:
                return "s"

    match self:
        case "OUTSET":
            with open("tth.txt","a") as file:
                file.write("0"+str(outset)+"\n")
        case "HALT":
            with open("tth.txt","a") as file:
                file.write("1"+str(outset)+"\n")
        case _:
            print("\nWRONG WORD\n")


    return outset

if __name__ == "__main__":
    start = input(str("\n[OUTSET] [HALT]\n\n-> "))
    print(tth(start.upper()))



































































