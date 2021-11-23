# Techno-CRUD
In this Django CRUD web application I have used Bootstrap,jQuery and Django.
It gives the additional functionality as I have provided a Search Bar , Page selector which limits how much data you want to visit in a user list and also provided paginator for
viewing next page list with previous and next icons.
On searching the query It renders the related data to the query and also tells how much data matches from your query from the database.
It contains four buttons i.e.. GET,PUT,POST and DELETE on clicking on these buttons I have rendered bootstrap modal which asks for User's unique key i.e.. ID.
On clicking PUT button and after adding user you can view which user added currently as i have used Timestamp for that i.e. using(employee=Employee.objects.latest('created')).
User can updated the data,Get the data by providing key and can Delete his/her data and on clicking Delete button I have rendered a modal which ensures that the user really want 
to delete the data.
In this website code you can view back-end logics at view.py and can see front-end knowledgw in Templates.
