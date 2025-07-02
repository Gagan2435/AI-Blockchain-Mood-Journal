document.getElementById("analyzeSaveBtn").addEventListener("click", function() {
    const entry = document.getElementById("entry").value;
    if (!entry) {
        alert("Please write something!");
        return;
    }

    // For now, show placeholder result
    document.getElementById("emotionResult").innerText = "Analyzing... (Backend will handle this)";
});
