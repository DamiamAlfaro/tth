import datetime 
import os


def tth_a(): #part a) this function prepares to start; checks for errors (closed or open instances), returns the last instance quantity, and annotates the instance
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



def tth_b(self): #past b) here we extract the integers representing the quantities of each instance to later graph them
    integers = []
    outsets = []
    finishes = []
    with open(self,"r") as counts:
        ins = counts.readlines()
        for out,fin in enumerate(ins):
            if out % 2 == 0:
                outsets.append(int(eval(fin[1:-1])[3])+round(int(eval(fin[1:-1])[4])/60,3))
            else:
                finishes.append(int(eval(fin[1:-1])[3])+round(int(eval(fin[1:-1])[4])/60,3))


    for initial,last in zip(outsets,finishes):
        integer = round(last - initial,3)
        integers.append(integer)

    return integers
        

def tth_c(self): #part c) graph the array of integers (amount of hours spend)
    pass

                    
        
    






if __name__ == "__main__":
    tth_a()
    print(tth_b("tth.txt"))



































































