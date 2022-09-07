from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.ticket import Ticket

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

#==========================================
#Register / Login Routes 
#==========================================

@app.route("/register" , methods=["POST"])
def register():
    #1 validating form information
    data={
        "first_name" : request.form["first_name"], 
        "last_name" : request.form["last_name"], 
        "email" : request.form["email"], 
        "password" : request.form["password"], 
        "pass_conf" : request.form["pass_conf"]
    }
    
    if not User.validate_register(data):
        return redirect("/")
    
    #2 - bcrypt password
    data["password"] = bcrypt.generate_password_hash(request.form['password'])

    #3 - save new user to db 

    new_user_id = User.create_user(data)

    #4 enter user into session and redirect into dashboard
    session["user_id"] = new_user_id
    return redirect("/dashboard")

#========================
#LOGIN METHODS BELOW 
#=========================
@app.route("/login", methods=["POST"])
def login():
    #1 validate login info 
    data ={
        "email" : request.form["email"],
        "password" : request.form["password"]
    }
    if not User.validate_login(data):
        return redirect("/")

    #2 query for user info based on email 

    user = User.get_by_email(data)

    #3 put user id into session and redirect into dashboard
    session["user_id"] = user.id
    return redirect("/dashboard")

#===============================
# RENDER DASHBOARD ROUTE
#================================
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please login or register before entering the site!")
        return redirect("/")

    data = {
        "user_id" : session["user_id"]
    }

    user = User.get_by_id(data)
    all_tickets = Ticket.get_all()
    return render_template("dashboard.html", user = user, all_tickets = all_tickets)
    


#===============================
# LOGOUT ROUTE
#================================

@app.route("/logout")
def logout():
    session.clear()
    flash("Successfully logged out!")
    return redirect('/')

#================================
#ROUTE TO CREATE TICKET PAGE FROM DASH TO CREATE PAGE 
#=================================

@app.route("/tickets/new")
def go_to_create():
    return render_template('create.html')

#=================================
#POST INFO TO DATABASE AND REDIRECT POST BACK TO DASHBOARD 
#===================================
@app.route("/tickets/new", methods = ['POST'])
def add_ticket():
    #create ticket on SQL 

    #data object
    data = {
        "problem" : request.form["problem"],
        "description" : request.form['description'],
        "urgency" : request.form["urgency"],
        "screen_q" : request.form["screen_q"],
        "expectations" : request.form["expectations"],
        "user_id" : session["user_id"],
    }

#VALIDATION CREATE PAGE HERE 
    if not Ticket.validate_create(data):
        return redirect(f"/tickets/new")

    new_ticket = Ticket.create_ticket(data)
    return redirect (f'/dashboard')

#=======================
#ROUTE FROM DASHBOARD TO EDIT PG
#========================
@app.route('/tickets/<int:ticket_id>/edit')
def edit_page(ticket_id):
    data = {
        "id" : ticket_id,
    }
    ticket = Ticket.show_ticket(data)
    return render_template('edit.html', ticket = ticket)

#=======================
#UPDATE AND THEN REDIRECT TO DASHBOARD 
#=======================
@app.route('/tickets/<int:ticket_id>/edit', methods = ['POST'])
def ticket_edit(ticket_id):
    data = {
        "problem" : request.form["problem"], 
        "description" : request.form["description"],
        "urgency" : request.form["urgency"],
        "screen_q" : request.form["screen_q"],
        "expectations" : request.form["expectations"],
        "user_id" : session["user_id"], 
        "id" : ticket_id,
    }
    if not Ticket.validate_create(data):
        return redirect("/tickets/<int:ticket_id>/edit")
    
    print(data)
    Ticket.edit_ticket(data)
    return redirect('/dashboard')

#==================================
#ROUTE TO ONE PAGER / SHOW PAGE 
#==================================
@app.route('/tickets/<int:ticket_id>')
def goto_showpage(ticket_id):
    data = {
        "id" : ticket_id
    }
    thisuser = {
        "user_id" : session['user_id']
    }

    user = User.get_by_id(thisuser)
    ticket = Ticket.one_ticket(data)
    return render_template('show.html', ticket = ticket, user = user)

#=================================
#DELETE TICKET 
#=================================
@app.route('/delete/<int:ticket_id>')
def remove_ticket(ticket_id):
    data = {
        "ticket_id" : ticket_id
    }
    Ticket.delete_ticket(data)
    return redirect('/dashboard')

