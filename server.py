from flask import Flask, session, redirect, request, render_template
import random
import datetime


app = Flask(__name__)
app.secret_key = 'totallytopsecret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
        session['activities'].insert(0,"Game Began")

    return render_template('index.html', gold=session['gold'], activities=session['activities'])

@app.route("/process_money", methods=["POST"])
def get_gold():

    if request.form["action"] == "farm":
        go_gold = random.randrange(1,3)
        if go_gold == 1:
            goldval = random.randrange(1,9)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "You've farmed %s gold (%s)" %(str(goldval),timestamp)
            session["activities"].append(event_log)
            session.modified = True
            session["gold"] += goldval
        if go_gold == 2:
            goldval = random.randrange(1,9)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= " You lost %s gold (%s)" %(str(goldval),timestamp)
            session["activities"].append(event_log)
            session["gold"] -= goldval

    if request.form["action"] == "cave":
        go_gold = random.randrange(1,3)
        if go_gold == 1:
            goldval = random.randrange(0,11)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= " You've found some treasure! Found %s gold!  (%s)" %(str(goldval),timestamp)
            session["activities"].append(event_log)
            session["gold"] += goldval
        if go_gold == 2:
            goldval = random.randrange(1,11)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= " You lost %s gold (%s)" %(str(goldval),timestamp)
            session["activities"].append(event_log)
            session["gold"] -= goldval

    if request.form["action"] == "house":
        go_gold = random.randrange(1,3)
        if go_gold == 1:
            goldval = random.randrange(2,6)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "Earned %s at home. (%s)" %(str(goldval),timestamp)
            session["activities"].append(event_log)
            session["gold"] += goldval
        if go_gold == 2:
            goldval = random.randrange(2,5)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= " Lost %s gold (%s)" %(str(goldval),timestamp)
            session["activities"].append(event_log)
            session["gold"] -= goldval

    if request.form["action"] == "casino":
        go_gold = random.randrange(1,3)
        if go_gold == 1:
            goldval = random.randrange(10,101)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "Won %s gold from the casino!(%s)" %(str(goldval),timestamp)
            session["activities"].append(event_log)
            session["gold"] += goldval
        
        if go_gold == 2:
            goldval = random.randrange(10,101)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= " House wins! %s  (%s)" %(str(goldval),timestamp)
            session["activities"].append(event_log)
            session["gold"] -= goldval
        


    return redirect("/")

@app.route("/restart")
def restart_game():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)