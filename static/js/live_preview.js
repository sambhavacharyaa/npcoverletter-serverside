document.addEventListener('DOMContentLoaded', function () {

    // Escape user input before inserting into HTML
    function escapeHtml(str) {
        const div = document.createElement('div');
        div.textContent = str || '';
        return div.innerHTML;
    }


    // Get value from input field
    function val(id) {
        const el = document.getElementById(id);
        return el ? escapeHtml(el.value.trim()) : '';
    }


    // Convert uploaded stamp image into base64 preview
    function getStampPreview(inputId, callback) {

        const input = document.getElementById(inputId);

        // No image selected
        if (!input || !input.files || !input.files[0]) {
            callback("");
            return;
        }

        const reader = new FileReader();

        // Return base64 image
        reader.onload = function (e) {
            callback(e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }


    function renderPersonalLetter() {

        const full_name = val('id_personal-full_name') || '________';
        const address = val('id_personal-address') || '________';
        const domain_name = val('id_personal-domain_name') || '________';
        const domain_tld = val('id_personal-domain_tld') || '.com.np';
        const purpose = val('id_personal-purpose') || '________';
        const ns1 = val('id_personal-ns1') || '________';
        const ns2 = val('id_personal-ns2') || '________';
        const email = val('id_personal-email') || '________';
        const phone = val('id_personal-phone') || '________';

        return `

<p>
    To,<br>
    Hostmaster<br>
    Mercantile Communications Pvt. Ltd.
</p>


<p>
    <strong>Subject: Request for ${domain_tld} Domain Registration</strong>
</p>


<p>
    Dear Sir/Madam,
</p>


<p>
    I am <strong>${full_name}</strong>, residing at ${address}.
    I would like to request the registration of a domain under the .np ccTLD.
</p>


<div class="domain-box">

    <p>
        <strong>Domain:</strong>
        ${domain_name}${domain_tld}
    </p>

    <p>
        <strong>Primary Name Server (NS1):</strong>
        ${ns1}
    </p>

    <p>
        <strong>Secondary Name Server (NS2):</strong>
        ${ns2}
    </p>

</div>


<p>
    <strong>Purpose of registering this domain:</strong><br>
    ${purpose}
</p>


<p>
    I kindly request you to approve my domain registration request.
</p>


<p>
    Thank you.
</p>


<p>
    Sincerely,<br><br>
    <strong>${full_name}</strong>
    <br>
    Email: ${email}<br>
    Phone: ${phone}
</p>

`;
    }



function renderBusinessLetter(stamp = "") {

    const company_name = val('id_business-company_name') || '________';
    const representative_name = val('id_business-representative_name') || '________';
    const domain_name = val('id_business-domain_name') || '________';
    const domain_tld = val('id_business-domain_tld') || '.com.np';
    const address = val('id_business-address') || '________';
    const business_description = val('id_business-business_description') || '________';
    const ns1 = val('id_business-ns1') || '________';
    const ns2 = val('id_business-ns2') || '________';
    const representative_email = val('id_business-representative_email') || '________';
    const representative_phone = val('id_business-representative_phone') || '________';
    return `

<!-- Business Letterhead -->
<!-- Business Letterhead -->
<div class="text-center border-b-2 border-gray-200 pb-5 mb-8">

    <h1 class="m-0 text-2xl font-bold text-gray-900">
        ${company_name}
    </h1>
     <h2 class="m-0 text-1xl font-bold text-gray-900">
        ${address}
    </h2>

</div>


<p>
    To,<br>
    Hostmaster<br>
    Mercantile Communications Pvt. Ltd.
</p>


<p>
    <strong>
        Subject: Request for ${domain_tld} Domain Registration
    </strong>
</p>


<p>
    Dear Sir/Madam,
</p>


<p>
    We, <strong>${company_name}</strong>, would like to request
    the registration of a domain under the .np ccTLD for our organization.
</p>


<div class="domain-box">

    <p>
        <strong>Domain:</strong>
        ${domain_name}${domain_tld}
    </p>

    <p>
        <strong>Primary Name Server (NS1):</strong>
        ${ns1}
    </p>

    <p>
        <strong>Secondary Name Server (NS2):</strong>
        ${ns2}
    </p>

</div>


<p>
    <strong>Organization Address:</strong><br>
    ${address}
</p>


<p>
    <strong>Business Description:</strong><br>
    ${business_description}
</p>


<p>
    The authorized representative for this domain registration request is
    <strong>${representative_name}</strong>.
</p>


<p>
    We kindly request you to approve our domain registration request.
</p>


<p>
    Thank you.
</p>


<p>
    Sincerely,<br><br>

    <strong>${representative_name}</strong><br>

    ${company_name}
    <br>
    Email: ${representative_email}<br>
    Phone: ${representative_phone}

</p>


${stamp ? `

<div class="stamp">

    <img src="${stamp}" width="120">

</div>

` : ''}


`;

}

    const previewContainer = document.getElementById('letter-preview');


    function updatePreview() {


        const activeMode = document
            .getElementById('personal-form')
            .classList
            .contains('hidden')
            ? 'business'
            : 'personal';



        if (activeMode === "personal") {

            previewContainer.innerHTML = renderPersonalLetter();

        } else {


            getStampPreview(
                "id_business-business_stamp",
                function(stamp) {

                    previewContainer.innerHTML =
                        renderBusinessLetter(stamp);

                }
            );

        }

    }



    // Prevent excessive rendering while typing
    let debounceTimer;


    function scheduleUpdate() {

        clearTimeout(debounceTimer);

        debounceTimer = setTimeout(
            updatePreview,
            150
        );

    }



    // Listen for typing changes
    document
        .getElementById('personal-form')
        .addEventListener(
            'input',
            scheduleUpdate
        );


    document
        .getElementById('business-form')
        .addEventListener(
            'input',
            scheduleUpdate
        );



    // Listen for stamp upload
    const stampInput = document.getElementById(
        'id_business-business_stamp'
    );


    if (stampInput) {

        stampInput.addEventListener(
            'change',
            updatePreview
        );

    }



    // Update when switching tabs
    document
        .getElementById('personal-btn')
        .addEventListener(
            'click',
            updatePreview
        );


    document
        .getElementById('business-btn')
        .addEventListener(
            'click',
            updatePreview
        );



    // Initial render
    updatePreview();

});