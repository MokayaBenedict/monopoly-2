const board = [
    {"square": 39, "name": "GO", "type": "special"},
    {"square": 1, "name": "Mediterranean Avenue", "type": "property", "price": 60, "rent": [2, 10, 30, 90, 160, 250]},
    {"square": 2, "name": "Community Chest", "type": "community_chest"},
    {"square": 3, "name": "Baltic Avenue", "type": "property", "price": 60, "rent": [4, 20, 60, 180, 320, 450]},
    {"square": 4, "name": "Income Tax", "type": "special"},
    {"square": 5, "name": "Reading Railroad", "type": "property", "price": 200, "rent": [25, 50, 100, 200]},
    {"square": 6, "name": "Oriental Avenue", "type": "property", "price": 100, "rent": [6, 30, 90, 270, 400, 550]},
    {"square": 7, "name": "Chance", "type": "chance"},
    {"square": 8, "name": "Vermont Avenue", "type": "property", "price": 100, "rent": [6, 30, 90, 270, 400, 550]},
    {"square": 9, "name": "Connecticut Avenue", "type": "property", "price": 120, "rent": [8, 40, 100, 300, 450, 600]},
    {"square": 10, "name": "Jail", "type": "special"},
    {"square": 11, "name": "St. Charles Place", "type": "property", "price": 140, "rent": [10, 50, 150, 450, 625, 750]},
    {"square": 12, "name": "Electric Company", "type": "property", "price": 150, "rent": [4, 10]},
    {"square": 13, "name": "Virginia Avenue", "type": "property", "price": 160, "rent": [12, 60, 180, 500, 700, 900]},
    {"square": 14, "name": "Pennsylvania Railroad", "type": "property", "price": 200, "rent": [25, 50, 100, 200]},
    {"square": 15, "name": "St. James Place", "type": "property", "price": 180, "rent": [14, 70, 200, 550, 750, 950]},
    {"square": 16, "name": "Community Chest", "type": "community_chest"},
    {"square": 17, "name": "Tennessee Avenue", "type": "property", "price": 180, "rent": [14, 70, 200, 550, 750, 950]},
    {"square": 18, "name": "New York Avenue", "type": "property", "price": 200, "rent": [16, 80, 220, 600, 800, 1000]},
    {"square": 19, "name": "Free Parking", "type": "special"},
    {"square": 20, "name": "Kentucky Avenue", "type": "property", "price": 220, "rent": [18, 90, 250, 700, 875, 1050]},
    {"square": 21, "name": "Chance", "type": "chance"},
    {"square": 22, "name": "Indiana Avenue", "type": "property", "price": 220, "rent": [18, 90, 250, 700, 875, 1050]},
    {"square": 23, "name": "Illinois Avenue", "type": "property", "price": 240, "rent": [20, 100, 300, 750, 925, 1100]},
    {"square": 24, "name": "B&O Railroad", "type": "property", "price": 200, "rent": [25, 50, 100, 200]},
    {"square": 25, "name": "Atlantic Avenue", "type": "property", "price": 260, "rent": [22, 110, 330, 800, 975, 1150]},
    {"square": 26, "name": "Ventnor Avenue", "type": "property", "price": 260, "rent": [22, 110, 330, 800, 975, 1150]},
    {"square": 27, "name": "Water Works", "type": "property", "price": 150, "rent": [4, 10]},
    {"square": 28, "name": "Marvin Gardens", "type": "property", "price": 280, "rent": [24, 120, 360, 850, 1025, 1200]},
    {"square": 29, "name": "Go to Jail", "type": "special"},
    {"square": 30, "name": "Pacific Avenue", "type": "property", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275]},
    {"square": 31, "name": "North Carolina Avenue", "type": "property", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275]},
    {"square": 32, "name": "Community Chest", "type": "community_chest"},
    {"square": 33, "name": "Pennsylvania Avenue", "type": "property", "price": 320, "rent": [28, 150, 450, 1000, 1200, 1400]},
    {"square": 34, "name": "Short Line Railroad", "type": "property", "price": 200, "rent": [25, 50, 100, 200]},
    {"square": 35, "name": "Chance", "type": "chance"},
    {"square": 36, "name": "Park Place", "type": "property", "price": 350, "rent": [35, 175, 500, 1100, 1300, 1500]},
    {"square": 37, "name": "Luxury Tax", "type": "special"},
  
    
    {"square": 38, "name": "Boardwalk", "type": "property", "price": 400, "rent": [50, 200, 600, 1400, 1700, 2000]}
    
];

const boardElement = document.querySelector('.board');

const layout = [
    10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0,    // Bottom row (GO to Jail)
    11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 38,  // Left and right columns
    12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 
    13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 
    14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 
    15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 
    16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 
    17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 
    18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, // Top row (Free Parking to Go to Jail)
];

layout.forEach((squareIndex, idx) => {
    const cell = document.createElement('div');
    if (squareIndex === 0) {
        cell.className = 'cell empty';
    } else {
        const square = board[squareIndex];
        cell.className = 'cell';
        cell.innerHTML = `<div class="cell-name">${square.name}</div>`;
    }
    boardElement.appendChild(cell);
});

// let currentPosition = 0;

// function movePlayer(steps) {
//     currentPosition = (currentPosition + steps) % 40;
//     const cell = boardElement.children[currentPosition];
//     const cellRect = cell.getBoundingClientRect();
//     const boardRect = boardElement.getBoundingClientRect();

//     const playerToken = document.getElementById('player-token');
//     playerToken.style.left = `${cellRect.left - boardRect.left + cellRect.width / 2 - playerToken.offsetWidth / 2}px`;
//     playerToken.style.top = `${cellRect.top - boardRect.top + cellRect.height / 2 - playerToken.offsetHeight / 2}px`;
// }