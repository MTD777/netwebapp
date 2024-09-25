// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');
    const form = document.getElementById('script-form');
    const outputDiv = document.getElementById('output');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        console.log('Form submitted');

        // Find the clicked button
        const clickedButton = document.activeElement;
        const scriptName = clickedButton.value;

        const formData = new FormData(form);
        formData.append('script_name', scriptName);

        // Log form data for debugging
        for (let [key, value] of formData.entries()) {
            console.log(`${key}: ${value}`);
        }

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => {
            console.log('Fetch response received');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            console.log('Fetch successful');
            outputDiv.innerHTML = data;
        })
        .catch(error => {
            console.error('Fetch error:', error);
            outputDiv.innerHTML = `<p>Error: ${error}</p>`;
        });
    });
});
