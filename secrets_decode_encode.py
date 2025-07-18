import base64
import json

def encode_dockerconfigjson(username, password, email):
    auth_str = f"{username}:{password}"
    auth_b64 = base64.b64encode(auth_str.encode()).decode()

    docker_config = {
        "auths": {
            "https://index.docker.io/v1/": {
                "username": username,
                "password": password,
                "email": email,
                "auth": auth_b64
            }
        }
    }

    docker_config_json = json.dumps(docker_config)
    encoded = base64.b64encode(docker_config_json.encode()).decode()
    return encoded

def decode_dockerconfigjson(encoded):
    decoded_json = base64.b64decode(encoded).decode()
    parsed = json.loads(decoded_json)
    return parsed

# ----------------------------
# Example usage
# ----------------------------

# Encode
username = "gurpreetgandhi"
password = "Nokia@2690"
email = "gurpreetgandhi3@gmail.com"

encoded_secret = encode_dockerconfigjson(username, password, email)
print("Encoded .dockerconfigjson:")
print(encoded_secret)

js = 'eyJhdXRocyI6eyJodHRwczovL2luZGV4LmRvY2tlci5pby92MS8iOnsidXNlcm5hbWUiOiJuaWtoaWx2MjE1IiwicGFzc3dvcmQiOiJOaWtoaWxAMjE1IiwiZW1haWwiOiJuaWtoaWwudkBnYWlhbnNvbHV0aW9ucy5jb20iLCJhdXRoIjoiYm1scmFHbHNkakl4TlRwT2FXdG9hV3hBTWpFMSJ9fX0='
# Decode
decoded_secret = decode_dockerconfigjson(js)
print("\nDecoded .dockerconfigjson:")
print(json.dumps(decoded_secret, indent=2))
