import os

def count_letters(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        letter_count = sum(c.isalpha() for c in content)
    return letter_count

input_dir = 'input'
output_dir = 'output'
output_file = os.path.join(output_dir, 'results.txt')

total_letter_count = 0

with open(output_file, 'w') as out_file:
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if os.path.isfile(file_path):
            letter_count = count_letters(file_path)
            total_letter_count += letter_count
            out_file.write(f'{filename}: {letter_count}\n')
            print(f'Прочитан файл: {filename}')

print(f'Имя файла с результатами: {output_file}')
print(f'Общее количество букв: {total_letter_count}')
