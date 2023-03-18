const fs = require("fs").promises;
const fs_sync = require("fs");

const nodemailer = require("nodemailer");
require('dotenv').config();

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
    await send_file(`${pdfPath}${folder}/${file}`)

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

async function send_file(file_path){
  const attachment = {
    filename: "report.pdf",
    content: fs_sync.readFileSync(file_path),
  };
  
  // create reusable transporter object using the default SMTP transport
  let transporter = nodemailer.createTransport({
    host: process.env.Host,
    port: process.env.Port,
    secure: false,
    auth: {
      user: process.env.Email,
      pass: process.env.Password,
    },
    tls: {
      ciphers:'SSLv3'
  }
  });
  
  // send mail with defined transport object
  let info = await transporter.sendMail({
    from: process.env.From,
    to: process.env.Email,
    subject: "PDF Report",
    text: "Please find attached the PDF report.",
    attachments: [attachment],
  });
  
  console.log('envido')
}