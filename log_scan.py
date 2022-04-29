import os, time
import re
import datetime
import sys
import threading
from tkinter import StringVar

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

logs_path = 'E:\logs'
words = ['BT\[','SSI Memory Utilization','REBOOTING NOW!!!','SETUP FAILURE','reboot','### warm reboot ###','FSM1_FSM2_TIMING_OUT_OF_SYNC','Stop recording']

def run_thread(logs_date,logs_time):
    download_thread = threading.Thread(target=search_logs, name="Downloader", args=(logs_date, logs_time))
    download_thread.start()

def init_progress():
    global progress_var
    global progress_status
    progress_var = tk.DoubleVar()
    progress_status = tk.StringVar()
    progress_status.set(" ")

def search_logs(logs_date,logs_time):
        progress_var.set(0)
        try:
            directory = os.path.normpath(f"C:/logs/{logs_date}")
            for subdir, dirs, files in os.walk(directory):
                directory = os.path.dirname(os.path.abspath(__file__))
                start_time_txt = logs_time[0].split(':')
                end_time_txt = logs_time[1].split(':')
                log_scanner_txt = ""+logs_date+"___"+start_time_txt[0]+"_"+start_time_txt[1]+"-"+end_time_txt[0]+"_"+end_time_txt[1]+".txt"
                tmp_name = log_scanner_txt
                if os.path.exists(directory+"/"+tmp_name):
                    for i in range(1,10):
                        tmp_name = f"{log_scanner_txt[:-4]}({i}).txt"
                        if not os.path.exists(directory+"/"+tmp_name):
                            break
                my_file = os.path.join(directory, tmp_name)
                step = 100/len(files)
                cnt = step
                progress_var.set(cnt)
                txt_printed = False
                for file in files:
                    if file.endswith(".log"):
                        modified = os.path.getmtime(f"C:/logs/{logs_date}/{file}")
                        dateNum = re.findall(r'\d{1,2}:\d{1,2}',str(datetime.datetime.fromtimestamp(modified)))
                        dateHour = datetime.datetime.strptime(str(dateNum[0]), '%H:%M').time()
                        logs_startTime = datetime.datetime.strptime(str(logs_time[0]), '%H:%M').time()
                        logs_EndTime = datetime.datetime.strptime(str(logs_time[1]), '%H:%M').time()
                        if dateHour >= logs_startTime and dateHour <= logs_EndTime:
                            try:
                                f=open(os.path.join(subdir, file),'r')
                                a = f.readlines()
                                with open(my_file, "a") as file_txt:
                                    file_txt.write("\n\n\n--------------------------- "+file+" ---------------------------\n\n\n")
                                for line in a: 
                                    if re.compile('|'.join(words),re.IGNORECASE).search(line):
                                        with open(my_file, "a") as file_txt:
                                            file_txt.write(line+"\n")
                                            txt_printed = True
                                    else:
                                        pass
                            except:
                                print("something went wrong in the file")
                            #f.close()
                        cnt += step
                        progress_var.set(cnt)
                        if txt_printed:
                            progress_status.set(f"Successfully Scanned and exported to:\n{tmp_name}")
                            
                
                       
                    

        except:
            print("something went wrong")
            pass
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

if __name__ == '__main__':
    import natan
    natan.vp_start_gui()

"""
------------------ READ FROM START till END ------------------

with open('test.txt') as input_data:
    # Skips text before the beginning of the interesting block:
    for line in input_data:
        if line.strip() == 'Start':  # Or whatever test is needed
            break
    # Reads text until the end of the block:
    for line in input_data:  # This keeps reading the file
        if line.strip() == 'End':
            break
        print line # Line is extracted (or block_of_lines.append(line), etc.)

"""