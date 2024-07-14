
// This script is used to handle the API key creation, copying, refreshing, and deletion logic on the dashboard page.

document.addEventListener('DOMContentLoaded', function() {
    const createButton = document.getElementById('create-api-key');
    const keyList = document.getElementById('api-key-list');

    createButton.addEventListener('click', createApiKey);

    keyList.addEventListener('click', function(e) {
        if (e.target.classList.contains('copy-key')) {
            copyKey(e.target);
        } else if (e.target.classList.contains('refresh-key')) {
            refreshKey(e.target);
        } else if (e.target.classList.contains('delete-key')) {
            deleteKey(e.target);
        }
    });

    function createApiKey() {
        fetch('/create-api-key/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            const newRow = `
                <tr data-key-id="${data.id}">
                    <td>${data.name}</td>
                    <td>${data.key.slice(0, 8)}************************</td>
                    <td>${new Date(data.expires_at).toLocaleString()}</td>
                    <td>
                        <button class="copy-key" data-key="${data.key}">Copy</button>
                        <button class="refresh-key">Refresh</button>
                        <button class="delete-key">Delete</button>
                    </td>
                </tr>
            `;
            keyList.insertAdjacentHTML('beforeend', newRow);
        });
    }

    function copyKey(button) {
        const key = button.getAttribute('data-key');
        navigator.clipboard.writeText(key).then(() => {
            alert('API key copied to clipboard!');
        });
    }

    function refreshKey(button) {
        const row = button.closest('tr');
        const keyId = row.getAttribute('data-key-id');
        // Implement refresh logic here
    }

    function deleteKey(button) {
        const row = button.closest('tr');
        const keyId = row.getAttribute('data-key-id');
        if (confirm('Are you sure you want to delete this API key?')) {
            fetch(`/delete-api-key/${keyId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    row.remove();
                }
            });
        }
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
