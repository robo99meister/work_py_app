#ログファイルから時刻と領域、検出値のみ抽出する。
#入力ファイルは"JobExecute.1.txt"
fr = open('C:\python\JobExecute.1.txt')
#出力ファイルは"logmod.txt"
fw = open('C:\python\logcsv.csv','w')

new_line_flag = 0

line = fr.readline()
while line:
    #Detect Toner in の列を検索
    dcount = line.find('Detect Toner in')
    if -1 != dcount:
        #Detect Toner in 後の文字列を抽出
        sline = line[dcount +16:]
        #/までの領域でエリア情報を抽出
        slcount = sline.find('/')
        if -1 != slcount:
            #スペース区切りで2個目に時間情報、,区切りで後ろから3個目に検出数
            dline = line.split(' ')[1] + ',' + sline[: slcount -1]  + ',' + sline.split(',')[-3] + '\n'
            fw.writelines(dline)
            new_line_flag = 1
    elif -1 != line.find('tdtrMain() done.') and new_line_flag == 1:
        fw.writelines('\n')
        new_line_flag = 0
    line = fr.readline()

fr.close()
fw.close()
