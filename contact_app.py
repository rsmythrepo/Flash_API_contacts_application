from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Welcome to My Flask App</title>
<style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                text-align: center;
                background-color: #fff;
                padding: 40px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 10px;
                color: #3498db;
            }
            p {
                font-size: 1.2em;
                margin-bottom: 20px;
            }
            a {
                display: inline-block;
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            a:hover {
                background-color: #2980b9;
            }
</style>
</head>
<body>
<div class="container">
<h1>Welcome to My Contact App</h1>
<p>This is a simple Flask web application with beautiful HTML content!</p>
</div>
</body>
</html>
    '''

contacts = {
    "Alice" : 93981273,
    "Rachel": 98398713,
    "Joe" : 987236971
}

@app.route("/phone/<string:name>/", methods=['GET']) # notice the id is captured from the URI
def get_phone_number(name):
    if name in contacts.keys():
        return {"phone number": contacts[name]}
    else:
        return {"error":"User not found."}

@app.route("/contacts/", methods=['GET'])
def get_contacts():
    return contacts

# add a new record
@app.route("/new_contact/<string:name>/<int:phone>/", methods=['POST'])
def new_contact(name, phone):
    if name in contacts:
        return {"error": "That name already exists. Please use a different one."}
    else:
        contacts[name] = phone
        return {
            "added_contact_report": {
                "Name": name,
                "Phone": phone
            }
        }

# delete an existing record
@app.route("/delete_contact/<string:name>/", methods=['DELETE'])
def delete_contact(name):
    if name in contacts:
        deleted_contact = contacts[name]
        del contacts[name]
        return {
            "delete_contact_report": {
                "Name": name,
                "Phone": deleted_contact
            }
        }
    else:
        return {"error": "Cannot delete: user not found."}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
