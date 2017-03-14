sample = '''
{
    "response_code": 200,
    "pnr": "6224484662",
    "train_num": "12311",
    "train_name": "HWH DLI KLK MAI",
    "doj": "23-12-2013",
    "from_station": {
        "code": "DLI",
        "name":"Delhi"
    },
    "to_station": {
        "code": "KLK",
        "name":"Kalka"
    },
    "reservation_upto": {
        "code": "KLK",
        "name":"Kalka"`
    },
    "boarding_point": {
        "code": "DLI",
        "name":"Delhi"
    },
    "class": "1A",
    "no_of_passengers": 3,
    "chart_prepared": "N",
    "passengers": [
        {
            "sr": "1",
            "booking_status": "CNF  ,GN",
            "current_status": "CNF"
        },
        {
            "sr": "2",
            "booking_status": "W/L    1,RLGN",
            "current_status": "W/L    1"
        },
        {
            "sr": "3",
            "booking_status": "W/L    2,RLGN",
            "current_status": "W/L    2"
        }
    ],
    "error": null
}
'''

FORMAT = '''
{
    "response_code": 200,
    "pnr": "",
    "train_num": "",
    "train_name": "",
    "doj": "",
    "from_station": {
        "code": "",
        "name":""
    },
    "to_station": {
        "code": "",
        "name":""
    },
    "reservation_upto": {
        "code": "",
        "name":""
    },
    "boarding_point": {
        "code": "",
        "name":""
    },
    "class": "",
    "no_of_passengers": 3,
    "chart_prepared": "N",
    "passengers": [
        {
            "sr": "1",
            "booking_status": "CNF  ,GN",
            "current_status": "CNF"
        },
        {
            "sr": "2",
            "booking_status": "W/L    1,RLGN",
            "current_status": "W/L    1"
        },
        {
            "sr": "3",
            "booking_status": "W/L    2,RLGN",
            "current_status": "W/L    2"
        }
    ],
    "error": null
}
'''

import json;
import random;

class ResponseGenerator:

    def __init__(self):
        self.data = dict();

        return;

    def genRandom(self):

        return(self.data);

    def getSample(self):
        global sample;
        return(sample);

    def toJSON(self):
        op = str();
        try:
            op = json.dumps(self.data);
        except json.JSONDecodeError:
            print("[ERROR] Could not decode",self.data);
            op = None;
        return(op);

if __name__ == "__main__":
    exit();