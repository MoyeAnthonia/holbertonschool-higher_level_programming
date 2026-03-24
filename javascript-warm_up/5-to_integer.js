#!/usr/bin/node
const firstArg = process.argv[2];
const result = parseInt(firstArg)
if (isNaN(result))
    {
        console.log('Not a number');
    }
    else {
        console.log(`My number: ${result}`);
    }
