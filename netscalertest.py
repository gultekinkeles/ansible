word = '-devno'
with open(r'backup.txt', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            metin = line
            alinacakKarakterSayisi = metin.find("-devno")
            yeniMetin = metin[0:alinacakKarakterSayisi - 1]
            print(yeniMetin)
            f = open("backup1.txt", "a")
            f.write(yeniMetin,)
            f.write("\n")
