chrome.tabs.onUpdated.addListener(function(tabId, changeInfo) {
  if (changeInfo.status == 'complete') {
    console.log("hello")
    chrome.scripting.executeScript({
      target: { tabId: tabId },
      files: ['popup_detect.js']
    });
  }
});

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      if (request.message === "open_popup") {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
          chrome.tabs.sendMessage(tabs[0].id, {"message": "open_popup"});
        });
      }
      if (message.type == 'popupDetected') {
        const tabId = sender.tab.id;
        if (popup_cnt[tabId]) {
          popup_cnt[tabId]++;
        } else {
          popup_cnt[tabId] = 1;
        }
        console.log('Popup detected on ' + sender.tab.url);
        // console.log('Popup count for tab ' + tabId + ': ' + popup_cnt[tabId]);
      }
    });

  