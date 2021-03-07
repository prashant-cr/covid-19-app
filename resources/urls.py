from flask_admin import Admin
from flask_restful import Api
from models import session
from models.admin_model import ModelView
from models.users import User
from resources.login import Login, Refresh
from resources.sign_up import SignUp
from resources.covid import CovidData


def restful_api(app):
    api = Api(app, prefix="/api/v1")
    api.add_resource(SignUp, '/signup', strict_slashes=False)
    api.add_resource(Login, '/login', strict_slashes=False)
    api.add_resource(Refresh, '/refresh', strict_slashes=False)
    api.add_resource(CovidData, '/covid', strict_slashes=False)

    # admin
    admin = Admin(app, template_mode='bootstrap3')
    admin.add_view(ModelView(User, session))


