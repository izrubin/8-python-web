#!/usr/bin/env python

import requests
import pandas as pd

class Record:
    def __init__(self, q=None, interval=None):
        
        self.q = q
        self.interval = interval
        self.params = {}
        self.df = self._get_all_records()
    
    def _get_all_records(self):
        "Iterates until the end of records and returns the data"
        start = 0
        data = []
        self.params = {
        "q": self.q, 
        "year": self.interval, 
        "basisOfRecord": "PRESERVED_SPECIMEN",
        "hasCoordinate": "true",
        "hasGeospatialIssue": "false",
        "country": "US",
        "offset": "0",
        "limit": "300",
        }
        while 1:
            # make requests and store results
            res = requests.get(
                url = "http://api.gbif.org/v1/occurrence/search?",
                params = self.params,            
            )
            # increment counter
            self.params["offset"] = str(int(self.params["offset"]) + 300)
        
            # concatenate data 
            idata = res.json()
            data += idata["results"]
        
            # stop when end of record is reached
            if idata["endOfRecords"]:
                break
       
        return pd.DataFrame(data)
    