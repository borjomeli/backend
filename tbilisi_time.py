from flask import Flask, render_template_string
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def show_tbilisi_time():
    # Get Tbilisi timezone
    tbilisi_tz = pytz.timezone('Asia/Tbilisi')
    
    # Get current time in Tbilisi
    tbilisi_time = datetime.now(tbilisi_tz)
    
    # Format the time
    formatted_time = tbilisi_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Simple HTML template
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tbilisi Time</title>
        <meta http-equiv="refresh" content="1">
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background-color: #f0f0f0;
            }
            .time-container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }
            .time {
                font-size: 2em;
                color: #333;
                margin-bottom: 10px;
            }
            .location {
                font-size: 1.2em;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="time-container">
            <h1>🕐 Current Time</h1>
            <div class="time">{{ time }}</div>
            <div class="location">Tbilisi, Georgia</div>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template, time=formatted_time)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
