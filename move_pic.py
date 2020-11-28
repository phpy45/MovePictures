# this code transfers all pictures from camera SD card into
# C:/Users/sense/Pictures/"date taken" it creates a new folder
# in pictures named YYYY-MO-DAY for further post processing

# tl:dr cleans out SD card and organizes pictures on computer by date
import os
import shutil
from datetime import date

os.chdir(r'F:\DCIM\114D3300')
for files in os.listdir(r'F:\DCIM\114D3300'):
    os.chdir(r'F:\DCIM\114D3300')
    list_of_files = os.listdir(r'F:\DCIM\114D3300')
    first_time_stamp = os.path.getctime('F:/DCIM/114D3300/' + str(list_of_files[0]))
    date_info = date.fromtimestamp(first_time_stamp)

    os.chdir("C:/Users/sense/Pictures")
    os.makedirs(str(date_info))

    os.chdir(r'F:\DCIM\114D3300')

    for filename in os.listdir(r'F:\DCIM\114D3300'):
        time_stamp = os.path.getctime('F:/DCIM/114D3300/' + str(filename))
        file_date_info = date.fromtimestamp(time_stamp)
        if file_date_info == date_info:
            os.chdir("C:/Users/sense/Pictures")
            new_loc = "C:/Users/sense/Pictures/" + str(date_info)
            old_file_loc = 'F:/DCIM/114D3300/' + filename
            shutil.move(old_file_loc, new_loc)
