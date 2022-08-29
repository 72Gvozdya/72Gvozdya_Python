'''Читает файл и возвращает количество строк, слов и символов'''

infile = open('word_count.tst')  # открывает файл
lines = infile.read().split("\n")  # читает файл с разбивкой по строкам
line_count = len(lines)  # Определяет кол-во строк функцией len
# инициализирует другие счётчики
word_count = 0
char_count = 0
for line in lines:  # перебирает строки файла
    words = line.split()  # выполняет разбивку по словам
    word_count += len(words)

    char_count += len(line)  # возвращает кол-во символов

print("File has {0} lines, {1} words, {2} characters".format (line_count, word_count, char_count))