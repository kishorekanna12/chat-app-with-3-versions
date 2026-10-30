from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
messages = []

HTML_V1 = """
<!DOCTYPE html>
<html>
<head><title>Chat App - v1 (24MIS0381)</title></head>
<body style="font-family: Arial; margin: 40px;">
    <h2>Chat App - Version 1 (Send Message)</h2>
    <p><b>Reg No:</b> 24MIS0381</p>
    <form method="POST" action="/send">
        <input type="text" name="message" placeholder="Type a message..." required>
        <button type="submit">Send</button>
    </form>
    {% if status %}
        <p style="color: green;">{{ status }} (Total stored: {{ count }})</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    status = request.args.get('status')
    return render_template_string(HTML_V1, status=status, count=len(messages))

@app.route('/send', methods=['POST'])
def send():
    msg = request.form.get('message')
    if msg:
        messages.append(msg)
    return redirect('/?status=Message+Added+Successfully!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)