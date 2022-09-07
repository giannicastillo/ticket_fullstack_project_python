from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Ticket:
    def __init__(self,data):
        self.id = data['id']
        self.problem = data['problem']
        self.description = data['description']
        self.urgency = data['urgency']
        self.screen_q = data['screen_q']
        self.expectations = data['expectations']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # a single instance that goes in to field 
        self.user = {} 

    @staticmethod
    def validate_create(data):
        is_valid = True

        if len(data["problem"]) < 5:
            flash("Problem must be 5 characters long!")
            is_valid = False
        
        if len(data["description"]) < 8:
            flash("Description must be 8 characters long!")
            is_valid = False
        
        if len(data["urgency"]) < 2:
            flash("Urgency must be 2 characters long!")
            is_valid = False
        
        if len(data["screen_q"]) < 5:
            flash("Explain how your screen looks in 5 characters.")
            is_valid = False
        
        if len(data["expectations"]) < 5:
            flash("Explain expectations in 5 characters!")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tickets LEFT JOIN users on tickets.user_id = users.id;"
        results = connectToMySQL("ticket_fullstack_py2").query_db(query)
        all_tickets = []
        for row in results:
            ticket = cls(row)
            user_data = {
                "id" : row['id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "email" : row['email'],
                "password" : row['password'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at'],
            }
            ticket.user = user.User(user_data)
            all_tickets.append(ticket)
        return all_tickets

    @classmethod
    def create_ticket(cls,data):
        query = "INSERT INTO tickets (problem, description, urgency, screen_q, expectations, user_id, created_at, updated_at) VALUES (%(problem)s, %(description)s, %(urgency)s, %(screen_q)s, %(expectations)s, %(user_id)s, NOW(), NOW());"
        new_ticket = connectToMySQL('ticket_fullstack_py2').query_db(query,data)
        return new_ticket

    @classmethod
    def show_ticket(cls,data):
        query = "SELECT * FROM tickets WHERE id= %(id)s"
        results = connectToMySQL("ticket_fullstack_py2").query_db(query,data)
        return cls(results[0])

    @classmethod
    def edit_ticket(cls,data):
        query = "UPDATE tickets SET problem = %(problem)s, description = %(description)s, urgency = %(urgency)s, screen_q = %(screen_q)s, expectations = %(expectations)s, user_id = %(user_id)s WHERE id= %(id)s;"
        results = connectToMySQL("ticket_fullstack_py2").query_db(query,data)
        return results
    
    @classmethod
    def one_ticket(cls,data):
        query = "SELECT * FROM tickets LEFT JOIN users on tickets.user_id = users.id WHERE tickets.id = %(id)s;"
        results = connectToMySQL("ticket_fullstack_py2").query_db(query,data)
        print(results)
        ticket = cls(results[0])
        user_data = {
            "id" : results[0]['id'], 
            "first_name" : results[0]['first_name'],
            "last_name" : results[0]['last_name'],
            "email" : results[0]['email'],
            "password" : results[0]['password'],
            "created_at" : results[0]['users.created_at'],
            "updated_at" : results[0]['users.updated_at']
        }
        ticket.user = user.User(user_data)
        return ticket
    
    @classmethod
    def delete_ticket(cls,data):
        query = "DELETE FROM tickets WHERE id= %(ticket_id)s;"
        return connectToMySQL("ticket_fullstack_py2").query_db(query,data)
