from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return "FinSecure demo is running!"

# Simple echo endpoint to give ZAP something to crawl
@app.route("/echo")
def echo():
    q = request.args.get("q", "")
    # Render without escaping on purpose (for educational purposes: will likely be flagged)
    return render_template_string(f"<h1>Echo</h1><p>You said: {q}</p>")

@app.route("/headers")
def headers():
    # No security headers (ZAP will flag)
    resp = make_response("No extra security headers here.")
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)