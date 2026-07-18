from io import BytesIO
from PIL import Image
from weasyprint import HTML
import numpy as np
from playwright.sync_api import sync_playwright
import base64
def generate_personal_letter(data):
    full_name = data["full_name"]
    address = data["address"]
    domain_name = data["domain_name"]
    email = data["email"]
    purpose = data["purpose"]
    ns1 = data["ns1"]
    ns2 = data["ns2"]
    phone = data["phone"]
    letter = f"""
<p>
    To,<br>
    Hostmaster<br>
    Mercantile Communications Pvt. Ltd.
</p>

<p>
    <strong>Subject: Request for .com.np Domain Registration</strong>
</p>

<p>
    Dear Sir/Madam,
</p>

<p>
    I am <strong>{full_name}</strong>, residing at {address}.
    I would like to request the registration of a domain under the .np ccTLD.
</p>

<div class="domain-box">
    <p><strong>Domain:</strong> {domain_name}</p>
    <p><strong>Primary Name Server (NS1):</strong> {ns1}</p>
    <p><strong>Secondary Name Server (NS2):</strong> {ns2}</p>
</div>

<p>
    <strong>Purpose of registering this domain:</strong><br>
    {purpose}
</p>

<p>
    My address is <strong>{address}</strong>.
</p>

<p>
    I have attached the required documents for your reference. I kindly request you to approve my domain registration request.
</p>

<p>
    Thank you.
</p>

<p>
    Sincerely,<br>
    <strong>{full_name}</strong>
    <br>
    Phone: {phone}
    <br>
    Email: {email}
</p>
"""

    return letter

def generate_business_letter(data):
    company_name = data["company_name"]
    representative_name = data["representative_name"]
    domain_name = data["domain_name"]
    business_description = data["business_description"]
    address = data["address"]
    business_stamp = data.get("business_stamp")
    ns1 = data["ns1"]
    ns2 = data["ns2"]
    representative_email = data["representative_email"]
    representative_phone = data["representative_phone"]
    stamp_html = ""

    if business_stamp:
        encoded = base64.b64encode(
            business_stamp.read()
        ).decode()

        stamp_html = f"""
        <div class="stamp">
            <img src="data:image/png;base64,{encoded}" width="120">
        </div>
        """
    
    letter = f"""
    
<p>
    To,<br>
    Hostmaster<br>
    Mercantile Communications Pvt. Ltd.
</p>

<p>
    <strong>Subject: Request for Domain Registration of {company_name}</strong>
</p>

<p>
    Dear Sir/Madam,
</p>

<p>
    We, <strong>{company_name}</strong>, would like to request the
    registration of a domain under the .np ccTLD for our organization.
</p>

<div class="domain-box">
    <p><strong>Domain:</strong> {domain_name}</p>
    <p><strong>Primary Name Server (NS1):</strong> {ns1}</p>
    <p><strong>Secondary Name Server (NS2):</strong> {ns2}</p>
</div>

<p>
    <strong>Organization Details:</strong><br>
    Company Name: {company_name}<br>
    Company Address: {address}
</p>

<p>
    <strong>Business Description:</strong><br>
    {business_description}
</p>

<p>
    The authorized representative for this domain registration request is
    <strong>{representative_name}</strong>.
</p>

<p>
   We have attached the required documents for your reference. We kindly request you to approve our domain registration request.
</p>

<p>
    Thank you.
</p>

<p>
    Sincerely,<br><br>
    <strong>{representative_name}</strong><br>
    {company_name}
    <br>
    Email: {representative_email}<br>
    Phone: {representative_phone}
</p>
{stamp_html}
"""

    return letter

def _autocrop_bottom_whitespace(img, threshold=250, padding=40):
    arr = np.array(img.convert('L'))
    rows_with_content = np.where(arr.min(axis=1) < threshold)[0]
    if len(rows_with_content) == 0:
        return img
    last_content_row = rows_with_content[-1]
    crop_height = min(last_content_row + padding, img.height)
    return img.crop((0, 0, img.width, crop_height))


def render_letter_to_jpeg(letter_html, is_business=False, company_name="", company_address="", width_px=1240, quality=90):

    # Wrap the letter inside a complete HTML page
    letterhead = ''
    if is_business:
        letterhead = f"""

        <div class="letterhead">

            <h1>{company_name}</h1>
            <h3>{company_address}</h3>

        </div>

        """

    full_html = f"""

    <html>

        <head>

            <style>

 body {{

                    font-family: 'Arial', serif;

                    font-size: 22px;

                    line-height: 1.6;

                    color: #000;

                    padding: 60px 70px;

                    width: {width_px}px;

                }}

                .letterhead {{

                    text-align: center;

                    border-bottom: 2px solid #ddd;

                    padding-bottom: 20px;

                    margin-bottom: 35px;

                }}

                .letterhead h1 {{

                    margin: 0;

                    font-size: 42px;

                    font-weight: bold;

                }}

                .domain-box {{

                    border: 1px solid #ccc;

                    padding: 16px 20px;

                    margin: 20px 0;

                }}

            </style>

        </head>
        

        <body>
        {letterhead}
        {letter_html}
        </body>

    </html>

    """

    with sync_playwright() as p:

        # Launch headless chromium browser

        browser = p.chromium.launch()

        page = browser.new_page(

            viewport={"width": width_px, "height": 2000}

        )

        # Load HTML content

        page.set_content(full_html)

        # Take screenshot of the letter

        png_bytes = page.screenshot(full_page=True)

        browser.close()

    # Convert PNG screenshot to JPEG

    img = Image.open(BytesIO(png_bytes)).convert("RGB")

    img = _autocrop_bottom_whitespace(img)

    buffer = BytesIO()

    img.save(buffer, format="JPEG", quality=quality)

    return buffer.getvalue()