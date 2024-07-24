import os
import pandas as pd
import openpyxl
from datetime import datetime, date
# print(os.getcwd())

# create a module for reusable functions
def hod_folder(folder):
    try:
        myfolder = os.mkdir(folder)
        return (myfolder)
    
    except FileExistsError:
        return 'folder already exists'

def write_file(name, folder, stud_id, score, remarks, instruct_id, topics, col_no):
    filename = name + '.xlsx'
    filepath = os.path.join(folder, filename)
    with pd.ExcelWriter(filepath,
    datetime_format="YYYY-MM-DD", mode='w') as writer:
        # check if content exist
        df = pd.DataFrame([[stud_id, score, remarks, instruct_id, topics, date(2024, 7, 14)]], index=[col_no], columns=['students_id', 'score', 'remarks', 'instructors_id', 'topics', 'date'])
        df.to_excel(writer, sheet_name='StudentScore')
        writer._save()

        # set up a cron system