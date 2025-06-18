from flask import Flask, jsonify, send_file
import datetime
import pytz
from PIL import Image, ImageDraw

app = Flask(__name__)

@app.route("/timezone/Europe/Copenhagen", methods=["GET"])
def get_copenhagen_time():
    tz = pytz.timezone("Europe/Copenhagen")
    now = datetime.datetime.now(tz)
    return jsonify({
        "datetime": now.isoformat(),
        "timezone": "Europe/Copenhagen",
        "unixtime": int(now.timestamp()),
        "utc_offset": now.strftime('%z')
    })

@app.route("/logo.png")
def logo():
    img = Image.new('RGB', (256, 256), color=(30, 30, 60))
    draw = ImageDraw.Draw(img)
    draw.ellipse((64, 64, 192, 192), fill=(255, 255, 255))
    draw.line((128, 128, 128, 80), fill=(0, 0, 0), width=6)
    draw.line((128, 128, 170, 140), fill=(0, 0, 0), width=6)
    path = "/tmp/realtime_clock_logo.png"
    img.save(path)
    return send_file(path, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
