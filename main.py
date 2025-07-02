from flask import Flask, request, jsonify

app = Flask(__name__)

# قاعدة بيانات الـ Access Keys (ممكن تزود فيها بعدين)
valid_keys = {
    "123456": {
        "email": "example@gmail.com",
        "password": "password123",
        "money": "999999999",
        "rank": "MAX",
    }
}

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    access_key = data.get("access_key")

    if access_key not in valid_keys:
        return jsonify({
            "status": "error",
            "message": "Invalid access key. Contact @SYCHO_DEV_BOT to get one."
        }), 401

    user_data = valid_keys[access_key]
    return jsonify({
        "status": "success",
        "money": user_data["money"],
        "rank": user_data["rank"],
        "message": "Account updated successfully."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
