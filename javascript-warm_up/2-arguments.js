// function addNo() {
//   return "No argument";
// }
// function addOne(a) {
//   return "Argument found";
// }
// function addTwo(a, b) {
//   return "Arguments found";
// }
// console.log(addNo());
// console.log(addOne("Best"));
// console.log(addTwo("Best", "School"));

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log("No argument");
} else if (args.length === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}