const fs = require("fs");
const path = require("path");

const directoryPath =
  "/home/hugo/dev/stuck_in_the_website/src/content/generative_art";

fs.readdir(directoryPath, function (err, files) {
  if (err) {
    return console.log("Error reading directory: " + err);
  }

  files.forEach(function (file) {
    const filePath = path.join(directoryPath, file);
    fs.readFile(filePath, "utf8", function (err, data) {
      if (err) {
        return console.log("Error reading file: " + err);
      }

      // Alter text based on custom code
      //   console.log(file);

      const name = file
        .replace(".md", "")
        .split("-")
        .map((e) => e.charAt(0).toUpperCase() + e.slice(1))
        .join(" ");

      const alteredText = data.replace(name, `title: ${name}`);

      fs.writeFile(filePath, alteredText, function (err) {
        if (err) {
          return console.log("Error writing file: " + err);
        }
        console.log("File " + file + " was successfully updated.");
      });
    });
  });
});
