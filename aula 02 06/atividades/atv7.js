const readlineSync= require('readline-sync')

//criando função que irá receber 2 números e a média deles
function media(a,b) {
    return a + b / 2
}
nota1= parseFloat(readlineSync.question("Digite a primeira nota: "))
nota2= parseFloat(readlineSync.question("Digite a segunda nota: "))

media = (nota1, nota2)
console.log(`A média é = ${media}`)