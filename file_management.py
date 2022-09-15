from importlib.resources import path
from msilib.schema import Directory
import os
import shutil
from sre_constants import GROUPREF_EXISTS


#choose the desired folder location to organize
os.chdir(#choose your desired path(make sure '\' is '\\') )

#Type of files
#feel free to add any extension I have missed
pdf_type = '.pdf'
video_type = ('.mp4', '.mov','.avi', '.flv', '.mkv', '.wmv')
microsoft_type = ('.doc', '.docx', '.txt', '.xls', '.ppt','.xlsx', '.pptx')
software_type = ('.exe', '.pkg', '.dmg')
image_type = ('.jpg', '.jpeg', '.png','.svg','.gif', '.tif','.tiff')
audio_type = ('.wav', '.aiff', '.flac','.aac','.mp3','.alac','.wma')

#Make folder if it doesn't exist
if not os.path.exists("PDF"):
    os.mkdir("PDF")
    print("PDF folder created")

if not os.path.exists("Videos"):
    os.mkdir("Videos")
    print("Video folder created")

if not os.path.exists("Microsoft Offices"):
    os.mkdir("Microsoft Offices")
    print(" Microsoft Offices folder created")

if not os.path.exists("Softwares"):
    os.mkdir("Softwares")
    print(" Softwares folder created")

if not os.path.exists("Pictures"):
    os.mkdir("Pictures")
    print("Pictures folder created")

if not os.path.exists("ETC"):
    os.mkdir("ETC")
    print("ETC")

if not os.path.exists("Audio"):
    os.mkdir("Audio")
    print("Audio folder created")

def get_non_hidden_files_except_current_file():

    return [f for f in os.listdir() if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__) ]

#Iterate throught the folder and put each file into correct folders
def move_files(files):
    for file in files:
        if file.endswith(pdf_type):
            shutil.move(file,"PDF")
        elif file.endswith(video_type):
            shutil.move(file,"Videos")
        elif file.endswith(microsoft_type):
            shutil.move(file,"Microsoft Offices")
        elif file.endswith(software_type):
            shutil.move(file, "Softwares")
        elif file.endswith(image_type):
            shutil.move(file, "Pictures")
        elif file.endswith(audio_type):
            shutil.move(file, "Audio")
        else:
            shutil.move(file,"ETC")
    print("Organizing finished")



if __name__ == "__main__":
    file = get_non_hidden_files_except_current_file()
    move_files(file)