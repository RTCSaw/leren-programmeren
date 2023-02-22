let size = prompt("Voer een getal in:");

// input
size = parseInt(size);

//bovenste helft
for (let i = 1; i <= size; i++) {
  let row = "";
  for (let j = 1; j <= size - i; j++) {
    row += " ";
  }
  for (let k = 1; k <= 2 * i - 1; k++) {
    row += i;
  }
  console.log(row);
}

// onderste helft
for (let i = size - 1; i >= 1; i--) {
  let row = "";
  for (let j = 1; j <= size - i; j++) {
    row += " ";
  }
  for (let k = 1; k <= 2 * i - 1; k++) {
    row += i;
  }
console.log(row);
}
