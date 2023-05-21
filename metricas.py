import json
import numpy as np
import wma as WMA

def cal_nmse():
    with open("fullData.json") as f:
        data = json.load(f)

    wma = WMA.gera_list_wma()

    total_len_arr = []
    for i in data:
        obj = data[i]
        if "total_len" in obj:
            total_len_arr.append(obj["total_len"])

    NMSE = np.subtract(wma, total_len_arr)
    NMSE = np.square(NMSE)
    NMSE = np.sum(NMSE)
    NMSE = NMSE / len(wma)
    NMSE = np.sqrt(NMSE)
    NMSE = NMSE / np.mean(total_len_arr)
    NMSE = round(NMSE, 2)
    return NMSE

def cal_mape():
    with open("fullData.json") as f:
        data = json.load(f)

    wma = WMA.gera_list_wma()

    count_arr = []
    for i in data:
        obj = data[i]
        if "count" in obj:
            count_arr.append(obj["count"])

    MAPE = np.subtract(wma, count_arr)
    MAPE = np.abs(MAPE)
    MAPE = np.divide(MAPE, count_arr)
    MAPE = np.sum(MAPE)
    MAPE = MAPE / len(wma)
    MAPE = MAPE * 100
    MAPE = round(MAPE, 2)
    return MAPE