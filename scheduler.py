import time
import os

show_execution_time = True

def ExecuteLatexAndGetTime():
    t1 = time.time()
    os.system("xelatex.exe --quiet main.tex")
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
    while (True):
        last_time = ExecuteLatexAndGetTime()
        if (show_execution_time):
            print(last_time)
