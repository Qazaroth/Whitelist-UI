from flask import Blueprint, render_template, request, redirect, url_for, flash
from PropertiesHandler import PropertiesHandler

from utils.config import logo
from Forms import ServerPropertiesForm

bp = Blueprint("serverProperties", __name__)
ph = PropertiesHandler()

@bp.route("/properties")
def main():
    form = ServerPropertiesForm()
    properties = ph.getProperties()

    form.allowFlight.data = properties["allow-flight"]
    form.allowNether.data = properties["allow-nether"]

    return render_template("serverproperties/properties.html", logo=logo, form=form, data=properties)