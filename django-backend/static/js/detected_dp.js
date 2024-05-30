document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const suggestions = document.getElementById('suggestions');
    const results = document.getElementById('results');

    searchInput.addEventListener('keyup', function() {
        const query = searchInput.value;
        if (query.length > 2) {
            fetch(`/detected_dp/?query=${query}`, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                suggestions.innerHTML = '';
                data.results.forEach(item => {
                    const suggestionItem = document.createElement('div');
                    suggestionItem.classList.add('suggestion-item');
                    suggestionItem.textContent = `${item.website_url} - ${item.dark_pattern_label}`;
                    suggestionItem.addEventListener('click', () => displayResult(item));
                    suggestions.appendChild(suggestionItem);
                });
            });
        } else {
            suggestions.innerHTML = '';
        }
    });

    function displayResult(item) {
        results.innerHTML = '';
        const resultItem = document.createElement('div');
        resultItem.classList.add('result-item');
        resultItem.innerHTML = `<strong>URL:</strong> ${item.website_url}<br>
                                <strong>Dark Pattern:</strong> ${item.dark_pattern_label}<br>
                                <strong>Details:</strong> ${item.dark_text}`;
        results.appendChild(resultItem);
    }
});
