console.log("CogniGuard Popup working!");

// api endpoint
const apiUrl = "http://127.0.0.1:5500/tp-score";

// Function to fetch transparency score
const fetchTransparencyScore = () => {
    // Fetching transparency score from api
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error("Response was not ok!");
            }
            return response.json();
        })
        .then(userData => {
            // Process the retrieved data
            const transparencyScoreElement = document.getElementById("transparencyScore");
            transparencyScoreElement.textContent = `Transparency Score: ${userData.transparencyScore}`;
        })
        .catch(error => {
            console.log("Error", error);
        });
};

// Fetch transparency score when DOM is loaded
document.addEventListener("DOMContentLoaded", fetchTransparencyScore);
