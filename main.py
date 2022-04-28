import tkinter
import os, time
import re
import datetime

logs_path = 'E:\logs'
words = ['BT\[','SSI Memory Utilization','REBOOTING NOW!!!','SETUP FAILURE','reboot']

def search_logs(logs_date,logs_time):
        global words
        try:
            directory = os.path.normpath(f"C:/logs/{logs_date}")
            for subdir, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(".log"):
                        print(f"this is the file name {file}")
                        modified = os.path.getmtime(f"C:/logs/{logs_date}/{file}")
                        dateNum = re.findall(r'\d{1,2}:\d{1,2}',str(datetime.datetime.fromtimestamp(modified)))
                        print(f"this is file time: {dateNum}")
                        dateHour = datetime.datetime.strptime(str(dateNum[0]), '%H:%M').time()
                        logs_startTime = datetime.datetime.strptime(str(logs_time[0]), '%H:%M').time()
                        logs_EndTime = datetime.datetime.strptime(str(logs_time[1]), '%H:%M').time()
                        directory = os.path.dirname(os.path.abspath(__file__))
                        start_time_txt = logs_time[0].split(':')
                        end_time_txt = logs_time[1].split(':')
                        log_scanner_txt = ""+logs_date+"___"+start_time_txt[0]+"_"+start_time_txt[1]+"-"+end_time_txt[0]+"_"+end_time_txt[1]+".txt"
                        print(f"this is {log_scanner_txt}")
                        my_file = os.path.join(directory, log_scanner_txt)
                        if dateHour >= logs_startTime and dateHour <= logs_EndTime:
                            try:
                                f=open(os.path.join(subdir, file),'r')
                                a = f.readlines()
                                file_cnt = 0
                                if file_cnt == 0:
                                    with open(my_file, "a") as file_txt:
                                        file_txt.write(file+" : \n")
                                for line in a: 
                                    if re.compile('|'.join(words),re.IGNORECASE).search(line):
                                        with open(my_file, "a") as file_txt:
                                            file_txt.write(line+"\n")
                                    else:
                                        pass
                            except:
                                print("something went wrong in the file")
                            #f.close()
        except:
            print("something went wrong")
            pass