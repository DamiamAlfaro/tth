import datetime 
import os


def tth_a():
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
        with open("tth.txt","r") as file2:
            records = file2.readlines()
            if int(records[-1:][0][0]) == 0:
                pass
            else:
                lastoutset = eval(records[-2:][0][1:-1])
                lastfinish = eval(records[-2:][1][1:-1])
                outset_time = int(lastoutset[3])+round(int(lastoutset[4])/60,2)
                finish_time = int(lastfinish[3])+round(int(lastfinish[4])/60,2)
                th = finish_time - outset_time 
                print(f"\nLast flow = {round(th,2)} hours\n")

    the = input("\n[OUTSET] [HALT]\n\n-> ")
    match str(the).upper():
        case "OUTSET":
            with open("tth.txt","r+") as file:
                check = file.readlines()
                if int(check[-1:][0][0]) == 0:
                    raise TypeError("Close your counting dumbass.")
                else:
                    file.write("0"+str(outset)+"\n")
        case "HALT":
            with open("tth.txt","r+") as file:
                check = file.readlines()
                if int(check[-1:][0][0]) == 1:
                     raise TypeError("Open your counting dumbass.")
                else:
                    file.write("1"+str(outset)+"\n")
        case _:
            print("\nWRONG WORD\n")



def tth_b(self):
    with open(self,"r") as counts:
        ins = counts.readlines()
        print(ins)







if __name__ == "__main__":
    tth_a()
    tth_b("tth.txt")



































































