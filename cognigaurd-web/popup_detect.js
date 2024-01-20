var observer = new MutationObserver(function(mutations) {
  mutations.forEach(function(mutation) {
    if (mutation.attributeName === 'style') {
      if (window.getComputedStyle(popup).visibility === 'visible') {
        var popupRect = popup.getBoundingClientRect();
        var popupCenter = { x: popupRect.left + popupRect.width / 2, y: popupRect.top + popupRect.height / 2 };
        var screenCenter = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
        if (Math.abs(popupCenter.x - screenCenter.x) < 1 && Math.abs(popupCenter.y - screenCenter.y) < 1) {
          chrome.runtime.sendMessage({type: 'popupDetected'});
        }
      }
    }
  });
});
observer.observe(document, {childList: true, subtree: true}); 