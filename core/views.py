from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from weasyprint import HTML
import os
from .forms import PersonalDomainForm, BusinessDomainForm
from .utils import generate_personal_letter, generate_business_letter





def create_pdf(letter):

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

            "font_path": f"file://{font_path}",  # WeasyPrint requires file:// URLs

        }

    )

    # Generate the PDF

    return HTML(string=html_string).write_pdf()



def home(request):

    personal_form = PersonalDomainForm()
    business_form = BusinessDomainForm()


    if request.method == "POST":


        # Personal form submission
        if "personal_submit" in request.POST:

            personal_form = PersonalDomainForm(request.POST)


            if personal_form.is_valid():

                data = personal_form.cleaned_data

                # Generate letter
                letter = generate_personal_letter(data)


                # Save data for PDF and email
                request.session["pdf_context"] = {

                    "letter": letter,

                    "name": data["full_name"],

                    "domain_name": data["domain_name"],

                    "email": data["email"],
                }


                return render(
                    request,
                    "home.html",
                    {
                        "letter": letter,
                        "personal_form": personal_form,
                        "business_form": business_form,
                        "selected_form": "personal",
                    }
                )



        # Business form submission
        elif "business_submit" in request.POST:


            business_form = BusinessDomainForm(request.POST)


            if business_form.is_valid():

                data = business_form.cleaned_data


                # Generate letter
                letter = generate_business_letter(data)


                # Save data for PDF and email
                request.session["pdf_context"] = {

                    "letter": letter,

                    "name": data["representative_name"],

                    "domain_name": data["domain_name"],

                    "email": data["representative_email"],
                }


                return render(
                    request,
                    "home.html",
                    {
                        "letter": letter,
                        "personal_form": personal_form,
                        "business_form": business_form,
                        "selected_form": "business",
                    }
                )


    return render(
        request,
        "home.html",
        {
            "personal_form": personal_form,
            "business_form": business_form,
        }
    )



def download_pdf(request):

    # Get generated letter
    pdf_context = request.session.get("pdf_context")


    if not pdf_context:

        return HttpResponse(
            "No generated letter found."
        )


    # Generate PDF
    pdf = create_pdf(
        pdf_context["letter"]
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