// Example fingerprint login using WebAuthn
async function loginWithFingerprint() {
    if (!window.PublicKeyCredential) {
        alert("Fingerprint not supported in this browser.");
        return;
    }
    
    const publicKeyCredentialRequestOptions = {
        challenge: new Uint8Array(32),
        allowCredentials: [],
        timeout: 60000,
    };
    
    try {
        const assertion = await navigator.credentials.get({
            publicKey: publicKeyCredentialRequestOptions
        });
        // Send assertion to server for verification
        const response = await fetch('/verify-fingerprint', {
            method: 'POST',
            body: JSON.stringify(assertion)
        });
        if (response.ok) {
            window.location.href = "dashboard.html";
        }
    } catch (err) {
        console.error("Fingerprint error:", err);
    }
}