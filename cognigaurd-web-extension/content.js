
// This script will be injected into all web pages


// Send message to background script
chrome.runtime.sendMessage({ url: window.location.href }, function(response) {
    console.log(response.result);
    // Update extension UI with the dark pattern information
    // ...
});



