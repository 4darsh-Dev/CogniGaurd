


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

