import os
import codecs
import re


txtpath = './data/applenews'
# keywords = ['桃園捷運', '機場捷運', '台北捷運', '新北捷運', '雙北捷運',
#             '台中捷運', '高雄捷運', '桃捷', '機捷', '北捷', '中捷', '高捷', '捷運']
info_list = []

files = os.listdir(txtpath)
total = len(files)
for idx, file in enumerate(files):
    f = codecs.open(txtpath + '/' + file, 'r', 'utf-8')
    txtinfo = ''
    lines = f.readlines()
    print('%.2f%%' % (idx/total * 100))
    titleDspace = re.sub(r'\([^)]*\)', '', lines[0])
    txtinfo += 'Apple_News,'
    txtinfo += '"' + titleDspace.replace('\u3000',
                                   ' ').replace('\n', '').split('Title')[1].strip(' : ') + '"' + ','
    dateDspace = re.sub(r'\([^)]*\)', '', lines[2]).replace('　', '')
    txtinfo += dateDspace.replace('\u3000',
                                  ' ').replace('\n', '').split('Date:')[1] + ','
    urlDspace = re.sub(r'\([^)]*\)', '', lines[7]).replace('　', '')
    txtinfo += urlDspace.replace('\u3000', ' ').replace('\n',
                                                        '').replace('＆', '&').split('Url:')[1]

    info_list.append(txtinfo)


w = codecs.open('./ckipnewsinfo/Apple_News.csv', 'w', 'utf-8')
w.write('Board,Title,Date,Url\n')
for item in info_list:
    w = codecs.open('./ckipnewsinfo/Apple_News.csv', 'a+', 'utf-8')
    w.write(item + '\n')
