import tkinter
import os, time
import re
import datetime

logs_path = 'E:\logs'
words = ['BT\[','SSI Memory Utilization','REBOOTING NOW!!!','SETUP FAILURE','reboot','### warm reboot ###','FSM1_FSM2_TIMING_OUT_OF_SYNC','Stop recording']

def search_logs(logs_date,logs_time):
        global words
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
                                file_cnt = 0
                                if file_cnt == 0:
                                    with open(my_file, "a") as file_txt:
                                        file_txt.write("\n\n\n--------------------------- "+file+" ---------------------------\n\n\n")
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