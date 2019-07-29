#ログファイルから時刻と領域、検出値のみ抽出する。

import re

#入力ファイルは"JobExecute.1.txt"
fr = open('C:\python\JobExecute.1.txt')
#出力ファイルは"logmod.txt"
fw = open('C:\python\logcsv.csv','w')

line = fr.readline()
while line:
    #tbpsOutputResult.c の列を検索
    if -1 != line.find('tbpsOutputResult.c'):
        if -1 != line.find('Threshold'):
            dline = line.split(' ')[1] + ',Threshold R,' + re.split('[(,)]',line)[-4] + '\n'
            fw.writelines(dline)
            dline = line.split(' ')[1] + ',Threshold G,' + re.split('[(,)]', line)[-3] + '\n'
            fw.writelines(dline)
            dline = line.split(' ')[1] + ',Threshold B,' + re.split('[(,)]', line)[-2] + '\n'
            fw.writelines(dline)
        elif -1 != line.find('Black Pixel Num'):
            dline = line.split(' ')[1] + ',High Density In Mesh,' + re.split('[(/,)]',line)[-9] + '\n'
            fw.writelines(dline)
            dline = line.split(' ')[1] + ',High Density In whole image,' + re.split('[(/,)]',line)[-7] + '\n'
            fw.writelines(dline)
            dline = line.split(' ')[1] + ',Middle Density at center,' + re.split('[(/,)]',line)[-5] + '\n'
            fw.writelines(dline)
            dline = line.split(' ')[1] + ',MiddleDensity near edge,' + re.split('[(/,)]',line)[-3] + '\n'
            fw.writelines(dline)
    elif -1 != line.find('tbpsMain() done.'):
        fw.writelines('e \n')
    line = fr.readline()

fr.close()
fw.close()
