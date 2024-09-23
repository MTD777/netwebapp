// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('script-form');
    const outputDiv = document.getElementById('output');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.text())
        .then(data => {
            outputDiv.innerHTML = data;
        })
        .catch(error => {
            outputDiv.innerHTML = `<p>Error: ${error}</p>`;
        });
    });
});
