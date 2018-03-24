# fill in the params dictionary, write functions to update it
# with the entered arguments to __init__, write functions
# to get_all_records and store results as a dataframe.
# have all functions run during init so that the initialized
# object calls the request and returns a full dataframe. 

import toyplot
import requests
import pandas as pd
    
class Record:
    
    def __init__(self, q=None, interval=None):
        
        self.q = q
        self.interval = interval
        self.params = {}
        self.data = {}
        self.df = {}
        self._get_all_records()
    
    def _get_all_records(self):
        "iterate until end of records"
        start = 0
        data = []
        
        # define base URL
        baseurl = "http://api.gbif.org/v1/occurrence/search?"
        
        # eliminate brackets on interval
        interval2 = str(self.interval[0])+","+str(self.interval[1])
        
        searchparams = {
            "q": str(self.q), 
            "year": interval2, 
            "offset": "0",
            "limit": "300"
        }

        # run loop infinitely untill it gets break command (same as while True)
        while 1:
            # make request and store results
            res = requests.get(
                url=baseurl, 
                params=searchparams,
            )
            # increment counter
            searchparams["offset"] = str(int(searchparams["offset"]) + 300)

            # concatenate data 
            idata = res.json()
            data += idata["results"]

            # stop when end of record is reached
            if idata["endOfRecords"]:
                break
                
            self.data = data
            self.df = pd.DataFrame(self.data)

        return data