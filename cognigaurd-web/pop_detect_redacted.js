observers=new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
        // console.log(entry);
        if(entry.isIntersecting){
          if(Math.abs(entry.boundingClientRect.left+(entry.boundingClientRect.width/2)- window.innerWidth/2) < 15 && Math.abs(entry.boundingClientRect.top+(entry.boundingClientRect.height/2) - window.innerHeight/2) < 15){
            // console.log(entry)
          }
        }
    });
  },{threshold:1});
  
  target=null;
  document.querySelectorAll("*").forEach(function(target){
    observers.observe(target);
  });
  
  
  console.log(document.getElementsByClassName("grid grid-cols-7 md:grid-cols-12 mx-auto h-full relative").getboundingClientRect);
  
  // once finalizing a popup element eliminate the intersectionobserver then just observe it to reduce computataion
  // add more filters to prevent false positive
  // like : keyword matching in text
  /*
  z index
  centering
  close button 
  modal
  background opacity
  
  */