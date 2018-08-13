# -*- coding: utf-8 -*-
import urllib.request
import json

sheetId = '11BCnspCt2Mut3nhc4WMY6CYTd0zF9C3eCzsk1AEpKLM'
range = 'sales!A1:E6'
api_key = ''
with urllib.request.urlopen("https://sheets.googleapis.com/v4/spreadsheets/"
                            + sheetId +"/values/" + range + "?key=" + api_key) as res:
    json = json.loads(res.read().decode("utf-8"))
    for columns in json['values']:
        str = ''
        for value in columns:
            str += '\'' + value + '\'' + ','
        print(str)