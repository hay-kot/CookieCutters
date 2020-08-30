import flask
from infrastructure.view_modifiers import response
from services import package_service

blueprint = flask.Blueprint("home", __name__, template_folder="templates")


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    return {"packages": package_service.get_latest_packages()}
