document.addEventListener("DOMContentLoaded", () => {
    // Floating emoji background
    const emojis = ['❤️', '🌈', '😡', '😢', '😃', '✨', '💫', '🌻', '🍀', '🌸'];
    const emojiContainer = document.querySelector('.emoji-container');
    for (let i = 0; i < 30; i++) {
        const emoji = document.createElement('div');
        emoji.classList.add('emoji');
        emoji.innerText = emojis[Math.floor(Math.random() * emojis.length)];
        emoji.style.left = `${Math.random() * 100}%`;
        emoji.style.top = `${Math.random() * 100}%`;
        emoji.style.fontSize = `${20 + Math.random() * 30}px`;
        emoji.style.position = "absolute";
        emoji.style.opacity = 0.3;
        emojiContainer.appendChild(emoji);
    }

    // Entry saving logic with Flask
    const submitBtn = document.getElementById('submitBtn');
    if (submitBtn) { // prevent errors on pages without this button
        submitBtn.addEventListener('click', () => {
            const entry = document.getElementById('journalInput').value.trim();

            if (!entry) {
                alert("Please write something before saving!");
                return;
            }

            fetch('/save', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ entry: entry })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Server error");
                }
                return response.json();
            })
            .then(data => {
                console.log("Returned JSON:", data);

                const result = document.getElementById('result');
                result.innerHTML = `
                    ✅ ${data.message} <br>
                    🔗 Hash: ${data.hash} <br>
                    🩺 Detected Emotion: <b>${data.emotion}</b> (${data.confidence}% confidence)
                `;
                result.style.color = "green";
                document.getElementById('journalInput').value = '';
            })
            .catch(error => {
                console.error('Error:', error);
                alert("Something went wrong. Please try again.");
            });
        });
    }

    // Dark mode toggle
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) { // prevent errors on pages without this button
        darkModeToggle.addEventListener('click', function () {
            document.body.classList.toggle('dark-mode');
        });
    }
    
});
function publishToBlockDAG(hash, buttonElement) {
    if (!confirm("Are you sure you want to publish this hash to BlockDAG?")) return;
    fetch(`/publish/${hash}`, { method: 'POST' })
    .then(response => {
        if (!response.ok) throw new Error("Failed to publish to BlockDAG.");
        return response.json();
    })
    .then(data => {
        alert(data.message);
        buttonElement.disabled = true;
        buttonElement.textContent = "✅ Published to BlockDAG";
    })
    .catch(error => {
        alert("Error publishing to BlockDAG.");
        console.error(error);
    });
}

