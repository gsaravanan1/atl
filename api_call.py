import requests
api_key='1f0da8963a983c9e8c378b5c0265be33'
class weatherapi:
    def __init__(self,api_key,url) -> None:
        self.api_key=api_key
        self.url=url
    def fetchdata(self,city):
       
        param ={
            'q':city,
            'appid':self.api_key,
            'units':'metric'
        }
        resp=requests.get(self.url)
        data=resp.json()
        return data
    def transformdata(data):
        city=data['name']
        temp=data['main']['temp']
        humidity=data['main']['temp']
        return [city,temp, humidity]

    def getweatherreport(self,cities, api_key):
        results=[]
        for city in cities:
            data=self.fetchdata(city, self.api_key)
            transformed=self.transformdata(data)
            results.append(transformed)
        return results

weathercall=weatherapi(api_key=api_key, url='https://api.openweathermap.org/data/2.5/weather')

print(weathercall.fetchdata(city='London,uk'))

