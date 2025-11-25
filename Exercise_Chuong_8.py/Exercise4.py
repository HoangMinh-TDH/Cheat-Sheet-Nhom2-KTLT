file_name = input("Enter file: ")
try:
    file_list = open(file_name)
except FileNotFoundError:
    print("File not found:", file_name)
    exit()

word_list = []

for line in file_list:
    words = line.split()
    for word in words:
        if word not in word_list:
            word_list.append(word)

file_list.close()
word_list.sort()

print(word_list)