from flask import Flask, jsonify, request

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
    body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; }
    .container { text-align: center; background-color: #fff; padding: 40px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); border-radius: 8px; }
    h1 { font-size: 3em; margin-bottom: 10px; color: #3498db; }
    p { font-size: 1.2em; margin-bottom: 20px; }
    a, button { padding: 10px 20px; background-color: #3498db; color: white; text-decoration: none; border-radius: 5px; transition: background-color 0.3s ease; border: none; cursor: pointer; margin: 5px; }
    a:hover, button:hover { background-color: #2980b9; }
</style>
</head>
<body>
<div class="container">
    <h1>Welcome to My Contact App</h1>
    <p>This is a simple Flask web application with multiple endpoints.</p>

    <!-- Link to view all contacts -->
    <a href="/contacts/" target="_blank">View All Contacts</a>

    <!-- Form to get a contact by name -->
    <h3>Find Contact</h3>
    <form action="/phone/" method="get" onsubmit="event.preventDefault(); getContact();">
        <input type="text" id="contactName" placeholder="Enter name" required>
        <button type="submit">Get Contact</button>
    </form>
    <p id="contactResult"></p>

    <!-- Form to add a new contact -->
    <h3>Add Contact</h3>
    <form action="/new_contact/" method="post" onsubmit="event.preventDefault(); addContact();">
        <input type="text" id="newName" placeholder="Name" required>
        <input type="number" id="newPhone" placeholder="Phone" required>
        <button type="submit">Add Contact</button>
    </form>
    <p id="addResult"></p>

    <!-- Form to delete a contact -->
    <h3>Delete Contact</h3>
    <form action="/delete_contact/" method="post" onsubmit="event.preventDefault(); deleteContact();">
        <input type="text" id="deleteName" placeholder="Enter name" required>
        <button type="submit">Delete Contact</button>
    </form>
    <p id="deleteResult"></p>
</div>

<script>
    async function getContact() {
        const name = document.getElementById("contactName").value;
        const response = await fetch(`/phone/${name}/`);
        const data = await response.json();
        document.getElementById("contactResult").textContent = JSON.stringify(data);
    }

    async function addContact() {
        const name = document.getElementById("newName").value;
        const phone = document.getElementById("newPhone").value;
        const response = await fetch(`/new_contact/${name}/${phone}/`, { method: "POST" });
        const data = await response.json();
        document.getElementById("addResult").textContent = JSON.stringify(data);
    }

    async function deleteContact() {
        const name = document.getElementById("deleteName").value;
        const response = await fetch(`/delete_contact/${name}/`, { method: "DELETE" });
        const data = await response.json();
        document.getElementById("deleteResult").textContent = JSON.stringify(data);
    }
</script>

</body>
</html>
    '''


contacts = {
    "Alice": 93981273,
    "Rachel": 98398713,
    "Joe": 987236971
}


@app.route("/phone/<string:name>/", methods=['GET'])
def get_phone_number(name):
    if name in contacts:
        return jsonify({"phone number": contacts[name]})
    else:
        return jsonify({"error": "User not found."})


@app.route("/contacts/", methods=['GET'])
def get_contacts():
    return jsonify(contacts)


@app.route("/new_contact/<string:name>/<int:phone>/", methods=['POST'])
def new_contact(name, phone):
    if name in contacts:
        return jsonify({"error": "That name already exists. Please use a different one."})
    else:
        contacts[name] = phone
        return jsonify({"added_contact_report": {"Name": name, "Phone": phone}})


@app.route("/delete_contact/<string:name>/", methods=['DELETE'])
def delete_contact(name):
    if name in contacts:
        deleted_contact = contacts.pop(name)
        return jsonify({"delete_contact_report": {"Name": name, "Phone": deleted_contact}})
    else:
        return jsonify({"error": "Cannot delete: user not found."})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
