from marshmallow import Schema, fields as field
from webargs.flaskparser import use_kwargs
from resources.base_resources import BaseResource
from utils.utilities import get_current_jwt_identity
from functionality.covid import send_covid_mail_with_graph
from utils.resource_exceptions import handle_exceptions


class CovidDataReport(BaseResource):
    decorators = [get_current_jwt_identity, handle_exceptions]

    @staticmethod
    def get(*args, **kwargs):
        response = send_covid_mail_with_graph(args[0], **kwargs)
        return response
