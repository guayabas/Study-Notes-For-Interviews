import argparse
import time
import os

TEXLIVE_EXECUTABLE_PATH = "C:\\texlive\\2022\\bin\\win32\\xelatex.exe"
# MIKTEX_EXECUTABLE_PATH = "C:\\Users\\aleja\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\xelatex.exe"
MIKTEX_EXECUTABLE_PATH = "C:\\Users\\aleja\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\pdflatex.exe"
show_execution_time = True

def ExecuteLatexAndGetTime(latex_executable_path:str, latex_command_options):
    command_to_run = latex_executable_path + latex_command_options + " main.tex > log.txt"
    t1 = time.time()
    os.system(command_to_run)
    t2 = time.time()
    return (t2 - t1)

def show(key):
    if (key == 'u'):
            average_status = input("Key 'u' has been pressed, get an average run for current latex execution [Y/N]")
            if (average_status == 'Y' or average_status == 'y'):
                number_attempts = 25
                attempts = []
                for i in range(0,number_attempts):
                    attempts.append(ExecuteLatexAndGetTime())
            else:
                print("Average cancelled")
    elif (key == 's'):
            show_execution_time ^= 1

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--latex_executable", default="miktex")
    console_arguments = parser.parse_args()
    latex_executable = None
    latex_command_options = None
    if   (console_arguments.latex_executable == "miktex"):
        latex_executable = MIKTEX_EXECUTABLE_PATH
        latex_command_options = " --quiet"
    elif (console_arguments.latex_executable == "texlive"):
        latex_executable = TEXLIVE_EXECUTABLE_PATH
        latex_command_options = ""
    else:
        print("Unknown latex executable. Aborting.")
        exit()
    print("Using : {}".format(latex_executable))
    while (True):
        last_time = ExecuteLatexAndGetTime(latex_executable, latex_command_options)
        if (show_execution_time):
            print(last_time)
