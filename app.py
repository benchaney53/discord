from flask import Flask, render_template, request
import os
import discord

from discord.ext import commands

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/discord")
def discord():
    return render_template("discord.html")

@app.route("/join", methods=["POST"])
def join():
    server_id = request.form["server_id"]
    return f"Joining server with ID {server_id}"

if __name__ == "__main__":
    app.run(debug=True)
