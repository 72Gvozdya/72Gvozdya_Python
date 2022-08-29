punct = str.maketrans("", "", "!,.:;?-")
with open('moby_01.txt') as infile, open('moby_01_clean.txt', 'w') as outfile:
    for line in infile:
        # Привести к одному регистру
        cleaned_line = line.lower()
        # Удалить знаки препинания
        cleaned_line = cleaned_line.translate(punct)
        # Разбить на слова
        words = cleaned_line.split()
        cleaned_words = "\n".join(words)
        # Записать все слова по одному на строку файла
        outfile.write(cleaned_words)