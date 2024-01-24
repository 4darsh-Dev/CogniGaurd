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

// Displaying dark patterns
let scanResultBox = document.getElementsByClassName("scan-result-box")[0];
const displayDp = (response, length) =>{
    
    
    let head = document.createElement('h2');
    head.innerText = "What we have found so far:";

    scanResultBox.appendChild(head)

    let scanList = document.createElement("ul");
    scanList.classList.add("scan-list");

    scanResultBox.appendChild(scanList)

    let responseArr = []   

    for(let i=0; i<length; i++)
    {
        let scanItems = document.createElement("li")
        scanItems.classList.add("scan-items");

        scanItems.innerText = `${responseArr[0]}`;

        scanList.appendChild(scanItems);


    }


}

let analyzeBtn = document.getElementById("analyze-btn");

analyzeBtn.addEventListener("click", displayDp);

