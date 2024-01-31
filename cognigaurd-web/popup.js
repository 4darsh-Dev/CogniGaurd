// console.log("CogniGuard Popup working!");

// // api endpoint
// const apiUrl = "http://127.0.0.1:8000/api/";

// // Function to fetch transparency score
// const fetchTransparencyScore = () => {
//     // Fetching transparency score from api
//     fetch(apiUrl + "tp-score/")
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error("Response was not ok!");
//             }
//             return response.json();
//         })

//         .then(userData => {
//             // Process the retrieved data
            
//             const transparencyScore = userData.transparency_score;
//             const transparencyScoreElement = document.getElementById("transparencyScore");
//             transparencyScoreElement.textContent = `${transparencyScore}`;
//             updateTransparencyMeter(transparencyScore);
            
//         })
//         .catch(error => {
//             console.log("Error", error);
//         });
        
// };

// // Fetch transparency score when DOM is loaded
// document.addEventListener("DOMContentLoaded", fetchTransparencyScore);

// function updateTransparencyMeter(transparencyScore) {
//     const arrowElement = document.getElementById("arrow");
//     const scoreDisplayElement = document.getElementById("score-display");

//     // Calculate arrow rotation based on transparency score
//     const rotation = (transparencyScore / 10) * 180 - 90;
    
//     // Rotate arrow and update score display
//     arrowElement.style.transform = `rotate(${rotation}deg)`;
//     scoreDisplayElement.innerText = transparencyScore;
// }

// // Displaying dark patterns
// let scanResultBox = document.getElementsByClassName("scan-result-box")[0];
// const displayDp = (response, length) =>{
    
    
//     let head = document.createElement('h2');
//     head.innerText = "What we have found so far:";

//     scanResultBox.appendChild(head)

//     let scanList = document.createElement("ul");
//     scanList.classList.add("scan-list");

//     scanResultBox.appendChild(scanList)

//     let responseArr = []   

//     for(let i=0; i<length; i++)
//     {
//         let scanItems = document.createElement("li")
//         scanItems.classList.add("scan-items");

//         scanItems.innerText = `${responseArr[0]}`;

//         scanList.appendChild(scanItems);


//     }


// }

// let analyzeBtn = document.getElementById("analyze-btn");

// analyzeBtn.addEventListener("click", displayDp);


// // CSRF Token / fixing the 403 forbidden error

// // CSRF Token / fixing the 403 forbidden error

// // csrfUrl = "http://127.0.0.1:8000/api/csrf/";

// const fetchCsrfToken = async () => {

//     const response = await fetch(apiUrl + "csrf/", { method: "GET" });
//     const data = await response.json();
//     console.log(data.csrfToken);
//     return data.csrfToken;

//   };
  
//   // Use an async function to fetch the CSRF token
//   const sendWebsiteData = async () => {
//     const csrfToken = await fetchCsrfToken();
  
//     const websiteData = {
//       url: window.location.href,
//       // Add more data as needed
//     };
  
//     // Send data to API
//     fetch(apiUrl + "dp-data/", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         "X-CSRFToken": csrfToken,
//       },
//       body: JSON.stringify(websiteData),
//     })
//       .then(response => {
//         if (!response.ok) {
//           throw new Error("Error sending website data to API");
//         }
//         return response.json();
//       })
//       .then(apiResponse => {
//         console.log("API Response:", apiResponse);
//       })
//       .catch(error => {
//         console.error("Error:", error);
//       });
//   };


  
//   // Execute the function when the DOM is fully loaded
//   document.addEventListener("DOMContentLoaded", sendWebsiteData);
  


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
// document.addEventListener("DOMContentLoaded", fetchTransparencyScore);

// function updateTransparencyMeter(transparencyScore) {
//     const arrowElement = document.getElementById("arrow");
//     const scoreDisplayElement = document.getElementById("score-display");

//     // Calculate arrow rotation based on transparency score
//     const rotation = (transparencyScore / 10) * 180 - 90;
    
//     // Rotate arrow and update score display
//     arrowElement.style.transform = `rotate(${rotation}deg)`;
//     scoreDisplayElement.innerText = transparencyScore;
// }

// Displaying dark patterns
let scanResultBox = document.getElementsByClassName("scan-result-box")[0];
const displayDp = (response, length) => {
    let head = document.createElement('h2');
    head.innerText = "What we have found so far:";
    scanResultBox.appendChild(head);

    let scanList = document.createElement("ul");
    scanList.classList.add("scan-list");
    scanResultBox.appendChild(scanList);

    let responseArr = [];

    for (let i = 0; i < length; i++) {
        let scanItems = document.createElement("li");
        scanItems.classList.add("scan-items");
        scanItems.innerText = `${responseArr[0]}`;
        scanList.appendChild(scanItems);
    }
};

// let analyzeBtn = document.getElementById("analyze-btn");

// // Click event listener for analyze button
// analyzeBtn.addEventListener("click", () => {
//     // Call the function to send website data when the button is clicked
//     sendWebsiteData();
// });

// // Function to fetch CSRF token
// const fetchCsrfToken = async () => {
//     const response = await fetch(apiUrl + "csrf/", { method: "GET" });
//     const data = await response.json();
//     console.log(data.csrfToken);
//     return data.csrfToken;
// };

// Function to send website data to the API
// const sendWebsiteData = async () => {
//     try {
//         const csrfToken = await fetchCsrfToken();
//         const websiteData = {
//             url: window.location.href,
//             // Add more data as needed
//         };

//         // Send data to API
//         const response = await fetch(apiUrl + "dp-data/", {
//             method: "POST",
//             credentials: "same-origin",
//             headers: {
//                 "Content-Type": "application/json",
//                 "Accept": "application/json",
//                 "X-CSRFToken": csrfToken,
//             },
//             body: JSON.stringify(websiteData),
//         });

//           if (!response.ok) {
//             throw new Error("Error sending website data to API");
//           }

//           const apiResponse = await response.json();
//           console.log("API Response:", apiResponse);
//         } catch (error) {
//           console.error("Error:", error);
//         }
    
// };


document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the "Analyze" button
    document.getElementById('analyze-btn').addEventListener('click', function () {
      // Get the current window URL
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        // Send a message to the background script with the URL
        chrome.runtime.sendMessage({ url: tabs[0].url }, function (response) {
          if (response && response.dp_data) {
            // Update the popup content with the received dark pattern data
            updatePopupContent(response.dp_data);
          } else {
            console.error("Invalid response from background script:", response);
          }
        });
      });
    });
  });
  
  function updatePopupContent(dpData) {
    // Add logic to update the popup content with the dark pattern data
    let scanResultBox = document.querySelector('.scan-result-box');
    scanResultBox.innerHTML = '';
  
    let head = document.createElement('h2');
    head.innerText = "What we have found so far:";
    scanResultBox.appendChild(head);
  
    let scanList = document.createElement("ul");
    scanList.classList.add("scan-list");
    scanResultBox.appendChild(scanList);
  
    for (let i = 0; i < dpData.length; i++) {
      let scanItems = document.createElement("li");
      scanItems.classList.add("scan-items");
      scanItems.innerText = dpData[i];
      scanList.appendChild(scanItems);
    }
  }
  