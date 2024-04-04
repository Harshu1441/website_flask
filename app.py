from flask import Flask, render_template, request, send_file
from generate import generate_files

app = Flask(__name__)

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
