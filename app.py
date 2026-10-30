from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
messages = ["Welcome to Chat App v2!"]

HTML_V2 = """
<!DOCTYPE html>
<html>
<head><title>Chat App - v2 (24MIS0381)</title></head>
<body style="font-family: Arial; margin: 40px;">
    <h2>Chat App - Version 2 (Send & View Messages)</h2>
    <p><b>Reg No:</b> 24MIS0381</p>
    <form method="POST" action="/send">
        <input type="text" name="message" placeholder="Type a message..." required>
        <button type="submit">Send</button>
    </form>
    <hr>
    <h3>Messages:</h3>
    <ul>
        {% for msg in messages %}
            <li>{{ msg }}</li>
        {% else %}
            <li>No messages yet.</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_V2, messages=messages)

@app.route('/send', methods=['POST'])
def send():
    msg = request.form.get('message')
    if msg:
        messages.append(msg)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)