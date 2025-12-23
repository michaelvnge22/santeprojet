document.getElementById("signup-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const user_id = document.getElementById("user_id").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    
    try {
        const response = await fetch("/auth/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({ user_id, email, password })
        });

        if (response.redirected) {
            window.location.href = response.url;
        } else {
            const data = await response.json();
            alert(data.message || "Inscription réussie");
            window.location.href = "/login";
        }
    } catch (error) {
        alert("Erreur lors de l'inscription : " + error.message);
        window.location.href = "/signup?message=Erreur lors de l'inscription";
    }
});