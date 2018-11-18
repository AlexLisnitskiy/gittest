import glob, os

print("This program shows list of all files in current directory")
str = input("Please, set file extention if needed: ")
if str == "":
    str = "*"
os.chdir(os.getcwd())
for file in glob.glob("*." + str):
    print(file)
