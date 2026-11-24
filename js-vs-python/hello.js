console.log("Hello from JavaScript");

const term = "variable";
console.log(`Today: ${term}`);

let learned = false;
let definition = null;
console.log(learned, definition);

if (learned) {
  console.log("Already learned");
} else {
  console.log("Still learning");
}

if (term === "variable" && !learned) {
  console.log("Time to learn variable");
}

const tags = ["python", "basics"];
tags.push("api");
console.log(tags.length);
console.log(tags.includes("api"));

const note = { term: "variable", definition: "A name that stores a value." };
console.log(note.term);

const notes = [
  {
    id: 1,
    term: "variable",
    definition: "A name that stores a value.",
    js_equivalent: "let / const",
    tags: ["python", "basics"],
    learned: true,
  },
  {
    id: 2,
    term: "list",
    definition: "An ordered collection of values.",
    js_equivalent: "Array",
    tags: ["python", "data"],
    learned: true,
  },
  {
    id: 3,
    term: "dict",
    definition: "Key-value pairs, like a JavaScript object.",
    js_equivalent: "Object",
    tags: ["python", "data"],
    learned: false,
  },
  {
    id: 4,
    term: "function",
    definition: "A reusable block of code defined with def.",
    js_equivalent: "function",
    tags: ["python", "basics"],
    learned: false,
  },
];

for (const note of notes) {
  console.log(note.term);
}

const query = "LI";
for (const note of notes) {
  if (note.term.toLowerCase().includes(query.toLowerCase())) {
    console.log("Found:", note.term);
  }
}

function findTerm(notes, name) {
  for (const note of notes) {
    if (note.term === name) {
      return note;
    }
  }
}

console.log(findTerm(notes, "dict"));
console.log(findTerm(notes, "class"));