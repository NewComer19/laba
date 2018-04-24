import pandas as pd
import glob
import urllib.request
import urllib.error
import datetime
import os
def state_id(id):
    S = [24, 25, 5, 6, 27, 23, 26, 7, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 8, 9, 10, 1, 3, 2, 4]
    return S[id - 1]
def get_state_name(id):
    if (id == 1):
        state = 'Винницкая область'
        return state

    elif (id == 2):
        state = 'Волныская область'
        return state

    elif (id == 3):
        state = 'Днепропетровская область'
        return state

    elif (id == 4):
        state = 'Донецкая область'
        return state

    elif (id == 5):
        state = 'Житомирская область'
        return state

    elif (id == 6):
        state = 'Закарпатская область'
        return state

    elif (id == 7):
        state = 'Запорожская область'
        return state

    elif (id == 8):
        state = 'Ивано-Франковская область'
        return state

    elif (id == 9):
        state = 'Киевская область'
        return state

    elif (id == 10):
        state = 'Кировоградская область'
        return state

    elif (id == 11):
        state = 'Луганская область'
        return state

    elif (id == 12):
        state = 'Львовская область'
        return state

    elif (id == 13):
        state = 'Николаевская область'
        return state

    elif (id == 14):
        state = 'Одесская область'

        return state
    elif (id == 15):
        state = 'Полтавская область'
        return state

    elif (id == 16):
        state = 'Ровно'
        return state

    elif (id == 17):
        state = 'Сумская область'
        return state

    elif (id == 18):
        state = 'Тернополь'
        return state

    elif (id == 19):
        state = 'Харьковская область'
        return state

    elif (id == 20):
        state = 'Херсонская область'
        return state

    elif (id == 21):
        state = 'Хмельницкий'
        return state

    elif (id == 22):
        state = 'Черкасская область'
        return state

    elif (id == 23):
        state = 'Черновцы'
        return state

    elif (id == 24):
        state = 'Черниговская область'
        return state

    elif (id == 25):
        state = 'Крым'
        return state

def download(ident):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+str(ident)+"&year1=1981&year2=2018&type=Mean"
    vhi_url = urllib.request.urlopen(url)
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = open('vhi_id_%02d.csv' % ident, 'wb')
    out.write(vhi_url.read())
    out.close()
    os.rename('vhi_id_%02d.csv' % ident, 'downloaded_at_' + now + '_vhi_id_%02d.csv' % ident)
    print("VHI is downloaded...")


for ident in range(1, 28):
    download(ident)

def VHI(rs, year):
        path = r"C:\Users\galey\PycharmProjects\laba1"
        allFiles = glob.glob(path + "/*"+str(state_id(rs))+".csv")
        for file in allFiles:
            df = pd.read_csv(file, header=1, names=['DATE','SMT','VCI','TCI','VHI'],  delimiter=',')
            df = df.dropna()

            df['YEAR'], df['WEEKSMN'] = df['DATE'].str.split(' ', 1).str
            df['WEEK'], df['SMN'] = df['WEEKSMN'].str.split(' ', 1).str
            del df['DATE']
            del df['WEEKSMN']
            df = df[['YEAR', 'WEEK', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI']]

        print('Минимальный VHI для ' + get_state_name(rs) + ': ' + str(df[df['YEAR'] == str(year)]['VHI'].min()) + " за " +str(year) + " год")
        print('Максимальный VHI для ' + get_state_name(rs) + ': ' + str(df[df['YEAR'] == str(year)]['VHI'].max()) + " за " +str(year) + " год")
        print('VHI < 15% за все время')
        df = df[(df['YEAR'] != 0) & (df['VHI'] < 15)]
        print (df)


VHI(2, 2004)


