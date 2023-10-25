word = input()

while word != 'End':
    if word == "SoftUni":
        word = input()
        continue
    else:
        double_char = ''
        for ch in word:
            double_char += 2 * ch
        print(double_char)
    word = input()