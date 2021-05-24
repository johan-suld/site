from flask import Flask, render_template, request
from functions import sql, sql_log
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def site():
    if request.method == 'POST':
        date_content = request.form['date']
        lines_list = sql("SELECT TOP 100 Title, Pageviews FROM WIKI WHERE DATE = '" + str(date_content) +
                         "' ORDER BY Pageviews DESC")
        if len(lines_list) == 0:
            no_hits = 'Ingen data för ' + date_content
            sql_log(datetime.now(tz=None).strftime("%Y-%m-%d %H:%M:%S"), date_content, 0)
            return render_template('index.html', error=no_hits)
        else:
            sql_log(datetime.now(tz=None).strftime("%Y-%m-%d %H:%M:%S"), date_content, 1)
            return render_template('index.html', lines=lines_list, date=date_content)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
