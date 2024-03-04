# simpleatom_form

Quick Start (I will describe it later)

Endpoints:
^url/forms/form_data/

METHODS:

1. POST: ^url/forms/form_data/
Takes various fields and makes a new entry in the database
For example
- {"email": "email"}
- {"email": "email", "first_question": "first_answer"}
- {"email": "email", "first_question": "first_answer", "second_question": "second_answer"}
return object with "id": id

2. PUT: ^url/forms/form_data/id/
update the object. 
If the updated json contains existing fields, and the fields have different data, the data is updated in the object. 
If the updated json contains new fields, these fields with data in them are added to the object
return updated object with id

3. GET ^url/forms/form_data/ - sends list with all objects from database
4. GET ^url/forms/form_data/id/ - sends one objects from database by id
5. GET ^url/forms/form_data?email=ttt@gmail.com - sends one objects from database by parameter



