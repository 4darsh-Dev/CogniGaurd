console.log("CogniGuard Popup working!");

// api endpoint
const apiUrl = "http://127.0.0.1:8000/api/";

// Function to fetch transparency score
const fetchTransparencyScore = () => {
    // Fetching transparency score from api
    fetch(apiUrl + "tp-score/")
        .then(response => {
            if (!response.ok) {
                throw new Error("Response was not ok!");
            }
            return response.json();
        })
        .then(userData => {
            // Process the retrieved data
            
            const transparencyScore = userData.transparency_score;
            const transparencyScoreElement = document.getElementById("transparencyScore");
            transparencyScoreElement.textContent = `${transparencyScore}`;
            updateTransparencyMeter(transparencyScore);
            
        })
        .catch(error => {
            console.log("Error", error);
        });
};

// Fetch transparency score when DOM is loaded
document.addEventListener("DOMContentLoaded", fetchTransparencyScore);

function updateTransparencyMeter(transparencyScore) {
    const arrowElement = document.getElementById("arrow");
    const scoreDisplayElement = document.getElementById("score-display");

    // Calculate arrow rotation based on transparency score
    const rotation = (transparencyScore / 10) * 180 - 90;
    
    // Rotate arrow and update score display
    arrowElement.style.transform = `rotate(${rotation}deg)`;
    scoreDisplayElement.innerText = transparencyScore;
}
