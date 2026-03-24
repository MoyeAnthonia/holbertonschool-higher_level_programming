#!/usr/bin/node
const oneArgs = process.argv.slice(2);
const twoArgs = process.argv.slice(3);
const [firstArg] = oneArgs;
const [secondArg] = twoArgs;

const newString = firstArg.concat(' is ', secondArg);

console.log(newString);