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
  const username = 'adarsh';
  const password = 'adarsh@123';
  const credentials = btoa(`${username}:${password}`);

  fetch(apiUrl + 'analyze-url/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Basic ' + credentials
    },
    body: JSON.stringify({ url: url })
  })
    .then(response => response.json())
    .then(data => {
      console.log('Response:', data);
      if (data.status === 'processing') {
        pollForResults(data.task_id);
      } else {
        displayDp(data.data, data.data.length);
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function pollForResults(taskId) {
  const pollInterval = setInterval(() => {
    fetch(apiUrl + `task-status/${taskId}/`, {
      method: 'GET',
      headers: {
        'Authorization': 'Basic ' + btoa('adarsh:adarsh@123')
      }
    })
      .then(response => response.json())
      .then(data => {
        if (data.status === 'completed') {
          clearInterval(pollInterval);
          displayDp(data.data, data.data.length);
        } else if (data.status === 'failed') {
          clearInterval(pollInterval);
          console.error('Task failed:', data.error);
        }
      })
      .catch(error => {
        console.error('Error polling for results:', error);
      });
  }, 5000); // Poll every 5 seconds
}





// Displaying dark patterns
let scanResultBox = document.getElementsByClassName("scan-result-box")[0];

const displayDp = (response) => {
  // Clear previous results
  scanResultBox.innerHTML = '';

  let head = document.createElement('h2');
  head.innerText = "What we have found so far:";
  scanResultBox.appendChild(head);

  let scanList = document.createElement("ul");
  scanList.classList.add("scan-list");
  scanResultBox.appendChild(scanList);

  if (response && response.length > 0) {
    response.forEach(item => {
      let scanItem = document.createElement("li");
      scanItem.classList.add("scan-item");
      scanItem.innerHTML = `
        <strong>${item.dark_pattern_label}</strong>: ${item.dark_text}
        <br>
        <small>URL: ${item.website_url}</small>
      `;
      scanList.appendChild(scanItem);
    });
  } else {
    let noResultItem = document.createElement("li");
    noResultItem.classList.add("scan-item");
    noResultItem.innerText = "No dark patterns found.";
    scanList.appendChild(noResultItem);
  }
};


document.addEventListener('DOMContentLoaded', function () {
  // Add event listener to the "Analyze" button

  document.getElementById('analyze-btn').addEventListener('click', function () {
    // Get the current tab's URL using the Chrome Extension API
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      let currentUrl = tabs[0].url;
      // Send the URL to the API
      sendUrlToAPI(currentUrl);
    });
  });

  // opening new tabs on clicking the buttons on the web extension


  // Base url
  let baseUrl = "https://cogniguard.onionreads.com/";
  let reportBtn = document.getElementById("report-btn");

  reportBtn.addEventListener("click", function () {
    let newTabUrl = baseUrl + "report-dp/";
    // Use chrome.tabs.create to open a new tab
    console.log("i am opening report page");
    chrome.tabs.create({ url: newTabUrl });


  })

  let helpBtn = document.getElementById("help-btn");
  helpBtn.addEventListener("click", function () {
    let newTabUrl = baseUrl + "faqs/";

    chrome.tabs.create({ url: newTabUrl });

  })

  let tandcBtn = document.getElementById("tandc-btn");
  tandcBtn.addEventListener("click", function () {
    let newTabUrl = baseUrl + "terms-of-use/";

    chrome.tabs.create({ url: newTabUrl });

  })

  let knowDp = document.getElementById("know-dp");
  knowDp.addEventListener("click", () => {
    let newTabUrl = baseUrl + "know-about-dp/";

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



