from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_restful import fields, marshal_with
from marshmallow import Schema, fields as field
from webargs.flaskparser import use_kwargs
from functionality.login import validate_user
from resources.base_resources import BaseResource
from utils.utilities import get_current_jwt_identity
from functionality.covid import get_covid_data


class CovidRequestFormat(Schema):
    country_code = field.Str(required=False)
    start_date = field.Date(required=False)
    end_date = field.Date(required=False)

    class Meta:
        strict = True


class CovidData(BaseResource):
    decorators = [get_current_jwt_identity]

    @use_kwargs(CovidRequestFormat)
    def post(self, *args, **kwargs):
        response = get_covid_data(args[0], **kwargs)
        return response
