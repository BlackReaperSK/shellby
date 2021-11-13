const Discord = require("discord.js");
const client = new Discord.Client();
const { exec } = require("child_process");

// RUN
client.login("YOUR_TOKEN");

// Seu prefixo 
const prefixo = "$";

client.on("message", function(message) {

    // Indentifica se o autor da mensagem é um bot, se for, não processar.
    if (message.author.bot) return;

    // Verifica se a menssagem começa com o prefixo setado acima.
    if (!message.content.startsWith(prefixo)) return;

    // Identando o input
    const input = message.content.slice(prefixo.length);
    // ocorrendo aqui: *$*shell ls -a -> input = shell ls -a

    const args = input.split(' ');
    // ocorrendo aqui: args = ['shell', 'ls', '-a']

    const comando = args.shift().toLowerCase();
    // ocorendo aqui: [*'shell'*, 'ls', '-a'] args = ['ls', '-a'] comando = ['shell']

  if (comando == "shell"){

    var cmd = args.toString().replace(',', ' ');
    // ocorrendo aqui: args = 'ls,-a' -> "ls -a" _> cmd

    //Exec
    exec(cmd, (erro, output) => {
        if (erro) {
            message.reply(`Erro: ${error.message}`);
            return;
        }
        message.reply("\n```css\n" + output + "```");
    });
  }
});
