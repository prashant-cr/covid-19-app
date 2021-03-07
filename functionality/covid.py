import requests
import pycountry
import datetime as dt


from datetime import datetime
from models import session
from utils.log_handler import function_logger
from models.users import User
from constants.common_constants import DEFAULT_FALSE_FLAG


@function_logger
def get_user_country_by_id(user_id=None):
    user_obj = session.query(User.country).filter(
        User.id == user_id,
        User.is_deleted == DEFAULT_FALSE_FLAG
    ).first()
    return user_obj


@function_logger
def get_covid_data(current_identity, **kwargs):
    country_code = kwargs.get('country')
    if not country_code:
        country_name = get_user_country_by_id(current_identity)[0]
        country_code_temp = pycountry.countries.search_fuzzy(country_name)[0]
        country_code = country_code_temp.alpha_2
    start_date = kwargs.get('start_date')
    end_date = kwargs.get('end_date')
    if not start_date and not end_date:
        today = datetime.now()
        end_date = today.date()
        start_date_temp = today - dt.timedelta(days=7)
        start_date = start_date_temp.date()

    response = get_covid_data_based_country(country_code, start_date, end_date)
    return response


@function_logger
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
