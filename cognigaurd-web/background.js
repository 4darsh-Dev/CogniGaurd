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
