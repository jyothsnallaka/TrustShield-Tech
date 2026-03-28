from flask import Flask, request

app = Flask(__name__)

def detect_fake(review):
    review = review.lower()
    if "buy now" in review or "best product ever" in review:
        return "❌ Fake Review"
    elif len(review) < 20:
        return "⚠️ Suspicious Review"
    else:
        return "✅ Genuine Review"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    
    if request.method == 'POST':
        review = request.form['review']
        result = detect_fake(review)

    return f"""
    <html>
    <body style='text-align:center; font-family:Arial;'>
        <h1>TrustShield Tech</h1>
        <h3>Fake Review Detection</h3>

        <form method="POST">
            <textarea name="review" style="width:300px;height:100px;"></textarea><br><br>
            <button>Check</button>
        </form>

        <h2>{result}</h2>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)