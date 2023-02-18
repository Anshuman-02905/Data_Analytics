import json
import pandas as pd
import os
def display_reports_admin():
    if (os.path.isfile("user_data.json") is False):
        # Check for if file is present or not
        # File will be generated only if any user will do some purchase
        print("No User Reports are Present")
        return
    fd = open("user_data.json", 'r')
    txt = fd.read()
    user_data = json.loads(txt)
    fd.close()
    print("Enter '0' to Check All Bills/Reports\
	and '1' To Check Specific User Bills/Reports :- ")
    n = int(input())
    if (n == 1):
        print("Enter User ID Whose Details You Want to Have a Look on")
        i = input()
        temp = pd.DataFrame()
        if i in user_data.keys():
            for j in user_data[i].keys():
                d = dict()
                d['User ID'] = i
                d['Purchase Number'] = j
                for k in user_data[i][j].keys():
                    d[k] = user_data[i][j][k]
                temp = temp.append(d, ignore_index=True)
                d = dict()
            temp = temp.reset_index(drop=True)
            from IPython.display import display
            display(temp)
        else:
            print("You Have Entered Wrong User ID that is not Present in DataBase...!!!")
    elif (n == 0):
        table = pd.DataFrame()
        for i in user_data.keys():
            temp = pd.DataFrame()
            for j in user_data[i].keys():
                d = dict()
                d['User ID'] = i
                d['Purchase Number'] = j
                for k in user_data[i][j].keys():
                    d[k] = user_data[i][j][k]
                temp = temp.append(d, ignore_index=True)
                d = dict()
            table = table.append(temp)
        table = table.reset_index(drop=True)
        from IPython.display import display
        display(table)
    else:
        print("Please Enter Valid Choice...!!!")
display_reports_admin()