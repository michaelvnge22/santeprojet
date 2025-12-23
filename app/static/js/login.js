document.getElementById("login-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    
    try {
        const response = await fetch("/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({ email, password })
        });
        
        if (response.redirected) {
            window.location.href = response.url;
        } else {
            const data = await response.json();
            if (response.ok) {
                alert("Connexion réussie !");
                window.location.href = "/dashboard";
            } else {
                alert(data.detail || "Erreur de connexion");
                window.location.href = "/login?message=" + encodeURIComponent(data.detail || "Erreur inconnue");
            }
        }
    } catch (error) {
        alert("Erreur lors de la connexion : " + error.message);
        window.location.href = "/login?message=Erreur lors de la connexion";
    }
});