import datetime as dt  #To take the time stamps
import requests

params = {
    'access_key': '59873ff6486674cd82bd2f78ec230836',
    'query': 'Dortmund',
    'historical_date_start' : '2015-01-01'
    , 'historical_date_end' : '2023-04-14'
}

api_result = requests.get('http://api.weatherstack.com/historical', params)

api_response = api_result.json()

print(api_response.keys())

print(api_response['success'])

#print(api_response)

#print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))
