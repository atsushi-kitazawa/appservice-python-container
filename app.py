import os
from flask import Flask, render_template
import psycopg2
import psycopg2.extras

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/users', methods=['GET'])
def users():
    host = os.environ['TEST_HOST']
    port = os.environ['TEST_PORT']
    database = os.environ['TEST_DATABASE']
    user = os.environ['TEST_USER']
    password = os.environ['TEST_PASSWORD']

    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password,
    )

    # Create cursor and fetch and close.
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('select * from user1')
    ds = cur.fetchall()
    cur.close()

    # Close connection.
    conn.close()
    return render_template('users.html', title='Flask pgsql', users=ds)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
