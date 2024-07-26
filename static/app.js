document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const query = document.getElementById('query').value;
        
        fetch('/palette', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query }),
        })
        .then(response => response.json())
        .then(data => {
            displayPalette(data.colors);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function displayPalette(colors) {
        const paletteDiv = document.getElementById('palette');
        paletteDiv.innerHTML = ''; // Limpiar contenido anterior

        colors.forEach(color => {
            const colorDiv = document.createElement('div');
            colorDiv.className = 'col-md-4 color';
            colorDiv.style.backgroundColor = color;

            const colorSpan = document.createElement('span');
            colorSpan.textContent = color;

            colorDiv.appendChild(colorSpan);
            paletteDiv.appendChild(colorDiv);
        });
    }
});
