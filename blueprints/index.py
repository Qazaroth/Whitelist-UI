from flask import Blueprint, render_template

from utils.config import logo

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    # clientIP = request.remote_addr
    return render_template("index.html", title="Homepage", logo=logo)