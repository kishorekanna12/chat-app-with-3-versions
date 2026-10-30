from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
messages = ["Welcome to Chat App v3!"]

HTML_V3 = """
<!DOCTYPE html>
<html>
<head><title>Chat App - v3 (24MIS0381)</title></head>
<body style="font-family: Arial; margin: 40px;">
    <h2>Chat App - Version 3 (Send, View & Delete Messages)</h2>
    <p><b>Reg No:</b> 24MIS0381</p>
    <form method="POST" action="/send">
        <input type="text" name="message" placeholder="Type a message..." required>
        <button type="submit">Send</button>
    </form>
    <hr>
    <h3>Messages:</h3>
    <ul>
        {% for msg in messages %}
            <li style="margin-bottom: 8px;">
                {{ msg }}
                <form method="POST" action="/delete/{{ loop.index0 }}" style="display:inline; margin-left: 10px;">
                    <button type="submit" style="color: red;">Delete</button>
                </form>
            </li>
        {% else %}
            <li>No messages yet.</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_V3, messages=messages)

@app.route('/send', methods=['POST'])
def send():
    msg = request.form.get('message')
    if msg:
        messages.append(msg)
    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(messages):
        messages.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)