document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded!");  // Debugging

    const map = L.map('map').setView([20, 78], 5);  // Centering on India

    // Debug: Ensure map is initialized
    console.log("Initializing Leaflet map...");

    // Load OpenStreetMap Tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    console.log("Map Initialized!");

    // Fetch locations from API
    fetch('/api/locations/')
        .then(response => response.json())
        .then(data => {
            console.log("Location Data Received:", data);

            if (!data.features || data.features.length === 0) {
                console.warn("No locations found in API response!");
                return;
            }

            data.features.forEach(feature => {
                console.log("Processing location:", feature.properties.name);
                L.marker(feature.geometry.coordinates.reverse())  
                    .addTo(map)
                    .bindPopup(`<b>${feature.properties.name}</b><br>Category: ${feature.properties.category}`);
            });
        })
        .catch(error => console.error("Error fetching locations:", error));
});
 