import pandas as pd
import os
import errno
import re
from sklearn.cluster import KMeans 
import matplotlib.pyplot as mtp 

def read_dataset(dataset_filepath):
    if os.path.exists(dataset_filepath):
        Hair_care_dataset = pd.read_excel(dataset_filepath)
        return Hair_care_dataset
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), dataset_filepath)

def write_file_to_csv_with_filename(data,filename):
    try:
        data.to_csv(filename, sep=',', encoding='utf-8')
        return "Save file success"
    except Exception as e:
        raise e

def extract_volume_from_string(title_string='Cultusia Hairmask Olive Oil 25Ml (3Pcs)'):
    if(title_string):
        volume_string = '\d+\s?(?:ml|liter|gr|kg|)'
        result = re.findall(volume_string, title_string,re.I)
        return result[0] if len(result)> 0  else ''
    return ''

def scaling_volume_data(string_data):
    if len(string_data)>0:
        string_data = string_data.lower()
        if('kg' in string_data):
            res = eval(string_data.lower().replace('kg','* 1000'))
            return res
        if('ml' in string_data):
            res = eval(string_data.lower().replace('ml','* 1'))
            return res
        if('liter' in string_data):
            res = eval(string_data.lower().replace('liter','* 1000'))
            return res
        if('gr' in string_data):
            res = eval(string_data.lower().replace('gr','* 1'))
            return res
        if('g' in string_data):
            res = eval(string_data.lower().replace('g','* 1'))
            return res
        return string_data
    else:
        return 0

def get_all_volumes_from_titles(dataframe, column_name = 'Title'):
        dataframe['Volume'] = dataframe[column_name].apply(lambda x: extract_volume_from_string(x))
        return dataframe

def extract_quantity_from_string(title_string='Cultusia Hairmask Olive Oil 25Ml (3Pcs)'):
    if(title_string):
        packet_string_1 = 'paket\s+\w+\s+\d+'
        packet_string_2 = 'packet\s+\w+\s+\d+'
        packet_string_3 = 'pack\s+\w+\s+\d+'
        packet_string_4 = 'packet\s+\w+\s+\d+'
        packet_string_5 = '\d+\s+pcs|\d+pcs'
        packet_string_6 = '\d+\s+pack'
        packet_string_7 = '\d+\s+packs'
        packet_string_8 = '\d+\s+bottle'
        packet_string_9 = '\d+\s+botol'
        packet_string_10 = '\d+\s+sachet'
        packet_string_13 = '\d+\s+Capsule'
        packet_string_11 = 'Sachet|Paket|Pouch|Box|bottle|pot|Twin Pack'
        list_of_quantity_string = [packet_string_1,packet_string_2,packet_string_3,packet_string_4,packet_string_5,packet_string_6,packet_string_7,packet_string_8,packet_string_9,packet_string_10,packet_string_11, packet_string_13]
        result = re.findall("|".join(list_of_quantity_string), title_string,re.I)
        return result[0] if len(result)> 0  else ''
    return ''

def scaling_quantity_data(string_data):
    if (string_data):
        res = [int(i) for i in string_data.split() if i.isdigit()]
        if len(res) == 0:
            qty = []
            res = [qty.append(i) for i in string_data if i.isdigit()]
            return ''.join(qty)
        return res[0]
    return 1

def get_all_quantity_from_titles(dataframe):
    dataframe['Quantity'] = dataframe["Title"].apply(lambda x: extract_quantity_from_string(x))
    return dataframe

def scale_the_data(dataframe):
    dataframe['Volume'] = dataframe['Volume'].apply(lambda x: scaling_volume_data(x))
    dataframe['Quantity'] = dataframe["Quantity"].apply(lambda x: scaling_quantity_data(x))
    return dataframe

def get_Hair_care_dataset_with_quantity_and_volume_by_title(dataset):
    dataframe = get_all_volumes_from_titles(dataset)
    dataframe = get_all_quantity_from_titles(dataframe)
    dataframe = scale_the_data(dataframe)
    print("shape of result dataframe -> ",dataframe.shape)
    print("Describe of result dataframe -> ",dataframe.describe())
    return dataframe

def convert_to_numeric_data(data):
    data[["Volume"]] = data[["Volume"]].apply(pd.to_numeric)
    data[["Quantity"]] = data[["Quantity"]].apply(pd.to_numeric)
    return data

def drop_na(data, array_of_column_name):
    data = data[array_of_column_name].dropna()
    return data

def binning_the_data(result):
    volume_quantile = pd.qcut(result['Volume'], q=5)
    SalePrice_quantile = pd.qcut(result['SalePrice'], q=5)
    print("Binned Volume", volume_quantile)
    print("Binned Sale Price", SalePrice_quantile)