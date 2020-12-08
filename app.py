from myproject import app
from flask import render_template,redirect,request,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField, IntegerField
import smtplib

app.config["SECRET_KEY"] = "mysecretkey"

TEMPLATES_AUTO_RELOAD=True

class ContactForm(FlaskForm):
    email = StringField("Email")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    zip = IntegerField("Zip Code")
    phone = IntegerField("Phone Number")
    submit = SubmitField("Submit")
    private_dinner = BooleanField("Private Dinner")
    private_consult = BooleanField("Private Client Consultation")
    business_consult = BooleanField("Business to Business Consultation")
    in_person_somm = BooleanField("Sommelier Led Wine Tastings In-person")
    online_somm = BooleanField("Sommelier Led Wine Tasting Online")
    comments = TextAreaField()

class HireSommForm(FlaskForm):
    email = StringField("Email")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    zip = IntegerField("Zip Code")
    phone = IntegerField("Phone Number")
    submit = SubmitField("Submit")
    private_dinner = BooleanField("Private Dinner")
    in_person_somm = BooleanField("Sommelier Led Wine Tastings In-person")
    online_somm = BooleanField("Sommelier Led Wine Tasting Online")
    comments = TextAreaField()

class WineConsultForm(FlaskForm):
    email = StringField("Email")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    zip = IntegerField("Zip Code")
    phone = IntegerField("Phone Number")
    submit = SubmitField("Submit")
    comments = TextAreaField()
    cellar_mgmt = BooleanField("Cellar Management")
    rare_and_vintage = BooleanField("Rare and Vintage Search")
    curate_case = BooleanField("Curated Cases")

class BusinessConsultForm(FlaskForm):
    email = StringField("Email")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    zip = IntegerField("Zip Code")
    phone = IntegerField("Phone Number")
    submit = SubmitField("Submit")
    comments = TextAreaField()
    retail = BooleanField("Retail Consultation")
    hotel_rest = BooleanField("Restuarant/Hotel Consultation")



@app.route('/', methods=["GET","POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        email_address = "wwcwebsite1@gmail.com"
        email_password = "awpjpzzgtoskbwhj"
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email_address, email_password)

            requested_services = []

            if form.private_dinner.data == True:
                requested_services.append("Private Dinner")
            if form.private_consult.data == True:
                requested_services.append("Private Consult")
            if form.business_consult.data == True:
                requested_services.append("Business Consult")
            if form.in_person_somm.data == True:
                requested_services.append("In Person Somm")
            if form.online_somm.data == True:
                requested_services.append("Online Somm")



            subject = "General Contact"
            body = "Name: " + form.first_name.data + " " + form.last_name.data + "\n" + "Email: " + form.email.data + "\n" + "Zip: " + str(form.zip.data) + "\n" + "Phone: " + str(form.phone.data) + "\n" + "Services: " + str(requested_services) + "\n" + "Comments: " + form.comments.data
            msg = f'subject: {subject}\n\n{body}'
            smtp.sendmail(email_address, "wellingtonwineconsulting@gmail.com", msg)

            first_name = form.first_name.data
            last_name = form.last_name.data

            # return redirect(url_for("thank_you", first_name=first_name, last_name=last_name))
            return render_template("thank_you.html", first_name=first_name, last_name=last_name)

    return render_template("home.html", form=form)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services', methods=["GET","POST"])
def services():


####### NEW WAY #######
    hiresommform = HireSommForm()
    wineconsultform = WineConsultForm()
    businessconsultform = BusinessConsultForm()
    if hiresommform.validate_on_submit() or wineconsultform.validate_on_submit() or businessconsultform.validate_on_submit():
        email_address = "wwcwebsite1@gmail.com"
        email_password = "awpjpzzgtoskbwhj"
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email_address, email_password)

            requested_services = []

            if hiresommform.private_dinner.data == True:
                requested_services.append("Private Dinner")
            if hiresommform.in_person_somm.data == True:
                requested_services.append("In Person Somm")
            if hiresommform.online_somm.data == True:
                requested_services.append("Online Somm")
            if wineconsultform.cellar_mgmt.data == True:
                requested_services.append("Cellar Management")
            if wineconsultform.rare_and_vintage.data == True:
                requested_services.append("Rare and Vintage")
            if wineconsultform.curate_case.data == True:
                requested_services.append("Curated Cases")
            if businessconsultform.retail.data == True:
                requested_services.append("Retail Business Consulting")
            if businessconsultform.hotel_rest.data == True:
                requested_services.append("Hotel and Restaurant Business Consulting")

            subject = "Services Contact"
            body = "Name: " + hiresommform.first_name.data + " " + hiresommform.last_name.data + "\n" + "Email: " + hiresommform.email.data + "\n" + "Zip: " + str(hiresommform.zip.data) + "\n" + "Phone: " + str(hiresommform.phone.data) + "\n" + "Services: " + str(requested_services) + "\n" + "Comments: " + hiresommform.comments.data
            msg = f'subject: {subject}\n\n{body}'
            smtp.sendmail(email_address, "wellingtonwineconsulting@gmail.com", msg)

            first_name = hiresommform.first_name.data
            last_name = hiresommform.last_name.data
            return render_template("thank_you.html", first_name=first_name, last_name=last_name)

    #### Hire Somm Form ###
    # hiresommform = HireSommForm()
    # if hiresommform.validate_on_submit():
    #
    #     email_address = "wwcwebsite1@gmail.com"
    #     email_password = "awpjpzzgtoskbwhj"
    #     with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    #         smtp.ehlo()
    #         smtp.starttls()
    #         smtp.ehlo()
    #         smtp.login(email_address, email_password)
    #
    #         requested_services = []
    #
    #         if hiresommform.private_dinner.data == True:
    #             requested_services.append("Private Dinner")
    #         if hiresommform.in_person_somm.data == True:
    #             requested_services.append("In Person Somm")
    #         if hiresommform.online_somm.data == True:
    #             requested_services.append("Online Somm")
    #
    #         subject = "Hire Sommelier Contact"
    #         body = "Name: " + hiresommform.first_name.data + " " + hiresommform.last_name.data + "\n" + "Email: " + hiresommform.email.data + "\n" + "Zip: " + str(hiresommform.zip.data) + "\n" + "Phone: " + str(hiresommform.phone.data) + "\n" + "Services: " + str(requested_services) + "\n" + "Comments: " + hiresommform.comments.data
    #         msg = f'subject: {subject}\n\n{body}'
    #         smtp.sendmail(email_address, email_address, msg)
    #
    #         print(requested_services)
    #
    #         first_name = hiresommform.first_name.data
    #         last_name = hiresommform.last_name.data
    #         return render_template("thank_you.html", first_name=first_name, last_name=last_name)
    #         # return redirect(url_for("thank_you"), first_name=first_name, last_name=last_name)
    #
    # ### Wine Consult Form ###
    # wineconsultform = WineConsultForm()
    # if wineconsultform.validate_on_submit():
    #
    #     email_address = "wwcwebsite1@gmail.com"
    #     email_password = "awpjpzzgtoskbwhj"
    #     with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    #         smtp.ehlo()
    #         smtp.starttls()
    #         smtp.ehlo()
    #         smtp.login(email_address, email_password)
    #
    #         requested_services = []
    #
    #         if wineconsultform.cellar_mgmt.data == True:
    #             requested_services.append("Cellar Management")
    #         if wineconsultform.rare_and_vintage.data == True:
    #             requested_services.append("Rare and Vintage")
    #         if wineconsultform.curate_case.data == True:
    #             requested_services.append("Curated Cases")
    #
    #         subject = "Wine Consulting Contact"
    #         body = "Name: " + wineconsultform.first_name.data + " " + wineconsultform.last_name.data + "\n" + "Email: " + wineconsultform.email.data + "\n" + "Zip: " + str(wineconsultform.zip.data) + "\n" + "Phone: " + str(wineconsultform.phone.data) + "\n" + "Services: " + str(requested_services) + "\n" + "Comments: " + wineconsultform.comments.data
    #         msg = f'subject: {subject}\n\n{body}'
    #         smtp.sendmail(email_address, email_address, msg)
    #
    #         print(requested_services)
    #
    #         first_name = wineconsultform.first_name.data
    #         last_name = wineconsultform.last_name.data
    #         return render_template("thank_you.html", first_name=first_name, last_name=last_name)
    #
    # ### Business Consult Form ###
    # businessconsultform = BusinessConsultForm()
    # if businessconsultform.validate_on_submit():
    #
    #     email_address = "wwcwebsite1@gmail.com"
    #     email_password = "awpjpzzgtoskbwhj"
    #     with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    #         smtp.ehlo()
    #         smtp.starttls()
    #         smtp.ehlo()
    #         smtp.login(email_address, email_password)
    #
    #         requested_services = []
    #
    #         if businessconsultform.retail.data == True:
    #             requested_services.append("Retail Business Consulting")
    #         if businessconsultform.hotel_rest.data == True:
    #             requested_services.append("Hotel and Restaurant Business Consulting")
    #
    #         subject = "Business Consulting Contact"
    #         body = "Name: " + businessconsultform.first_name.data + " " + businessconsultform.last_name.data + "\n" + "Email: " + businessconsultform.email.data + "\n" + "Zip: " + str(businessconsultform.zip.data) + "\n" + "Phone: " + str(businessconsultform.phone.data) + "\n" + "Services: " + str(requested_services) + "\n" + "Comments: " + businessconsultform.comments.data
    #         msg = f'subject: {subject}\n\n{body}'
    #         smtp.sendmail(email_address, email_address, msg)
    #
    #         first_name = businessconsultform.first_name.data
    #         last_name = businessconsultform.last_name.data
    #         return render_template("thank_you.html", first_name=first_name, last_name=last_name)

    return render_template("services.html", hiresommform=hiresommform, wineconsultform=wineconsultform, businessconsultform=businessconsultform)

@app.route('/contact', methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route('/thank_you')
def thank_you():
    return render_template("thank_you.html")

if __name__ == '__main__':
    app.run(debug=True)




# if form.validate_on_submit():
#     email_address = "wwcwebsite1@gmail.com"
#     email_password = "awpjpzzgtoskbwhj"
#     with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#         smtp.ehlo()
#         smtp.starttls()
#         smtp.ehlo()
#
#         smtp.login(email_address, email_password)
#
#         subject = "Website Launch"
#         body = form.email.data
#         msg = f'subject: {subject}\n\n{body}'
#         smtp.sendmail(email_address, email_address, msg)
#         return render_template("thankyou.html")
