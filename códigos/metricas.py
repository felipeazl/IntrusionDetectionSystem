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

    NMSE = np.subtract(total_len_arr, wma)
    NMSE = np.square(NMSE)
    NMSE = np.mean(NMSE)
    NMSE = NMSE / np.var(total_len_arr)
    NMSE = round(NMSE, 2)
    return NMSE

def cal_mape():
    with open("fullData.json") as f:
        data = json.load(f)

    wma = WMA.gera_list_wma()

    total_len_arr = []
    for i in data:
        obj = data[i]
        if "total_len" in obj:
            total_len_arr.append(obj["total_len"])

    MAPE = np.abs(np.subtract(total_len_arr, wma))
    MAPE = np.divide(MAPE, total_len_arr)
    MAPE = [x * 100 for x in MAPE]
    MAPE = np.mean(MAPE)
    MAPE = round(MAPE, 2)
    return MAPE
