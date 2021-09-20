const fs = require('fs');
const { hrtime } = require('process');

function main() {
    const start = hrtime.bigint();
    for (let i = 0; i < 1000000; i++) {
    }
    const end = hrtime.bigint();
    const number = Number(end - start);
	const elapsed = number / 1000000;
    console.log(`Took: ${elapsed} milliseconds.`);

    fs.appendFileSync('output.txt', `${elapsed}\n`);
}

main()