# Ticketing System (Python/SQL/Flask)

# Tools used to build this app
- Python 
- SQL 
- Flask
- Bootstrap

# Instructions to access app 
You gain access to the app by copying and pasting http://127.0.0.1:5000/ to you browser and then writing the command server.py on your terminal.  

#  Register / Log in 

In this page users will be able to register and then successfully log in with the write credentials.  

Validations will show if user did not register or if an incorrect email or password is written during log in attempt.  

![Screen Shot 2022-09-07 at 11 26 14 AM](https://user-images.githubusercontent.com/66094112/188917528-8254a6e5-c5aa-408b-8bba-ce99976c383a.png)
![Screen Shot 2022-09-07 at 11 28 47 AM](https://user-images.githubusercontent.com/66094112/188918092-82bec057-cb15-45ef-8661-d13299a8bd0c.png)

# Ticket Dashboard

After successfully logging in, a dashboard with tickets from other users will show. From this page you will have access to create a ticket, logout, edit, or delete ticket. 

![Screen Shot 2022-09-07 at 11 30 39 AM](https://user-images.githubusercontent.com/66094112/188918496-a6efb413-f40b-4cb2-81dc-5c74c937ad8c.png)

# Create Ticket 
The user will be able to submit a ticket on this page and answer questions that are necessary to trouble shooting problem. Clicking on submit once all areas are filled redirects user to the dashboard with new ticket displayed at the bottom.   

![Screen Shot 2022-09-07 at 11 36 28 AM](https://user-images.githubusercontent.com/66094112/188919942-e8a25883-5368-4631-a061-5f1f3ef99552.png)

![Screen Shot 2022-09-07 at 11 40 38 AM](https://user-images.githubusercontent.com/66094112/188920679-a6e4abd5-7f76-43b0-964b-4bc359dc75d7.png)

![Screen Shot 2022-09-07 at 11 42 46 AM](https://user-images.githubusercontent.com/66094112/188921159-1ea727c5-fba4-47aa-829c-25465754896d.png)

# Ticket Details

Viewing ticket details will show user the answers that they filled out in detail.  This gives admin a good understanding as to what challenges the user is facing and makes the process more efficient for the support engineer to troubleshoot. Clicking "Request Complete" deleted the task from the list.  

![Screen Shot 2022-09-07 at 11 43 52 AM](https://user-images.githubusercontent.com/66094112/188921369-383809fa-c029-4b9f-bf84-d8019d1ea99b.png)


# Edit Ticket 
Clicking edit from the dashboard will lead to a page that has the values already filled.  The user will be able to edit the ticket accordingly and then resubmit. After clicking update, the user will be redirected back to dashboard.

![Screen Shot 2022-09-07 at 11 50 00 AM](https://user-images.githubusercontent.com/66094112/188922770-e7b2ca4b-8e2a-4fe1-b0ce-2cb9e5df9bb2.png)

![Screen Shot 2022-09-07 at 11 50 55 AM](https://user-images.githubusercontent.com/66094112/188922988-87e30c01-976f-4307-b2c5-6d9eebfcf1dd.png)

# DELETE
By clicking the "Ticket Resolved" button on the dashboard, the user will be able to delete a "pending ticket" from the list once it is successfully resolved.  

![Screen Shot 2022-09-07 at 11 52 33 AM (2)](https://user-images.githubusercontent.com/66094112/188923387-16ad948d-7569-46b8-8c75-3403efcd89c2.png)
![Screen Shot 2022-09-07 at 11 53 21 AM](https://user-images.githubusercontent.com/66094112/188923574-d1e2629a-6d5a-480f-9abe-bd2ffbea486e.png)

# Bugs that need to be fixed 
- parsing error: users should only have the ability of editing their own ticket, not the ticket of other users.  
- if there is a validation error on edit page, after clicking submit redirect edit page back to edit page and display validations.  
