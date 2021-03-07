import requests
from datetime import datetime


def get_covid_data(current_identity, **kwargs):
    country_code = kwargs.get('country_code')
    start_date = kwargs.get('start_date')
    end_date = kwargs.get('end_date')
    response = get_covid_data_based_country(country_code, start_date, end_date)
    return response


def get_covid_data_based_country(country, start_date, end_date):
    url = "http://corona-api.com/countries/{}".format(country)
    req = requests.get(url)
    response_json = req.json()
    data = response_json.get('data')
    filtered_response = []
    timeline = data.get('timeline')
    for cov_data in timeline:
        updated_date = cov_data.get('date')
        updated_date = datetime.strptime(updated_date, "%Y-%m-%d")

        if start_date <= updated_date.date() <= end_date:
            filtered_response.append(cov_data)

    response_dict = dict(coordinates=data.get('coordinates'), name=data.get('name'), code=data.get('code'),
                         population=data.get('population'), today=data.get('today'), latest_data=data.get('latest_data'),
                         timeline=filtered_response)
    return response_dict
