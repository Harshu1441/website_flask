from flask import Flask, render_template, request, send_file, redirect, url_for
from generate import generate_files
import pyodbc


app = Flask(__name__)

# Database connection string
conn_str = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:database-79.database.windows.net,1433;Database=db01;Uid=database-79;Pwd=Harshu007*#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

# Function to establish database connection
def connect_to_database():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print("Database connection error:", e)
        return None, None

# Function to close database connection
def close_connection(conn, cursor):
    try:
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error closing connection:", e)


# Route for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn, cursor = connect_to_database()
        if conn and cursor:
            try:
                cursor.execute("INSERT INTO user01 (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                close_connection(conn, cursor)
                return redirect(url_for('login'))
            except pyodbc.IntegrityError as e:
                print("Error registering user:", e)
                close_connection(conn, cursor)
                return render_template('register.html', error="Username already exists.")
            except Exception as e:
                print("Error registering user:", e)
                close_connection(conn, cursor)
                return render_template('register.html', error="Error registering user.")
    return render_template('register.html')




# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn, cursor = connect_to_database()
        if conn and cursor:
            cursor.execute("SELECT * FROM user01 WHERE username=? AND password=?", (username, password))
            user = cursor.fetchone()
            close_connection(conn, cursor)
            if user:
                return render_template('index.html')
            else:
                return render_template('login.html', error="Invalid username or password.")
    return render_template('login.html')



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/generate', methods=['POST'])
def generate_website():
    navbar_title = request.form['navbar_title']
    list_items = request.form['list_items']
    navbar_bg_color = request.form['navbar_bg_color']
    navbar_text_color = request.form['navbar_text_color']
    custom_css = request.form['custom_css']
    custom_js = request.form['custom_js']
    footer_color = request.form['footer_color']

    # Handle navbar logo image
    navbar_logo = request.files['navbar_logo']

    slideshow_images = request.files.getlist('slideshow_images')
    div_images = request.files.getlist('div_images')

    zip_buffer = generate_files(navbar_title, list_items, navbar_bg_color, navbar_text_color, custom_css, custom_js, footer_color, slideshow_images, div_images, navbar_logo)

    return send_file(zip_buffer, as_attachment=True, download_name='output.zip')

if __name__ == "__main__":
    app.run(debug=True)
