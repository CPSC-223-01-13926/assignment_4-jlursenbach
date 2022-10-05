#!/usr/bin/env python3

"""
Author: Jacob Ursenbach
Purpose: CPSC 223
Creation Date: 20221005

Description:

This module uses the weather dictionary:

weather dictionary:
   key : datetime as string (formatted as YYYYMMDDhhmmss)
   value : readings dictionary

readings dictionary
   for key : 't'
   value : temperature as integer

   for key : 'h'
   value : humidity as integer

   for key : 'r'
   value : rainfall as float

   ex:
   "20210203075501": {"t": 55, "h": 87, "r": 0}
"""
import calendar
import json
import


def read_data(filename: str)-> dict:
    """
    reads data from a file
    decripts the json into a python dict
    if error, returns an empty dictionary

    :param filename: name of file to be read
    :return: dict conntaning json contents
    """

    try:

        with open(filename, r) as file:
            return json.load(file)

    except FileNotFoundError as e:

        print(f"ERROR: {e} \n"
              f"File: {filename} not found")

        return {}

def write_data(data: dict, filename: str) -> None:
    """
    Takes in a dict contaning data:

    :param data: python dict contaning data
    :param filename:
    :return:
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

# FixMe
def max_temperature(data: dict, date: str) -> int:
    """
    temperature assumed to be in Celcius
    :param data:
    :param date:
    :return:
    """
    max_temp = 0

    for dateKey, readings in data:

        if dateKey[0:8] == date:
        print(dateKey[0:8])

            if readings['t'] > max_temp:
                max_temp = readings['t']

    return max_temp


def min_temperature(data, date):
    x = 999
    for key in data:
        if data == key[0:8]:
            if data[key]['t'] < x:
                x = data[key]['t']
    return x

def max_humidity(data, date):
    x=0
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] > x:
                x = data[key]['h']
    return x

def min_humidity(data, date):
    x=9999
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] < x:
                x = data[key]['h']
    return x

def tot_rain(data, date):
    rainfall = 0
    for key in data:
        if date == key[0:8]:
            rainfall += data[key]['r']

def report_daily(data, date):
    """
    output format:

    ========================= DAILY REPORT ========================
    Date                      Time  Temperature  Humidity  Rainfall
    ====================  ========  ===========  ========  ========
    February 3, 2021      07:55:01           55        87      0.00
    February 3, 2021      09:06:02           63        84      0.00
    February 3, 2021      10:29:03           71        79      0.00
    February 3, 2021      12:55:04           72        69      0.00
    February 3, 2021      18:39:05           59        75      0.00

    :param data:
    :param date:
    :return: str
    """

    header = '========================= DAILY REPORT ========================\n'
             'Date                      Time  Temperature  Humidity  Rainfall\n'
             '====================  ========  ===========  ========  ========\n'

    body = ''

    date_str = calendar.month_name[int(date[4:6])] + '' + \
               calendar.month_name[int(date[6:8])] ', ' + \
               str(int date[0:4])

    for key in data:
        if date == key[0:8]:
            time = key[8:10] + ':' key[10:12] + ':' key[12:14]

            temp = data[key]['t']
            humidity = data[key]['h']
            rainfall = data[key]['r']

            body += f'{date_str: 22}{time: 8}{temp: 13}{humidity: 10}{rainfall: 10: 2f}\n'

    return header += body

    def report_historical(data):

        header = '============================== HISTORICAL REPORT =========================== \n'
                 '			                Minimum      Maximum   Minumum   Maximum     Total \n'
                 'Date                  Temperature  Temperature  Humidity  Humidity  Rainfall \n'
                 '====================  ===========  ===========  ========  ========  ======== \n'



if __name__ == '__main__':
    data = read_data("w.dat")
    print(max_temperature(data, "20210203"))

