from ntpath import realpath
import tkinter
import os, time
import re
import datetime

logs_path = 'E:\logs'
words = ['BT\[','SSI Memory Utilization','REBOOTING NOW!!!','SETUP FAILURE',"reboot"]

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
                        with open(join(os.path.dirname(realpath(__file__)), "Scanned Logs", "hello.txt"), "w") as export:
                            export.write("hello")
                        if dateHour >= logs_startTime and dateHour <= logs_EndTime:
                            print('its bigger')
                            try:
                                f=open(os.path.join(subdir, file),'r')
                                a = f.readlines()
                                for line in a:
                                    if re.compile('|'.join(words),re.IGNORECASE).search(line):
                                        print(line)
                                    else:
                                        pass
                            except:
                                print("something went wrong in the file")
                            #f.close()
        except:
            print("something went wrong")
            pass