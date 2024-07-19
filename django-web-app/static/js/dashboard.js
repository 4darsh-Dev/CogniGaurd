
// // // This script is used to handle the JWT creation, copying, refreshing, and deletion logic on the dashboard page.


// Custom alert display
const createAlertDiv = () => {
    const alertDiv = document.createElement('div');
    document.body.appendChild(alertDiv);
    return alertDiv;
};

const alertDiv = createAlertDiv();

const customAlert = (message) => {
    console.log("alert called");

    alertDiv.innerHTML = '';
    alertDiv.classList.add("alert-div");

    const alertMess = document.createElement('p');
    alertMess.classList.add('alert-message');
    alertMess.innerText = message;
    alertDiv.appendChild(alertMess);

    const alertClose = document.createElement('button');
    alertClose.classList.add('alert-close');
    alertDiv.appendChild(alertClose);
    alertClose.addEventListener('click', closeAlert);

    setTimeout(() => alertDiv.classList.add('show'), 10);
};

const closeAlert = () => {
    alertDiv.classList.remove('show');
    setTimeout(() => alertDiv.style.display = 'none', 500);
};

const getCookie = (name) => {
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [cookieName, cookieValue] = cookie.trim().split('=');
            if (cookieName === name) {
                return decodeURIComponent(cookieValue);
            }
        }
    }
    return null;
};

class TokenList extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
    }

    connectedCallback() {
        this.render();
    }

    render() {
        const tokens = this.getTokens();
        this.shadowRoot.innerHTML = `
          <style>
            :host {
              display: block;
              font-family: Arial, sans-serif;
              max-width: 800px;
              margin: 20px auto;
            }
            ul {
              list-style-type: none;
              padding: 0;
            }
            li {
              background-color: #f0f0f0;
              border-radius: 8px;
              margin-bottom: 10px;
              padding: 15px;
              display: flex;
              justify-content: space-between;
              align-items: center;
              transition: all 0.3s ease;
              opacity: 0;
              transform: translateY(20px);
              animation: fadeIn 0.5s ease forwards;
            }
            li:hover {
              box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            .token-text {
              word-break: break-all;
              margin-right: 10px;
            }
            button {
              background-color: #4CAF50;
              border: none;
              color: white;
              padding: 10px 15px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 14px;
              margin: 4px 2px;
              cursor: pointer;
              border-radius: 4px;
              transition: all 0.3s ease;
            }
            button:hover {
              background-color: #45a049;
              transform: translateY(-2px);
            }
            button.delete {
              background-color: #f44336;
            }
            button.delete:hover {
              background-color: #da190b;
            }
            @keyframes fadeIn {
              to {
                opacity: 1;
                transform: translateY(0);
              }
            }
          </style>
          <ul>
            ${tokens.map((token, index) => `
              <li style="animation-delay: ${index * 0.1}s">
                <span class="token-text">${token}</span>
                <div>
                  <button data-index="${index}">Copy</button>
                  <button class="delete" data-index="${index}">Delete</button>
                </div>
              </li>
            `).join('')}
          </ul>
        `;
        this.addEventListeners();
    }

    addEventListeners() {
        this.shadowRoot.addEventListener('click', (e) => {
            if (e.target.tagName === 'BUTTON') {
                const index = e.target.dataset.index;
                if (e.target.textContent === 'Copy') {
                    this.copyToken(index);
                } else if (e.target.textContent === 'Delete') {
                    this.deleteToken(index);
                }
            }
        });
    }

    getTokens() {
        return JSON.parse(localStorage.getItem('jwtTokens') || '[]');
    }

    addToken(token) {
        const tokens = this.getTokens();
        tokens.push(token);
        localStorage.setItem('jwtTokens', JSON.stringify(tokens));
        this.render();
    }

    copyToken(index) {
        const tokens = this.getTokens();
        navigator.clipboard.writeText(tokens[index])
            .then(() => customAlert('Token copied to clipboard!'))
            .catch(err => console.error('Error copying token: ', err));
    }

    deleteToken(index) {
        const tokens = this.getTokens();
        tokens.splice(index, 1);
        localStorage.setItem('jwtTokens', JSON.stringify(tokens));
        this.render();
    }
}

customElements.define('token-list', TokenList);

document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-token');
    const copyBtn = document.getElementById('copy-token');
    const tokenSpan = document.getElementById('token');
    const tokenList = document.querySelector('token-list');

    generateBtn.addEventListener('click', () => {
        fetch('/generate-token/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            },
        })
            .then(response => response.json())
            .then(data => {
                tokenSpan.textContent = data.token;
                copyBtn.disabled = false;
                tokenList.addToken(data.token);
                customAlert('Token generated successfully!');
            })
            .catch(error => console.error('Error:', error));
    });

    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(tokenSpan.textContent)
            .then(() => customAlert('Token copied to clipboard!'))
            .catch(err => console.error('Error copying token: ', err));
    });
});