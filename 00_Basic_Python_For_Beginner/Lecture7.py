""" #File i/o

f = open("Lecture7.txt", "r+") # r, w, a, r+
#data = f.read()
#data = f.read(10) # read n characters
data1 = f.readline() # read single line
print(data1)

data2 = f.readlines() # read all lines and store in list
print(data2)

# Write or update text in the same file.
data = f.write("I am learning\nPython from ApnaCollege & I love it & I am enjoying it.")

# Append text in the same file.
#data = f.write("\n Next i will learn c#.")

#print(data) # it will return number of characters written in the file. 

# read and write both
data = f.read("20")
print(data)

f.close() """


"""# with automatically closes the file after the nested block of code is executed.
with open("Lecture7.txt", "r") as f:
    data = f.read()
    print(data)

    with open("Lecture7.txt", "a") as f:
        f.write("\n Next i will learn c++.")

        import os
        os.remove("Lecture7.txt") # to delete a file"""

# Practice set
"""WAF to find which line of the file does the word "learning" occurs first.
print -1 if not found."""

"""def find_word_in_file():
    word = "learning"
    with open("Lecture7.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")  
find_word_in_file()"""

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("Lecture7.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"Found in line no {line_no}")
                return
            line_no += 1    
    print(-1)
check_for_line()


