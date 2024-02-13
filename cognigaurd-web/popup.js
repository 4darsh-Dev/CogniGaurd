// Description: This file contains the JavaScript code for the popup window of the Chrome extension. 

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

// Sending the url to the api
function sendUrlToAPI(url) {
  // Construct the Basic Auth header
  
  // Checking for erroneous url
  // url = encodeURIComponent(url);
  console.log(url);

  var username = 'cogni';
  var password = 'Mycogni@420';
  var credentials = username + ':' + password;
  var base64Credentials = btoa(credentials);

  // Make an AJAX request to your Django Rest Framework API
  fetch(apiUrl + 'dp-request/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Basic ' + base64Credentials
      },
      body: JSON.stringify({ url: url })

  })
  .then(response => {
      if (response.ok) {
          console.log('URL sent successfully');
          // Handle success as needed
          let respondseJson =  response.json();
          console.log(respondseJson);
          // Display the dark patterns
          displayDp(respondseJson, respondseJson.length);
          
          
      } else {
          console.error('Failed to send URL');
          // Handle error as needed
      }
  })
  .catch(error => {
      console.error('Error:', error);
      // Handle error as needed
  });


}






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



document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the "Analyze" button
    
    document.getElementById('analyze-btn').addEventListener('click', function () {
      // Get the current tab's URL using the Chrome Extension API
      chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
          let currentUrl = tabs[0].url;
          // Send the URL to the API
          sendUrlToAPI(currentUrl);
      });
  });

    // opening new tabs on clicking the buttons on the web extension


    // Base url
    let baseUrl = "http://127.0.0.1:8000/";
      let reportBtn = document.getElementById("report-btn");

      reportBtn.addEventListener("click", function(){
        let newTabUrl = baseUrl+"report-dp/";
        // Use chrome.tabs.create to open a new tab
          console.log("i am opening report page");
          chrome.tabs.create({ url: newTabUrl });


      })

      let helpBtn = document.getElementById("help-btn");
      helpBtn.addEventListener("click", function(){
        let newTabUrl = baseUrl+"faqs/";

        chrome.tabs.create({ url: newTabUrl });
        
      })

      let tandcBtn = document.getElementById("tandc-btn");
      tandcBtn.addEventListener("click", function(){
        let newTabUrl = baseUrl+"terms-conditions/";

        chrome.tabs.create({ url: newTabUrl });

      })

      let knowDp = document.getElementById("know-dp");
      knowDp.addEventListener("click", ()=>{
        let newTabUrl = baseUrl+"know-dp/";

        chrome.tabs.create({ url: newTabUrl });
      })

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
  
// opening new tabs on clicking the buttons on the web extension



