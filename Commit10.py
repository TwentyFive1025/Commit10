# Commit10
# excel

import pandas as pd
import sys
import openpyxl
import os

File_name = input("Название Файла: ")
Sheet_name = input("Название листа: ")
Commit_name = input("Название коммит: ")
Author_name = input("Название автора: ")
Date = input("Дата: ")
Message = input("Сообщение: ")
print(Commit_name, Author_name, Date, Message)

df = pd.DataFrame({'Commit': [Commit_name],'Author': [Author_name], 'Date': [Date], 'Message': [Message]})
excel_file_path = os.path.join('.', f'{File_name}.xlsx')
df.to_excel(excel_file_path, sheet_name=Sheet_name, index=False)
