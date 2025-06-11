const readline=require('readline-sync')

//pedindo ao usuario pra digitar um numero
num=parseInt(readline.question("Digite um número para começar a contagem regressiva: "))

for (let i= num; i<= -1; i--){
    console.log(i)
    
}
