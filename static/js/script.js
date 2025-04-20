document.querySelectorAll(".mood-buttons button").forEach(button => {
    button.addEventListener("click", () => {
      const mood = button.getAttribute("data-mood");
  
      fetch("/get_quote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mood: mood })
      })
      .then(res => res.json())
      .then(data => {
        const quoteBox = document.getElementById("quote-text");
        quoteBox.style.opacity = 0;
        setTimeout(() => {
          quoteBox.textContent = data.quote;
          quoteBox.style.opacity = 1;
        }, 300);
      });
    });
  });
  