
from .dbops import fetchData
import os, json


# fetch json data
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir = os.path.join(dir, 'data\\bar.json')


def writeJsontoFile(path, manner, data_dict):
    with open(path, manner) as file:
        json.dump(data_dict, file)

def readJsonfromFile(path, manner):
    with open(path, manner) as file:
        data = json.load(file)
    return data

def postJsonData(path, manner, data_list):
    data_dict = {}
    data_dict['data'] = []
    for i in data_list:
        data_dict['data'].append(i[1])
    writeJsontoFile(path, manner, data_dict)
    print('Json data updated.')

def getJsonData():
    data = readJsonfromFile(dir, 'r')
    '''
    for k, v in data.items():
        print(k, v)
    '''
    print('Json data fetched.')
    print(type(data), data)
    return data

def updateOverall():
    # write data fetched from db into line.json
    postJsonData(dir, 'w', fetchData())

    # read data from updated line.json
    json = getJsonData()

    return json
