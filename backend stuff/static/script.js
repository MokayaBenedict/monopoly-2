
// function rollDice() {
//     const dice1 = document.getElementById("dice1");
//     const dice2 = document.getElementById("dice2");

//     const roll1 = Math.floor(Math.random() * 6) + 1;
//     const roll2 = Math.floor(Math.random() * 6) + 1;

//     dice1.textContent = roll1;
//     dice2.textContent = roll2;
//}
// const button = document.getElementById('thor-button');

// button.addEventListener('click', () => {
//   alert('Thor token has been selected');
// });

// {
// const button = document.getElementById('token-button');

// button.addEventListener('click', () => {
//   alert('Ironman token has been selected');
// })};

const tokenPositions = {
    'IronMan-token': 0,
    'HawkEye-token': 0,
    'Thor-token': 0
};

let selectedToken = 'IronMan-token';

document.getElementById('token-button').addEventListener('click', () => {
    selectedToken = 'IronMan-token';
});

document.getElementById('hawk-button').addEventListener('click', () => {
    selectedToken = 'HawkEye-token';
});

document.getElementById('thor-button').addEventListener('click', () => {
    selectedToken = 'Thor-token';
});

function moveToken(token, newPosition) {
    const tokenElement = document.getElementById(token);
    const newCell = document.getElementById('cell-' + newPosition);
    newCell.appendChild(tokenElement);
}

function rollDice() {
    fetch('/roll_dice', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token: selectedToken })
    })
    .then(response => response.json())
    .then(data => {
        const { position, dice, token } = data;
        alert(token + ' rolled a ' + dice + ' and moved to ' + position);
        moveToken(token, position);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    moveToken('IronMan-token', 0);
    moveToken('HawkEye-token', 0);
    moveToken('Thor-token', 0);
});
