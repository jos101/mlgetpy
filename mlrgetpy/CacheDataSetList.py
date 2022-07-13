from dataclasses import dataclass, field
import pickle

@dataclass
class CacheDataSetList:

    def save_object(self, obj, filename):
        with open(filename, 'wb') as outp: 
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

    def getCache(self):
        list_response = []
        try:
            with open('response.pkl', 'rb') as inp:
                list_response = pickle.load(inp)
                response = list_response[0]
        except:
            list_response = [None, None]

        return list_response

    
