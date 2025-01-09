// division.js
const args = process.argv.slice(2);
const a = parseFloat(args[0]);
const b = parseFloat(args[1]);

if (b === 0) {
    console.error("Error: Division by zero");
    process.exit(1);
}

console.log(a / b);

