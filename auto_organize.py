import os, shutil
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path_to_organize = r"C:/Users/ENRIQUE ANGULO/Downloads/"
folder_names = ['csv files', 'image files', 'text files', 'exe files', 'zip files', 'Uncategorized', 'python code files']
file_name = os.listdir(path_to_organize)

for i in range(0, len(folder_names)):
    if not os.path.exists(path_to_organize + folder_names[i]):
        os.makedirs((path_to_organize + folder_names[i]))

for file in file_name:
    if file == "csv files" or file == "image files" or file == "text files" or file == "exe files" or file == "zip files" or file == "Uncategorized" or file == "python code files":
        continue
    elif ".csv" in file or ".xlsx" in file and not os.path.exists(path_to_organize + "csv files/" + file):
        shutil.move(path_to_organize + file, path_to_organize + "csv files/" + file)
    elif ".png" in file or ".jpeg" in file or ".jpg" in file or ".svg" in file and not os.path.exists(path_to_organize + "image files/" + file):
        shutil.move(path_to_organize + file, path_to_organize + "image files/" + file)
    elif ".txt" in file or ".docx" in file or ".pdf" in file or ".html" in file and not os.path.exists(path_to_organize + "text files/" + file):
        shutil.move(path_to_organize + file, path_to_organize + "text files/" + file)
    elif ".exe" in file or ".msi" in file and not os.path.exists(path_to_organize + "exe files/" + file):
        shutil.move(path_to_organize + file, path_to_organize + "exe files/" + file)
    elif ".zip" in file and not os.path.exists(path_to_organize + "zip files/" + file):
        shutil.move(path_to_organize + file, path_to_organize + "zip files/" + file)
    elif ".ipynb" in file or ".py" in file and not os.path.exists(path_to_organize + "python code files/" + file):
        shutil.move(path_to_organize + file, path_to_organize + "python code files/" + file)
    elif True:
        shutil.move(path_to_organize + file, path_to_organize + "Uncategorized/" + file)

