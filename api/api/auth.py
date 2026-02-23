import json

def handler(request):
    body = json.loads(request.body)

    email = body.get("email")
    password = body.get("password")

    if email == "admin@hivestar.ai" and password == "123456":
        return {
            "statusCode": 200,
            "body": json.dumps({"token": "fake-jwt-token"})
        }

    return {
        "statusCode": 401,
        "body": json.dumps({"error": "Invalid credentials"})
    }
