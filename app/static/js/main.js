document.getElementById("login-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    
    try {
        const response = await fetch("http://localhost:8000/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({ email, password })
        });
        
        const data = await response.json();
        if (response.ok) {
            alert("Connexion réussie !");
            // Stocker l'user_id dans le localStorage (ou utiliser un JWT dans une version plus avancée)
            localStorage.setItem("user_id", data.user_id);
            window.location.href = "/dashboard";
        } else {
            alert(data.detail);
        }
    } catch (error) {
        alert("Erreur lors de la connexion : " + error.message);
    }
});