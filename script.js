document.getElementById('submitBtn').addEventListener('click', function() {
    const text = document.getElementById('journalInput').value;
    if (text.trim() === "") {
        alert("Please enter some text before submitting.");
        return;
    }
    const hashedText = sha256(text);
    document.getElementById('result').innerText = `Entry hashed successfully:\n${hashedText}`;
});

// Simple SHA-256 hashing using SubtleCrypto API
function sha256(message) {
    const encoder = new TextEncoder();
    const data = encoder.encode(message);
    return crypto.subtle.digest('SHA-256', data).then(hashBuffer => {
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
        return hashHex;
    });
}
