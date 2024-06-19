from flask import Flask, request, send_from_directory
import sqlite3

app = Flask(__name__, static_url_path='', static_folder='')


def init_db():
       conn = sqlite3.connect('contacts.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Contact (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               telephone TEXT NOT NULL,
               data DATETIME NOT NULL,
               yslyga TEXT NOT NULL
           )
       ''')
       conn.commit()
       conn.close()


@app.route('/')
def home():
       return send_from_directory('', 'html.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
       name = request.form['name']
       telephone = request.form['telephon']
       data = request.form['data']
       yslyga = request.form['yslyga']
       conn = sqlite3.connect('contacts.db')
       cursor = conn.cursor()
       cursor.execute('''
           INSERT INTO Contact (name, telephone, data, yslyga)
           VALUES (?, ?, ?, ?)
       ''', (name, telephone, data, yslyga))
       conn.commit()
       conn.close()
       
       return 'Форма успешно отправлена!'


@app.route('/submit_form-comment', methods=['POST'])
def submit_form_comment():
       name = request.form['name']
       content = request.form['content']
       conn = sqlite3.connect('contacts.db')
       cursor = conn.cursor()
       cursor.execute('''
           INSERT INTO Comment (name, content)
           VALUES (?, ?)''', (name, content))
       conn.commit()
       conn.close()

       return 'Форма успешно отправлена!'


if __name__ == '__main__':

       init_db()
       app.run(host='0.0.0.0', port=5000)