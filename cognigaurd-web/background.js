const sendWebsiteData = (dat , type) => {
  const websiteData = {
      img: dat,
      type:type
      // Add more data as needed
  };

  // Send data to API
  fetch(apiUrl +"price-manipulation/", {
    
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
      // .then(apiResponse => {
      //     console.log("API Response:", apiResponse);
      // })
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
        return; // Ignore the message if it's within 1 second of the previous message
      }

      lastMessageTime = currentTime;

      if (request.message == "center popup" || request.message == "side popup") {
        const tabId = sender.tab.id;
        
        chrome.tabs.captureVisibleTab(null, {}, function (dataUrl){
          console.log('Popup detected on ' + sender.tab.url);
          sendWebsiteData(dataUrl, request.message);
        });
        
        // console.log('Popup count for tab ' + tabId + ': ' + popup_cnt[tabId]);
      } else {
        console.log(request.message);
        sendWebsiteData(dataUrl, request.message);
      }
});


  