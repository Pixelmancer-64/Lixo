const fs = require("fs").promises;
const nodemailer = require("nodemailer");

async function readDirectories() {
  try {
    const relatoriosPath =
      "/home/hugo/Downloads/Physical Test 8.0/Relatorios Exportados/";

    const dirs = await fs.readdir(relatoriosPath);

    const people = dirs.map((dir) => dir.split("-")[1]);

    process.stdout.write(
      `Selecione uma pessoa: \n${people
        .map((person, index) => `[${index + 1}] ${person}`)
        .join("\n")}\n`
    );

    const personIndex = parseInt(await askQuestion()) - 1;
    const person = dirs[personIndex];

    const pdfPath = `${relatoriosPath}${person}/FormatoPDF/`;
    const dates = await fs.readdir(pdfPath);

    process.stdout.write(
      `\nSelecione uma data: \n ${dates.map(
        (date, index) => `[${index + 1}] ${date} \n`
      )}`
    );

    const dateIndex = parseInt(await askQuestion()) - 1;
    const folder = dates[dateIndex];

    const pdfFiles = await fs.readdir(`${pdfPath}/${folder}`);

    process.stdout.write(
      `\nSelecione o arquivo que deseja enviar: \n${pdfFiles
        .map((file, index) => `[${index + 1}] ${file}`)
        .join("\n")}\n`
    );
    const pdfIndex = parseInt(await askQuestion()) - 1;
    const file = pdfFiles[pdfIndex];

    process.exit(0);
  } catch (error) {
    console.error(error);
  }
}

function askQuestion() {
  return new Promise((resolve) => {
    process.stdin.once("data", (data) => {
      resolve(data.toString().trim());
    });
  });
}

readDirectories();
