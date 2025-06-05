from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@db/recommendation_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Recommendation(db.Model):
    __tablename__ = 'recommendations'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100))
    reason = db.Column(db.String(255))

@app.route("/")
def index():
    return generate_html(Recommendation.query.order_by(Recommendation.id.desc()).all())

@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = Recommendation.query.filter(
        Recommendation.product.ilike(f"%{query}%")
    ).order_by(Recommendation.id.desc()).all()
    return generate_html(results)

def generate_html(recommendations):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Рекомендательная система</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"  rel="stylesheet">
        <style>
            body { background: #f8f9fa; padding: 30px; }
            .card { margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1 class="mb-4">Рекомендательная система</h1>
        <form class="mb-4" action="/search">
            <input type="text" name="q" class="form-control" placeholder="Поиск по продуктам...">
        </form>
        <div class="row">
    """

    for rec in recommendations:
        html += f"""
            <div class="col-md-6 col-lg-4 mb-3">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">{rec.product}</h5>
                        <p class="card-text">{rec.reason}</p>
                    </div>
                </div>
            </div>
        """

    html += """
        </div>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
