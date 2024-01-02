// Implement your dark pattern detection logic here
// For simplicity, this example always shows the popup

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      if (request.message === "clicked_browser_action") {
        chrome.runtime.sendMessage({"message": "open_popup"});
      }
    }
  );
  