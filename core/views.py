from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from weasyprint import HTML
import os
from .forms import PersonalDomainForm, BusinessDomainForm
from .utils import generate_personal_letter, generate_business_letter, render_letter_to_jpeg
from django.shortcuts import render





def create_pdf(letter, is_business=False, company_name="", company_address=""):

    # Absolute path to the font file

    font_path = os.path.join(

        settings.BASE_DIR,

        "static",

        "fonts",

        "NotoSans-Regular.ttf"

    )

    # Render the HTML template with the font path

    html_string = render_to_string(

        "pdf/cover_letter.html",

        {

            "letter": letter,
            'is_business': is_business,
            'company_name': company_name,
            'company_address': company_address,

            "font_path": f"file://{font_path}",  # WeasyPrint requires file:// URLs

        }

    )

    # Generate the PDF

    return HTML(string=html_string).write_pdf()



def home(request):
    personal_form = PersonalDomainForm(prefix='personal')
    business_form = BusinessDomainForm(prefix='business')
    letter = None
    selected_tab = 'personal'

    if request.method == 'POST':
        if 'personal_submit' in request.POST:
            selected_tab = 'personal'
            personal_form = PersonalDomainForm(request.POST, prefix='personal')

            if personal_form.is_valid():
                data = personal_form.cleaned_data

                # Combine domain name and selected TLD
                data['domain_name'] = f"{data['domain_name']}{data['domain_tld']}"
                print(data["domain_name"])
                letter = generate_personal_letter(data)
                request.session["pdf_context"] = {

                "letter": letter,
                "is_business": False,
                "name": data["full_name"],

                "domain_name": data["domain_name"],

            }

        elif 'business_submit' in request.POST:
            selected_tab = 'business'
            business_form = BusinessDomainForm(
            request.POST,
            request.FILES,
            prefix='business'
        )

            if business_form.is_valid():
                data = business_form.cleaned_data

                # Combine domain name and selected TLD
                data['domain_name'] = f"{data['domain_name']}{data['domain_tld']}"

                letter = generate_business_letter(data)
                request.session["pdf_context"] = {

                "letter": letter,
                "is_business": True,
                "company_name": data["company_name"],
                "company_address": data["address"],
                "name": data["representative_name"],

                "domain_name": data["domain_name"],

            }

    return render(request, 'home.html', {
        'personal_form': personal_form,
        'business_form': business_form,
        'letter': letter,
        'selected_tab': selected_tab,
    })


def download_pdf(request):

    # Get generated letter
    pdf_context = request.session.get("pdf_context")

    if not pdf_context:

        return HttpResponse(
            "No generated letter found."
        )


    # Generate PDF
    pdf = create_pdf(
        letter=pdf_context["letter"],
        is_business=pdf_context.get("is_business", False),
        company_name=pdf_context.get("company_name", ""),
        company_address=pdf_context.get("company_address", ""),
    )


    response = HttpResponse(
        pdf,
        content_type="application/pdf"
    )


    response["Content-Disposition"] = (
        'attachment; filename="cover_letter.pdf"'
    )


    return response




def send_pdf_email(request):

    if request.method == "POST":


        pdf_context = request.session.get("pdf_context")


        if not pdf_context:

            messages.error(
                request,
                "Please generate a cover letter first."
            )

            return redirect("/")



        # Generate PDF
        pdf_file = create_pdf(
            pdf_context["letter"]
        )



        email = EmailMessage(

            subject="Your .np Domain Registration Cover Letter",

            body="""
Hello,

Your .np domain registration cover letter has been attached.

Please review the document, sign it, and submit it to Mercantile.

Thank you.
""",

            to=[
                pdf_context["email"]
            ]
        )



        # Attach PDF
        email.attach(

            "cover_letter.pdf",

            pdf_file,

            "application/pdf"

        )



        # Send email
        email.send()



        messages.success(

            request,

            "Cover letter has been sent successfully."

        )


    return redirect("/")

def download_jpeg(request):
    pdf_context = request.session.get("pdf_context")

    if not pdf_context:
        return HttpResponse(
            "No generated letter found.",
            status=400
        )

    jpeg_bytes = render_letter_to_jpeg(
        letter_html=pdf_context["letter"],
        is_business=pdf_context.get("is_business", False),
        company_name=pdf_context.get("company_name", ""),
        company_address=pdf_context.get("company_address", ""),
    )

    response = HttpResponse(
        jpeg_bytes,
        content_type="image/jpeg",
    )

    response["Content-Disposition"] = (
        'attachment; filename="cover_letter.jpg"'
    )

    return response