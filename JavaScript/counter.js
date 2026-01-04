   let counter = 0;
        function count() {
            counter++;
            alert(counter);
            document.querySelector("h1").innerHTML = counter;
            
            if (counter % 5 === 0) {
                alert("Count is now " + counter);
            } 
        }
    document.addEventListener("DOMContentLoaded", function() {

        document.querySelector('button').addEventListener('click', count);
   
    });