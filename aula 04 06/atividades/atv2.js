const readline = require('readline-sync')

const listaDeNumeros =[]

for (let i = 1; i <= 6; i++){
    Num = readline.questionFloat(`Digite o ${i}º número `)
    listaDeNumeros.push(Num)
}

console.log('Filtrando elementos pares: ')
const pares = listaDeNumeros.filter(n => n % 2 ===0)
console.log(pares)



console.log('Filtrando elementos impares: ')
const impares = listaDeNumeros.filter(n => n % 2 ===1)
console.log(impares)
