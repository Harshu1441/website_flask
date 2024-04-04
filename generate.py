import zipfile
from io import BytesIO
import os

def generate_files(navbar_title, list_items, navbar_bg_color, navbar_text_color, custom_css, custom_js, footer_color, slideshow_images, div_images, navbar_logo):
    # Initialize HTML content
    html_content = f'<!DOCTYPE html>\n'
    html_content += f'<html lang="en">\n'
    html_content += f'<head>\n'
    html_content += f'\t<meta charset="UTF-8">\n'
    html_content += f'\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    html_content += f'\t<title>Generated Website</title>\n'
    html_content += f'\t<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n'
    html_content += f'\t<link rel="stylesheet" href="style.css">\n'  # Include custom CSS file
    html_content += f'</head>\n'
    html_content += f'<body>\n'


    # Navbar section
    html_content += generate_navbar(navbar_title, list_items, navbar_bg_color, navbar_text_color, custom_css, navbar_logo)

    # Slideshow section
    html_content += generate_slideshow(slideshow_images)

    # Divs section
    html_content += generate_divs(div_images)

    # Contact form section
    html_content += generate_contact_form()

    # Footer section
    html_content += generate_footer(footer_color)

    # Add closing tags for body and html
    html_content += f'\t<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>\n'
    html_content += f'\t<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>\n'
    html_content += f'\t<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n'
    html_content += f'\t<script src="script.js"></script>\n'
    html_content += f'</body>\n'
    html_content += f'</html>\n'

    # Create CSS content
    css_content = generate_css(navbar_bg_color, navbar_text_color, custom_css)

    # Create an in-memory buffer to store the ZIP file
    zip_buffer = BytesIO()

    # Create a folder named 'src' in the ZIP file
    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zipf:
        zipf.writestr('src/', '')

        # Save navbar logo image to the 'src' folder
        filename = os.path.basename(navbar_logo.filename)
        zipf.writestr(f'src/{filename}', navbar_logo.read())

    # Write HTML and CSS content to the in-memory buffer
    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zipf:
        zipf.writestr('index.html', html_content)
        zipf.writestr('style.css', css_content)
        zipf.writestr('script.js', custom_js)
        
        # Save slideshow images to the 'src' folder
        for image_file in slideshow_images:
            filename = os.path.basename(image_file.filename)
            zipf.writestr(f'src/{filename}', image_file.read())
        
        # Save div images to the 'src' folder
        for image_file in div_images:
            filename = os.path.basename(image_file.filename)
            zipf.writestr(f'src/{filename}', image_file.read())

    # Seek to the beginning of the buffer
    zip_buffer.seek(0)

    return zip_buffer

# Remaining functions remain unchanged


def generate_navbar(navbar_title, list_items, navbar_bg_color, navbar_text_color, custom_css, navbar_logo):
    # Generate HTML content for navbar
    html_content = f'<nav class="navbar navbar-expand-lg navbar-light sticky-top" style="background-color: {navbar_bg_color};">\n'  # Added sticky-top class
    html_content += f'\t<img src="src/{navbar_logo.filename}" alt="Logo" width="50" height="50" class="mr-3">\n'
    html_content += f'\t<a class="navbar-brand" href="#" style="color: {navbar_text_color};">{navbar_title}</a>\n'
    html_content += f'\t<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\n'
    html_content += f'\t\t<span class="navbar-toggler-icon"></span>\n'
    html_content += f'\t</button>\n'
    html_content += f'\t<div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">\n'
    html_content += f'\t\t<ul class="navbar-nav">\n'
    for item in list_items.split(','):
        html_content += f'\t\t\t<li class="nav-item">\n'
        html_content += f'\t\t\t\t<a class="nav-link" href="#" style="color: {navbar_text_color};">{item.strip()}</a>\n'
        html_content += f'\t\t\t</li>\n'
    html_content += f'\t\t</ul>\n'
    html_content += f'\t</div>\n'
    html_content += f'</nav>\n'
    return html_content


# Remaining functions remain unchanged




def generate_slideshow(slideshow_images):
    # Generate HTML content for slideshow
    html_content = f'<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">\n'
    html_content += f'\t<div class="carousel-inner">\n'
    for i, image_file in enumerate(slideshow_images):
        if i == 0:
            html_content += f'\t\t<div class="carousel-item active">\n'
        else:
            html_content += f'\t\t<div class="carousel-item">\n'
        html_content += f'\t\t\t<img class="d-block w-100" src="src/{image_file.filename}" alt="Slide {i + 1}">\n'
        html_content += f'\t\t</div>\n'
    html_content += f'\t</div>\n'
    html_content += f'</div>\n'
    return html_content

def generate_divs(div_images):
    # Generate HTML content for divs
    html_content = f'<div class="container">\n'
    html_content += f'\t<div class="row">\n'
    for image_file in div_images:
        html_content += f'\t\t<div class="col-md-4">\n'
        html_content += f'\t\t\t<div class="card mb-4">\n'
        html_content += f'\t\t\t\t<img class="card-img-top" src="src/{image_file.filename}" alt="Card image cap">\n'
        html_content += f'\t\t\t\t<div class="card-body">\n'
        html_content += f'\t\t\t\t\t<h5 class="card-title">Card title</h5>\n'
        html_content += f'\t\t\t\t\t<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card\'s content.</p>\n'
        html_content += f'\t\t\t\t\t<a href="#" class="btn btn-primary">Go somewhere</a>\n'
        html_content += f'\t\t\t\t</div>\n'
        html_content += f'\t\t\t</div>\n'
        html_content += f'\t\t</div>\n'
    html_content += f'\t</div>\n'
    html_content += f'</div>\n'
    return html_content

def generate_contact_form():
    # Generate HTML content for contact form
    html_content = f'<div class="container">\n'
    html_content += f'\t<h2>Contact Us</h2>\n'
    html_content += f'\t<form>\n'
    html_content += f'\t\t<div class="form-group">\n'
    html_content += f'\t\t\t<label for="name">Name:</label>\n'
    html_content += f'\t\t\t<input type="text" class="form-control" id="name">\n'
    html_content += f'\t\t</div>\n'
    html_content += f'\t\t<div class="form-group">\n'
    html_content += f'\t\t\t<label for="email">Email:</label>\n'
    html_content += f'\t\t\t<input type="email" class="form-control" id="email">\n'
    html_content += f'\t\t</div>\n'
    html_content += f'\t\t<div class="form-group">\n'
    html_content += f'\t\t\t<label for="message">Message:</label>\n'
    html_content += f'\t\t\t<textarea class="form-control" id="message" rows="4"></textarea>\n'
    html_content += f'\t\t</div>\n'
    html_content += f'\t\t<button type="submit" class="btn btn-primary">Submit</button>\n'
    html_content += f'\t</form>\n'
    html_content += f'</div>\n'
    return html_content

def generate_footer(footer_color):
    # Generate HTML content for footer
    html_content = f'<footer class="footer" style="background-color: {footer_color};">\n'
    html_content += f'\t<div class="container">\n'
    html_content += f'\t\t<span class="text-muted">Place sticky footer content here.</span>\n'
    html_content += f'\t</div>\n'
    html_content += f'</footer>\n'
    return html_content

def generate_css(navbar_bg_color, navbar_text_color, custom_css):
    # Create CSS content
    css_content = f'''
    /* Custom CSS */
    /* You can add any additional custom CSS here */
    .navbar {{
        background-color: {navbar_bg_color} !important;
        color: {navbar_text_color} !important;
    }}
    {custom_css}
    '''
    return css_content
