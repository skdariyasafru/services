document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("serviceSearch");
    const searchButton = document.getElementById("searchButton");
    const searchResults = document.getElementById("searchResults");

    if (!searchInput || !searchButton) return;

    searchButton.addEventListener("click", function () {
        const query = searchInput.value.trim();
        if (!query) {
            searchInput.focus();
            return;
        }
        console.log("Searching:", query);
    });

    searchInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            searchButton.click();
        }
    });

    searchInput.addEventListener("input", function () {
        const query = searchInput.value.trim();
        if (searchResults) {
            if (query.length < 2) {
                searchResults.classList.remove("show");
                searchResults.innerHTML = "";
            }
            // Flask AJAX search will be connected here later.
        }
    });
});
