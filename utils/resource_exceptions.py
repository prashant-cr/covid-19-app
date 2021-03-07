from functools import wraps
from flask_restful import abort
from werkzeug.exceptions import UnprocessableEntity

from flask import current_app as app
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import session


def handle_exceptions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ValueError as val_err:
            app.logger.error(val_err)
            session.rollback()
            return abort(400, message=str(val_err))
        except KeyError as key_err:
            app.logger.error(key_err)
            session.rollback()
            return abort(400, message=str(key_err))
        except IOError as io_err:
            app.logger.error()
            session.rollback()
            return abort(500, message=str(io_err))
        except IntegrityError as err:
            app.logger.error(err)
            session.rollback()
            return abort(500, message="Integrity-Error")
        except SQLAlchemyError as sa_err:
            app.logger.error(sa_err)
            session.rollback()
            return abort(500, message="SQLAlchemy Error")
        except UnprocessableEntity as sa_err:
            app.logger.error(sa_err)
            try:
                message = sa_err.data.get("messages", None)
            except Exception as sa_err:
                message = sa_err.message
            session.rollback()
            return abort(422, message=message)
        except Exception as exc:
            app.logger.error(exc)
            session.rollback()
            return abort(500, message=exc.message)

    return wrapper
