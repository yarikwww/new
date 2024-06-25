#Вправа 2.2
with open('file1.txt', 'r') as file:
    original_content = file.read()


upp = original_content.upper()


with open('file2.txt', 'w') as file:
    file.write(upp)