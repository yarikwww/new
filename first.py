#Вправа 1
import random



def generate_random_number():
    return random.randint(1, 100)



def create_files_and_summary():
    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    with open('summary.txt', 'w') as summary_file:
        for letter in letters:
            filename = f"{letter}.txt"
            random_number = generate_random_number()
            with open(filename, 'w') as file:
                file.write(str(random_number))
                summary_file.write(f"{filename}: {random_number}\n")





create_files_and_summary()