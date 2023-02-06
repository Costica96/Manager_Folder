import os
import shutil

#TODO: Create a directory folder Folder1
os.makedirs("Folder1")
os.chdir("Folder1")

#TODO: Create a text file with name at folder Folder1
file = open("file_1.txt", "w")
file.write("You are in folder Folder1, in file_1 file")
file.close()

#TODO: Create other auxiliar folders in Folder1
os.makedirs("Folder2")
os.makedirs("Folder_1_1")
os.makedirs("Folder_1_2")

#TODO: Create a text file with name at folder Folder_1_1
os.chdir("Folder_1_1")
file = open("file_1_1.txt", "w")
file.write("You are in folder Folder_1_1, in file_1_1 file")
file.close()
os.chdir("..")

#TODO: Create a text file with name at folder Folder_1_2
os.chdir("Folder_1_2")
file = open("file_1_2.txt", "w")
file.write("You are in folder Folder_1_2, in file_1_2 file")
file.close()
os.chdir("..")

#TODO: Create in folder Folder2, other auxiliar folders
os.chdir("Folder2")
os.makedirs("Folder3")
os.makedirs("Folder_2_1")
os.makedirs("Folder_2_2")

#TODO: Create a text file with name at folder Folder2
file = open("file_2.txt", "w")
file.write("You are in folder Folder2, in file_2 file")
file.close()

#TODO: Create a text file with name at folder Folder_2_1
os.chdir("Folder_2_1")
file = open("file_2_1.txt", "w")
file.write("You are in folder Folder_2_1, in file_2_1 file")
file.close()
os.chdir("..")

#TODO: Create a text file with name at folder Folder_2_2
os.chdir("Folder_2_2")
file = open("file_2_2.txt", "w")
file.write("You are in folder Folder_2_2, in file_2_2 file")
file.close()
os.chdir("..")



#TODO: Create in folder Folder3, other auxiliar folders
os.chdir("Folder3")
os.makedirs("Folder_3_1")
os.makedirs("Folder_3_2")

#TODO: Create a text file with name at folder Folder3
file = open("file_3.txt", "w")
file.write("You are in folder Folder3, in file_3 file")
file.close()

#TODO: Create a text file with name at folder Folder_3_1
os.chdir("Folder_3_1")
file = open("file_3_1.txt", "w")
file.write("You are in folder Folder_3_1, in file_3_1 file")
file.close()
os.chdir("..")

#TODO: Create a text file with name at folder Folder_3_2
os.chdir("Folder_3_2")
file = open("file_3_2.txt", "w")
file.write("You are in folder Folder_3_2, in file_3_2 file")
file.close()
os.chdir("..")

#TODO: Delete auxiliar files from general structure
shutil.rmtree("Folder_3_2")
shutil.rmtree("Folder_3_1")

os.chdir("..")
shutil.rmtree("Folder_2_2")
shutil.rmtree("Folder_2_1")

os.chdir("..")
shutil.rmtree("Folder_1_1")
shutil.rmtree("Folder_1_2")

for line in range(1000000):
    with open ("file_1.txt", "a") as file1:
        if os.path.getsize("file_1.txt") < 150:
            file1.write("\n" + "You are in folder Folder1, in file_1 file")
file1.close()

os.chdir("Folder2")
for line in range(10000000):
    with open ("file_2.txt", "a") as file2:
        if os.path.getsize("file_2.txt") < 225:
            file2.write("\n" + "You are in folder Folder2, in file_2 file")
file2.close()

os.chdir("Folder3")
for line in range(10000000):
    with open ("file_3.txt", "a") as file3:
        if os.path.getsize("file_3.txt") < 275:
            file3.write("\n" + "You are in folder Folder3, in file_3 file")
file3.close()

