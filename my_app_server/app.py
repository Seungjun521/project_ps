from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "안녕하세요, 주인님! 🔥"

if __name__ == '__main__':
    app.run(debug=True)
