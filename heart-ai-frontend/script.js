document.getElementById("predictForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const inputs = document.querySelectorAll("input");
    const features = Array.from(inputs).map(i => Number(i.value));

    const response = await fetch("https://heart-attack-predicter.onrender.com", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ features })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        data.heart_attack_risk === 1 ? "⚠️ High Risk" : "✅ Low Risk";
});
