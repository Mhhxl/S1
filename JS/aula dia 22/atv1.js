const readlineSync= require('readline-sync')


let numero= parseInt(readlineSync.question("Digite um número pra tabela: "))
console.log(numero)
for (let i =1; i<= 10; i++){
    let resultado= numero * i
    console.log(`${numero} X ${i}= ${resultado}`)

}
