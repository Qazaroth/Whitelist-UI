from flask import Blueprint, render_template, request, redirect, url_for, flash
from WhitelistHandler import WhitelistHandler

from config import logo

bp = Blueprint("main", __name__)

whHandler = WhitelistHandler()

@bp.route("/add", methods=["GET", "POST"])
def addUser():
    msg = ""
    if request.method == "POST":
        uname = request.form["username"]

        isSuccess = whHandler.addToWhitelist(uname)

        if isSuccess:
            msg = "Successfully added \"{}\" to whitelist!".format(uname)
        else:
            msg = "Error occured while adding \"{}\" to whitelist!".format(uname)
    
    whHandler.updateWhitelist()
    
    return render_template("addUser.html", title="Add User", logo=logo, msg=msg)

@bp.route("/remove/<target>")
def removeUser(target):
    isSuccess = whHandler.removeFromWhitelist(target)

    if isSuccess:
        flash("Successfully removed {} from whitelist!".format(target))
    else:
        flash("Unable to remove {} from whitelist!".format(target))

    whHandler.updateWhitelist()

    return redirect(url_for("main.home"))

@bp.route("/")
def home():
    # clientIP = request.remote_addr
    whitelistData = whHandler.getWhitelistData()
    return render_template("index.html", title="Homepage", data=whitelistData, logo=logo)