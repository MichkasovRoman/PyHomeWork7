def ReadDataFromFile(name):
    rawdata_list = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            rawdata_list.append(line.strip('\n').split(','))
        return rawdata_list

def SaveDataToFile(name, command):
    with open(name, 'a', encoding = 'utf8') as datafile:
        datafile.write(command + '\n')

def PrintBus():
    return ReadDataFromFile('bus.txt')

def AddBus():
    return SaveDataToFile('bus.txt', input('Введите данные автобуса: '))

def PrintDriver():
    return ReadDataFromFile('driver.txt')

def AddDriver():
    return SaveDataToFile('driver.txt', input('Введите данные вводителя: '))

def PrintRoute():
    return ReadDataFromFile('route.txt')

def AddRoute():
    return SaveDataToFile('route.txt', input('Введите данные маршрута: '))


