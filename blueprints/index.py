from flask import Blueprint, render_template, request
from WhitelistHandler import WhitelistHandler

bp = Blueprint("main", __name__)

whHandler = WhitelistHandler()

@bp.route("/")
def home():
    # clientIP = request.remote_addr
    whitelistData = whHandler.getWhitelistData()
    return render_template("index.html", title="Homepage", data=whitelistData)