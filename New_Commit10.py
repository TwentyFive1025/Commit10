# Commit10
# Excel

import subprocess
import pandas as pd
import os
import sys

def get_git_log_data():
    log_format = "%h@@@%an@@@%ad@@@%s"
    
    result = subprocess.run(
        ["git", "log", f"--pretty=format:{log_format}", "--date=format:%a %b %d %H:%M:%S %Y"],
        capture_output=True,
        text=True,
        check=True,
        encoding="utf-8"
        )

    log_output = result.stdout.strip()
    commits = []
    if log_output:
        for line in log_output.split('\n'):
            parts = line.split('@@@')
            if len(parts) == 4:
                commits.append(parts)
    return commits

if __name__ == "__main__":
    file_name = input("Название файла: ")
    Sheet_name = input("Название листа: ")

    git_data = get_git_log_data()
    headers = ["Commit", "Author", "Date", "message"]
    df = pd.DataFrame(git_data, columns=headers)
    excel_file_path = os.path.join('.', f'{file_name}.xlsx')

    df.to_excel(excel_file_path, sheet_name=sheet_name, index=False)
    
