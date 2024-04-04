function showSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'flex';

    sidebar.style.transition = "opacity 0.3s ease, transform 0.3s ease";
    
    
    setTimeout(function() {
        sidebar.style.opacity = "1";
        sidebar.style.transform = "translateX(0)";

        setTimeout(function() {
            sidebar.style.transition = "";
        },400);
    }, 100);
    
  }
function hideSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'none'
  }

  // document.getElementById('contact-form').addEventListener('submit', function(event) {
  //   alert('Message sent!');
  // });