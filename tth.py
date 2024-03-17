import datetime 
import os
import matplotlib.pyplot as plt
import ast
from collections import Counter
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import json

class tth:
    def getting_dates():
        all_date = datetime.datetime.now()
        date_string = str(all_date).split(" ")
        matrix_date = date_string[0].split("-")
        year, month, day = date_string[0].split("-")[0], date_string[0].split("-")[1], date_string[0].split("-")[2]
        hour, minute, second = date_string[1].split(":")[0], date_string[1].split(":")[1], round(float(date_string[1].split(":")[2]),1)
        return matrix_date, year, month, day, hour, minute, second


    def hours_numeration(self): #past b) here we extract the integers representing the quantities of each instance to later graph them
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
        

    def hours_visual(self):
        x = self[0]
        y = self[1]
        totalh = round(sum(x),2)
        plt.scatter(x, y, color='blue')
        plt.title(f"{choice.title()} | Hours = {totalh}")
        plt.ylabel("Time of day")
        plt.xlabel("Hours")
        plt.show()

    

    def time_date_recording(self,answer):
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

        match str(answer).upper():
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
                tth.hours_visual(tth.hours_numeration(self))
            case _:
                print("\nWRONG WORD\n")
        
        return calendar

    def accuracy_rate(): 
        #here you need to record the total of questions, and the correct ones in the file as well.
        total_questions = int(input("Total # Questions: "))
        right_questions = int(input("Total # Right questions answered: "))
        rate_float = round(right_questions/total_questions,4)
        rate_percentage = float(rate_float * 100)
        return rate_float, rate_percentage
            
    def recording_accuracy(self):
        rates = tth.accuracy_rate()
        print(f"\nToday's Accuracy: {rates[1]}%\n")
        with open(accuracy_file,"a") as file:
            file.write(f"{tth.getting_dates()[0]} = {rates[0]}\n")

    def days_worked(self):
        days_worked = []
        list_first = []
        with open(self,"r") as file:
            dates = file.readlines()
        for instance in dates:
            l = list(ast.literal_eval(instance[1:-1]).values())
            l_2 = l[0],l[1],l[2]
            list_first.append(list(l_2))
        # find a way to remove the repeated lists

    
    def analyzing_accuracy(self):
        pass

    def daily_hour_goal(self):
        pass

    def timeline(self,mil_action):
        sector = str(mil_action).title()
        print("\n[New] [View]\n")
        action = input("-> ")
        match str(action).upper():
            case "NEW":
                print("\nInput Date as: YYYY-MM-DD\n")
                date = str(input("-> "))
                try:
                    datetime.datetime.strptime(date,"%Y-%m-%d")
                except:
                    return "\nDo not know how to read?..."
                print("\nWhat occurred that date?\n")
                instance = input("-> ")
                if os.path.getsize(self) == 0:
                    new = [[],[]]
                    with open(self,"w") as testing:
                        json.dump(new,testing)
                else:
                    pass
                
                with open(self,"r") as file:
                    timelines = json.load(file)

                timelines[0].append(date)
                timelines[1].append(instance)

                with open(self,'w') as file_again:
                    json.dump(timelines,file_again)

            case "VIEW":
                with open(self,'r') as file:
                    milestones = json.load(file)
                
                dates = milestones[0]
                milestone = milestones[1]
                setup = pd.DataFrame(data={"Date": dates,"Milestone": milestone})
                setup["Date"] = pd.to_datetime(setup["Date"])
                setup["Level"] = [np.random.randint(-6,-2) if (i%2)==0 else np.random.randint(2,6) for i in
                                  range(len(setup))]
                with plt.style.context("fivethirtyeight"):
                    fig, ax = plt.subplots(figsize=(7,10))
                    ax.plot([0,]* len(setup), setup.Date,"-o",color="black",markerfacecolor="white");
                    ax.set_yticks(pd.date_range("2024-1-1","2024-12-30",freq="YS"), range(2024,2024));
                    ax.set_xlim(-7,7);
                    for idx in range(len(setup)):
                        dt,product,level = setup["Date"][idx],setup["Milestone"][idx],setup["Level"][idx]
                        dt_str = dt.strftime("%b-%Y")
                        ax.annotate(dt_str+"\n"+product,xy=(0.1 if level>0 else -0.1,dt),
                                    xytext=(level,dt),
                                    arrowprops=dict(arrowstyle="-",color="red",linewidth=0.8),
                                    va="center",fontsize=8);
                        ax.spines[["left", "top", "right", "bottom"]].set_visible(False);
                        ax.spines[["left"]].set_position(("axes", 0.5));
                        ax.xaxis.set_visible(False);
                        ax.set_title(f"{sector} Milestones", pad=10, loc="left",
                                     fontsize=25, fontweight="bold");
                        ax.grid(False)
                plt.show()        




if __name__ == "__main__":
    # we ought to find a way to reduce the amount of files here, I mean, sure, you only have
    # a couple of sectors, but the app will have n files by the user, a complex user.
    # we need a way to handle these files neatly. 
    programming_file = "/Users/damiamalfaro/tth/tth_programming.txt"
    math_file = "/Users/damiamalfaro/tth/tth_math.txt"
    accuracy_file = "/Users/damiamalfaro/tth/tth_math_accuracy.txt"
    math_timeline = "/Users/damiamalfaro/tth/tth_math_milestones.json" 
    programming_timeline = "/Users/damiamalfaro/tth/tth_programming_timeline.json"
    profession_timeline = "/Users/damiamalfaro/tth/tth_profession_timeline.json"
    profession_file = "/Users/damiamalfaro/tth/tth_profession.txt"
    ir_timeline = "/Users/damiamalfaro/tth/tth_ir_timeline.json"
    ir_file = "/Users/damiamalfaro/tth/tth_ir.txt"
    print("\n[Programming] [Mathematics] [Profession] [IR & Bussiness]\n")
    choice = input("-> ")
    match str(choice).title():
        case "Mathematics" | "Programming" | "Ir" | "Profession":
            print("\n[OUTSET] [HALT] [VIEW] [TEST] [MILESTONE]\n")
            answer = input("-> ")
            match str(answer).upper():
                case "OUTSET" | "HALT" | "VIEW":
                    tth.time_date_recording(math_file,answer)
                case "TEST":
                    tth.recording_accuracy(accuracy_file)
                case "MILESTONE":
                    tth.timeline(math_timeline,choice)
                case _:
                    pass

        case _:
            print("\nI'm sorry?...Do you know how to type?...\n")

        
            


 



