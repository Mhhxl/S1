
// solicitar 3 notas e dar a média
const readline = require('readline-sync')

 const ListaDeNotas=[]

for (let i = 1; i <= 3; i++){
    nota = readline.questionFlat(`Digite a 1${i} nota: `)
    listaDeNumeros.push(nota)
}

console.log('\nSoma das notas: ')
soma = listaDeNumeros.reduce ((soma, total) => soma + total, 0)
console.log(soma)

console.log('\nQuantidade de notas: ')
quantidadeNotas=ListaDeNotas.length
console.log(quantidadeNotas)

console.log('\nMédia: ')
media= soma/ quantidadeNotas
console.log(media)


console.log('exibindo todas as notas: ')
listaDeNumeros.forEach((nota, index) => console.log(`${++index}ª nota:${nota} `))