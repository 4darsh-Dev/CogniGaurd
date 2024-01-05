
// This script will be injected into all web pages

// Function to send website data to the API
const sendWebsiteData = () => {
  const websiteData = {
      url: window.location.href,
      // Add more data as needed
  };

  // Send data to API
  fetch(apiUrl, {
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

// Execute the function when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", sendWebsiteData);
