#file handaling
# store
#open read 
# modify

#  how to check if file exist or not
import os
if os.path.exists(r'C:\Users\Dell XPS\Desktop\phython\file.txt'):
    print(" exist")
else:
    print("not exist")
   

"""
text files (.txt ,.csv)
binary files (non text data ,.png .jpg, .pdf .mp3)
"""

#open file in python 
# open("file name","mode")

file = open(r'C:\Users\Dell XPS\Desktop\phython\file.txt')
content = file.read()
print(content)

# close file
file.close()

#write file  
    # if file exist then ovenwrite data 
    # if file dont exist then create new file to store data
file = open(r'C:\Users\Dell XPS\Desktop\phython\file.txt')      
content = input( " Enter a data to  Write:")
file.write(content)
print('data saved successfully!')
file.close()


#with statement           
with open('file _name', 'mode') as file_name:
    print ( file_name.read())    #automatic close

# append mode 
     # dont overwrite data .. simply add data
    # if file dont exist then create new file to store data
with open('C:\\Users\\Dell XPS\\Desktop\\phython\\file.txt', a) as file:
    content = input("Enter data to append =")
    file.write(content)
    print(" appent suggesfullily ")



