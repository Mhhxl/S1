const readlineSync= require('readline-sync')

const A= parseInt(readlineSync.question("Digite o valor de A: "))
const B= parseInt(readlineSync.question("Digite o valor de B: "))
const C= parseInt(readlineSync.question("Digite o valor de C: "))


const soma = A + B

if (soma < C) {
    console.log('A soma A + B é menor que C')
} else {
    console.log('A soma A + B é maior que C')
    
}
