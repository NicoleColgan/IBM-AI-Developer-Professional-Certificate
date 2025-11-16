# Import the Flask class from the flask module
from flask import Flask, make_response, request

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"    # string automatically returns 200


#################################################################################################################
# returning a status code
#################################################################################################################
@app.route("/no_content")
def no_content():
    return {"Message": "no content found"}, 204 # # return 204 when an operation is successful but nothing needs to be returned eg after deleting a resource (nothing is returned even if you return a message)

#################################################################################################################
# sending a custom http code back with make_response()
#################################################################################################################
@app.route("/exp")
def index_explicit():
    res = make_response({"message": "hello world"})
    res.status_code = 200
    return res

#################################################################################################################
# process input arugments
#################################################################################################################

@app.route("/data")
def get_data():
    '''
    Method to return data
    '''
    try:
        if data and len(data) > 0:  # check if data exists
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data missing"}, 500 # server error
    except NameError:   # 'data' not found
        return {"message": "'data' not found"}, 404 # 404 not found

@app.route("/name_search")
def name_search():
    '''
    Method to return person by name
    usage: `curl -X GET -i localhost:5000/name_search?q=Tanya`
    '''
    first_name = request.args.get("q", "").strip()  # default ""

    if first_name and not first_name.isdigit():  # first name is valid
        for person in data:
            if person.get("first_name") == first_name:  # first name in data
                return person
            else:
                return {"message": "person not found in 'data'"}, 404 #curl -X GET -i localhost:5000/name_search?q=not-in-data
    return {"message": "invalid request"}, 400    # invalid request - curl -X GET -i localhost:5000/name_search?

#################################################################################################################
# Add dynamic urls
# eg `GET http://localhost/person/unique_identifier`
# eg `DELETE http://localhost/person/unique_identifier``
#################################################################################################################

@app.route("/count")
def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500

# curl -X GET -i localhost:5000/person/0dd63e57-0b5f-44bc-94ae-5c1b4947cb49
@app.route("/person/<string:id>")
def find_by_uuid(id):
    for person in data:
        if person.get("id") == id:
            return person   # Return the matching person as a JSON response with a 200 OK status code
    return {"message": "person not found"}, 404

# curl -X DELETE -i localhost:5000/person/0dd63e57-0b5f-44bc-94ae-5c1b4947cb49
@app.route("/person/<string:id>", methods=["DELETE"])
def delete_by_uuid(id):
    for person in data:
        if person.get("id") == id:
            data.remove(person)
            return {"message": f"person with id {id} deleted"}
    return {"message": "no person found"}


#################################################################################################################
# Parse JSON from Request body
#################################################################################################################

# curl -X POST -i -w '\n'   --url http://localhost:5000/person   
#       --header 'Content-Type: application/json'   
#       --data '{
#         "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
#         "first_name": "John",
#         "last_name": "Horne",
#         "graduation_year": 2001,
#         "address": "1 hill drive",
#         "city": "Atlanta",
#         "zip": "30339",
#         "country": "United States",
#         "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
# }'
@app.route("/person", methods=["POST"])
def add_by_id():    # post request doesnt take in params
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input params"}, 422
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message": f"{new_person['id']}"}, 200


#################################################################################################################
# Add error handlers:
#  Flask makes it easy to handle global error handlers using the errorhandler() decorator.
# Instead of returning 404 html you want to return a JSON response for all invalid requests.
#################################################################################################################

# curl -X GET -i localhost:5000/invalid
@app.errorhandler(404)  # handle 404 errors
def api_not_found(error):
    '''
    This is a custom error handler for 404 errors
    Its triggered whenever a 404 occurs in a flask app
    '''
    return {"message": "API not found"}, 404


@app.errorhandler(Exception)
def handle_exception(e):
    '''
    global error handler
    '''
    return {"message": str(e)}, 500

@app.route("/test500")
def test500():
    raise Exception("Forced exception for testing")