window.addEventListener('pywebviewready', function() {
    // This event ensures the Python API is ready before we try to use it
    console.log('Python API is ready');
    initializeApp();
});

function initializeApp() {
    // Any initialization code can go here
    // This runs after the Python API is confirmed ready
}

async function handleClick() {
        // Get data from Python
        const data = await window.pywebview.api.get_list_of_players();
        displayData(data);
}

function displayData(data) {
    const table = document.getElementById('dataTable');
    let html = '';
    
    // Process data in groups of 3
    for (let i = 0; i < data.length; i += 3) {
        html += '<tr>';
        for (let j = 0; j < 3; j++) {
            html += `<td>${data[i][j]}</td>`;
            }
        html += '</tr>';
    }
    
    
    table.innerHTML = html;
}