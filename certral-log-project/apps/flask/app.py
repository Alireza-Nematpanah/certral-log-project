
from flask import Flask
import logging
import os

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [flask-service] %(message)s"
)

logger = logging.getLogger("flask-service")


@app.route("/")
def home():
    logger.info("Home page requested")
    return "Flask service is running!"


@app.route("/health")
def health():
    logger.info("Health check requested")
    return {"status": "healthy", "service": "flask"}


@app.route("/error")
def error():
    logger.error("CENTRAL_LOG_TEST Flask test error")
    return {"error": "Test error logged", "service": "flask"}, 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
