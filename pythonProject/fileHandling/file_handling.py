import os
print(os.getcwd())  # to check the current working directory
os.chdir(r"C:\Users\User\Desktop\check")  # to change the path of current working directory
print(os.getcwd())
# os.mkdir("example")
print(os.getcwd())
os.chdir(r"C:\Users\User\Desktop\check\example")
print(os.getcwd())
# os.mkdir("filehandling")
os.rmdir(r"C:\Users\User\Desktop\check\example\checkSample.py")
