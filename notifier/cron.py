from webpush import send_group_notification
import requests
from .models import covidData

indiaapi = "https://corona.lmao.ninja/countries/india"


def callAPI():
    r = requests.get(url=indiaapi)
    data = r.json()
    savedData = covidData.objects.get(id=1)
    prev = savedData.cases

    payload = {"head": "COVID-19 update!", "body": data['cases']}
    if(data['cases'] != prev):
        savedData.cases = data['cases']
        savedData.save()
        savedData.publish()
        send_group_notification(group_name="kanishka",
                                payload=payload, ttl=1000)
