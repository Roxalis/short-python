

def count_double_letter(word):
    i = 0
    clist = []
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            clist += ['1']
        else:
            clist += ['0']
        i += 1
    s = ''.join(clist)
    if '10101' in s or '11101' in s or '10111' in s or '11111' in s:
        return True
    else:
        return False


fin = open('words.txt')
for line in fin:
    word = line.strip()
    if count_double_letter(word):
        print(word)
