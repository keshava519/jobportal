import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/hydjobsinfo/'
response=requests.get(BASE_URL+ENDPOINT)
data=response.json()
for job in data:
    print('Date:', job['date'])
    print('Company Name:', job['company'])
    print('Company Title:', job['title'])
    print('Eligibility:', job['eligibility'])
    print('Email Address:', job['email'])
    print('Phone Number:', job['phonenumber'])
    print('Company Address:', job['address'])
    print()
