/* script_runner/static/script_runner/scripts.js */
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.text())
        .then(data => {
            const outputDiv = document.querySelector('.output');
            outputDiv.innerHTML = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
