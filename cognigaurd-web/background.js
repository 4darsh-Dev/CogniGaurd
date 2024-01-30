<<<<<<< HEAD
// chrome.runtime.onMessage.addListener(
//   function (request, sender, sendResponse) {
//     if (request.message === "open_popup") {
//       chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
//         chrome.tabs.sendMessage(tabs[0].id, { "message": "open_popup" });
//       });
//     }
//   }
// );


// Sending get request to django server

// $(function () {


//   $('#analyze-btn').click(function () {
//     let websiteData = {
//       url: window.location.href,
//       // Add more data as needed
//     };


//     let search_url = websiteData.url;
//     console.log(search_url);

//     if (search_url) {
//       chrome.runtime.sendMessage(
//         { url: search_url },
//         function (response) {
//           result = response.farewell;
//           alert(result.summary);

//           // Displaying dark patterns
//           let scanResultBox = document.getElementsByClassName("scan-result-box")[0];
//           const displayDp = (response, length) => {
//             let head = document.createElement('h2');
//             head.innerText = "What we have found so far:";
//             scanResultBox.appendChild(head);

//             let scanList = document.createElement("ul");
//             scanList.classList.add("scan-list");
//             scanResultBox.appendChild(scanList);

//             let responseArr = [];

//             for (let i = 0; i < length; i++) {
//               let scanItems = document.createElement("li");
//               scanItems.classList.add("scan-items");
//               scanItems.innerText = `${responseArr[0]}`;
//               scanList.appendChild(scanItems);
//             }
//           };

//         });
//     }


//     // $('#keyword').val('');

//   });
// });


chrome.runtime.onMessage.addListener(
  function (request, sender, sendResponse) {
    if (request.message === "open_popup") {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { "message": "open_popup" });
      });
    } else if (request.url) {
      // Perform the GET request to the Django server
      fetchDjangoData(request.url, sendResponse);
    }

    // Ensure sendResponse is called asynchronously
    return true;
  }
);

function fetchDjangoData(url, sendResponse) {
  // Perform the GET request to Django server
  fetch('http://127.0.0.1:8000/api/dp-data/?url=' + encodeURIComponent(url))
    .then(response => response.json())
    .then(data => {
      // Handle the data received from the server
      console.log(data);

      // Optionally, send a response back to the content script if needed
      sendResponse({ dp_data: data });
    })
    .catch(error => {
      console.error('Error fetching data from Django server:', error);
    });
}
=======
const fs = require('fs');
const sendWebsiteData = (dat) => {
  const websiteData = {
      img: dat,
      // Add more data as needed
  };

  newapiUrl="http://127.0.0.1:8000/"

  console.log(websiteData);

  // Send data to API
  fetch(newapiUrl +"popup_detect/", {
    
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify(websiteData),
  })
      .then(response => {
          if (!response.ok) {
              throw new Error("Error sending website data to API");
          }
          return response.json();
      })
      .then(apiResponse => {
          console.log("API Response:", apiResponse);
      })
      .catch(error => {
          console.error("Error:", error);
      });
};

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo,tab) {
  if (changeInfo.status == 'complete' && !tab.url.startsWith('chrome://')) {
    chrome.scripting.executeScript({
      target: { tabId: tabId },
      files: ['popup_detectV2.js']
    });
  }
});

let lastMessageTime = Date.now();


chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {      
  if (request.message === "open_popup") {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, {"message": "open_popup"});
    });
  }
  
  const currentTime = Date.now();
  
  
  if (currentTime - lastMessageTime < 3000) {
    lastMessageTime = currentTime;
    return; // Ignore the message if it's within 3 second of the previous message
  }
  
  lastMessageTime = currentTime;
  
  if (request.message == "center popup" || request.message == "side popup") {
    const tabId = sender.tab.id;
    
    chrome.tabs.captureVisibleTab(null, {}, function (dataUrl){
      console.log('Popup detected on ' + sender.tab.url);
      console.log(typeof(dataUrl));
      sendWebsiteData(dataUrl);
    });
    
    // console.log('Popup count for tab ' + tabId + ': ' + popup_cnt[tabId]);
  } else {
    console.log(request.message);
    sendWebsiteData(dataUrl);
  }
});

// Capture screenshot on click
chrome.tabs.onActivated.addListener(function(activeInfo) {
  chrome.tabs.captureVisibleTab(null, {}, function (dataUrl){
    // console.log('Screenshot captured on ' + tab.url);
    // console.log(typeof(dataUrl));
    sendWebsiteData(dataUrl);

    // Write data URL to file
    fs.writeFile('ss_scrape.txt', dataUrl, function(err) {
      if (err) {
        console.error('Error writing data URL to file:', err);
      } else {
        console.log('Data URL written to ss_scrape.txt');
      }
    });
  });
});

// function convertDataUrlToRgb(dataUrl) {
//   const canvas = document.createElement('canvas');
//   const context = canvas.getContext('2d');
//   const image = new Image();

//   return new Promise((resolve, reject) => {
//     image.onload = function() {
//       canvas.width = image.width;
//       canvas.height = image.height;
//       context.drawImage(image, 0, 0);

//       const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
//       const pixels = imageData.data;

//       const rgbData = [];
//       for (let i = 0; i < pixels.length; i += 4) {
//         const r = pixels[i];
//         const g = pixels[i + 1];
//         const b = pixels[i + 2];
//         rgbData.push([r, g, b]);
//       }

//       resolve(rgbData);
//     };

//     image.onerror = function() {
//       reject(new Error('Failed to load image'));
//     };

//     image.src = dataUrl;
//   });
// }
>>>>>>> origin/main
