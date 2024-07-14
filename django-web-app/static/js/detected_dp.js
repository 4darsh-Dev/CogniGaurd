document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const suggestions = document.getElementById('suggestions');
    const results = document.getElementById('results');
    
    searchInput.addEventListener('keyup', function() {
        const query = searchInput.value;
        if (query.length > 2) {
            fetch(`/detected-dp/?query=${encodeURIComponent(query)}`, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                suggestions.innerHTML = '';
                data.results.forEach(item => {
                    const suggestionItem = document.createElement('div');
                    suggestionItem.classList.add('suggestion-item');
                    suggestionItem.textContent = `${item.website_url} - ${item.dark_pattern_label}`;
                    suggestionItem.addEventListener('click', () => displayResult(item));
                    suggestions.appendChild(suggestionItem);
                });
            })
            .catch(error => {
                console.error('Error:', error);
                suggestions.innerHTML = '<div>Error fetching results</div>';
            });
        } else {
            suggestions.innerHTML = '';
        }
    });

    function displayResult(item) {
        results.innerHTML = '';
        const resultItem = document.createElement('div');
        resultItem.classList.add('result-item');
        resultItem.innerHTML = `<strong>URL:</strong> ${escapeHtml(item.website_url)}<br>
                                <strong>Dark Pattern:</strong> ${escapeHtml(item.dark_pattern_label)}<br>
                                <strong>Details:</strong> ${escapeHtml(item.dark_text)}`;
        results.appendChild(resultItem);
    }

    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
});