
def generate_personal_letter(data):
    full_name = data["full_name"]
    address = data["address"]
    citizenship_number = data["citizenship_number"]
    domain_name = data["domain_name"]
    purpose = data["purpose"]
    ns1 = data["ns1"]
    ns2 = data["ns2"]

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
    My citizenship number is <strong>{citizenship_number}</strong>.
</p>

<p>
    I kindly request you to approve my domain registration request.
</p>

<p>
    Thank you.
</p>

<p>
    Sincerely,<br><br>
    <strong>{full_name}</strong>
</p>
"""

    return letter

def generate_business_letter(data):
    company_name = data["company_name"]
    representative_name = data["representative_name"]
    domain_name = data["domain_name"]
    business_description = data["business_description"]
    registration_number = data["company_registration_number"]
    ns1 = data["ns1"]
    ns2 = data["ns2"]

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
    Registration Number: {registration_number}
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
    We kindly request you to approve our domain registration request.
</p>

<p>
    Thank you.
</p>

<p>
    Sincerely,<br><br>
    <strong>{representative_name}</strong><br>
    {company_name}
</p>
"""

    return letter