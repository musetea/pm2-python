import requests, datetime
from bs4 import BeautifulSoup #To install: pip3 install beautifulsoup4
import sys
from os import makedirs
from os import path

class Covid19:
    def __init__(self, version:str) -> None:
        self.version = version
        self.url = "https://www.worldometers.info/coronavirus/"

    def run(self):
        try:
            req = requests.get(self.url)
            if req.status_code != 200:
                print(f"{req.status_code} 요청오류!!!")
                return
        except requests.exceptions.Timeout as errd:
            print("Timeout Error : ", errd)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting : ", errc)
        except requests.exceptions.HTTPError as errb:
            print("Http Error : ", errb)
        # Any Error except upper exception
        except requests.exceptions.RequestException as erra:
            print("AnyException : ", erra)

        if req is None:
            return
        
        bsObj = BeautifulSoup(req.text, "html.parser")
        data = bsObj.find_all("div",class_ = "maincounter-number")
        if len(data) != 3:
            print(f"{len(data)} 데이터 배열 갯수 오류")

        NumTotalCase=0
        if isinstance(data[0],str):
            if data[0]:
                NumTotalCase = int(data[0].text.strip().replace(',', ''))
        
        NumDeaths = 0
        if isinstance(data[1],str):
            if data[1]:
                NumDeaths = int(data[1].text.strip().replace(',', ''))

        NumRecovered:int=0
        if isinstance(data[2],str):
            if data[2]:
                NumRecovered = int(data[2].text.strip().replace(',', ''))
            
        TimeNow = datetime.datetime.now()

        nameCsv: str = 'world_corona_case'
        fileName:str = f"{self.version}\{nameCsv}.csv"
        with open(fileName,'a') as fd:
            fd.write(f"{TimeNow},{NumTotalCase},{NumDeaths},{NumRecovered};\n")
        
        print(f"Successfully store COVID-19 data at {TimeNow}")




if __name__ == "__main__":

    version:str =  sys.version.split(" ")[0].replace(".", "").strip()
    baseDir:str = f"./{version}/"
    if not path.exists(baseDir):
        try:
            makedirs(baseDir)
        except OSError as e:
            print(e)

    
    corvid =  Covid19(version=version)
    corvid.run()




