import datetime 
import os
import matplotlib.pyplot as plt






class tth_noting:
    def getting_dates():
        all_date = datetime.datetime.now()
        date_string = str(all_date).split(" ")
        matrix_date = date_string[0].split("-")
        year, month, day = date_string[0].split("-")[0], date_string[0].split("-")[1], date_string[0].split("-")[2]
        hour, minute, second = date_string[1].split(":")[0], date_string[1].split(":")[1], round(float(date_string[1].split(":")[2]),1)
        return matrix_date, year, month, day, hour, minute, second





    def tth_b(self): #past b) here we extract the integers representing the quantities of each instance to later graph them
        integers = []
        finish_time = []
        outsets = []
        finishes = []
        with open(self,"r") as counts:
            ins = counts.readlines()
            for out,fin in enumerate(ins):
                if out % 2 == 0:
                    outsets.append(int(eval(fin[1:-1])[3])+round(int(eval(fin[1:-1])[4])/60,3))
                else:
                    finishes.append(int(eval(fin[1:-1])[3])+round(int(eval(fin[1:-1])[4])/60,3))
                    finish_time.append(int(eval(fin[1:-1])[3])+round(int(eval(fin[1:-1])[4])/60,2))


        for initial,last in zip(outsets,finishes):
            integer = round(last - initial,3)
            integers.append(integer)

        return integers,finish_time
        

    def tth_c(self): #part c) graph the array of integers (amount of hours spend)
        x = self[0]
        y = self[1]
        totalh = round(sum(x),2)
        plt.scatter(x,y,color = "#093b5d")
        plt.title(f"{choice.title()} | Hours = {totalh}")
        plt.ylabel("Time of day")
        plt.xlabel("Hours")
        plt.show()

    

    def tth_a(self): #part a) this function prepares to start; checks for errors (closed or open instances), returns the last instance quantity, and annotates the instance
        dat = str(datetime.datetime.now()).split(" ")
        calendar = dat[0].split("-")
        time = dat[1].split(":")
        instance = calendar+time
        outset = {}
        for a in range(len(instance)):
            outset[a] = instance[a]

        if os.path.getsize(self) == 0:
            pass
        else:
            with open(self,"r") as file2:
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

        the = input("\n[OUTSET] [HALT] [VIEW]\n\n-> ")
        match str(the).upper():
            case "OUTSET":
                with open(self,"r+") as file:
                    check = file.readlines()
                    if int(check[-1:][0][0]) == 0:
                        raise TypeError("Close your counting dumbass.")
                    else:
                        file.write("0"+str(outset)+"\n")
            case "HALT":
                with open(self,"r+") as file:
                    check = file.readlines()
                    if int(check[-1:][0][0]) == 1:
                         raise TypeError("Open your counting dumbass.")
                    else:
                        file.write("1"+str(outset)+"\n")
            case "VIEW":
                tth_noting.tth_c(tth_noting.tth_b(self))
            case _:
                print("\nWRONG WORD\n")
        
        return calendar

    def accuracy_rate():
        total_questions = int(input("Total # Questions: "))
        right_questions = int(input("Total # Right questions answered: "))
        rate_float = round(right_questions/total_questions,3)
        rate_percentage = float(rate_float * 100)
        return rate_float, rate_percentage
            
    def recording_accuracy(self):
        rates = tth_noting.accuracy_rate()
        print(f"\nToday's Accuracy: {rates[1]}%\n")
        with open(accuracy_file,"a") as file:
            file.write(f"{tth_noting.getting_dates()[0]} = {rates[0]}\n")




if __name__ == "__main__":
    print("\n[Programming] [Mathematics]\n")
    choice = input("-> ")
    programming_file = "/Users/damiamalfaro/tth/tth_programming.txt"
    math_file = "/Users/damiamalfaro/tth/tth_math.txt"
    accuracy_file = "/Users/damiamalfaro/tth/tth_math_accuracy.txt"
    match str(choice).upper():
        case "PROGRAMMING":
            tth_noting.tth_a(programming_file)
        case "MATHEMATICS":
            tth_noting.tth_a(math_file)
            tth_noting.recording_accuracy(accuracy_file)
        case _:
            print("\nI'm sorry?...Do you know how to type?...\n")

        
            


 



































































