prev_node = "";

observer = new MutationObserver(function (mutations) {
  mutations.forEach((mutation) => {
    if (mutation.attributeName === "style") {
      try {
        let elems = document.querySelectorAll("." + mutation.target.className);

        if (prev_node === mutation.target.className) return;
        
        if (elems.length <= 30) {
          Array.from(elems).forEach((elem) => {
            
            temp = elem.getBoundingClientRect();
            
            if (Math.abs(temp.left + temp.width / 2 - window.innerWidth / 2) <30 && Math.abs(temp.top + temp.height / 2 - window.innerHeight / 2) < 30) {
              chrome.runtime.sendMessage({
                message: "center popup"
              });
              return;
            } 
            
            else {
              chrome.runtime.sendMessage({
                message: "side popup"
              });              
              
              return;
            }
          });
        }
      }
      
      catch (err) {}
      prev_node = mutation.target.className;
    }
  });
});

observer.observe(document, {
  attributes: true,
  childList: true,
  subtree: true,
});
