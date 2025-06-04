const readline = require('readline-sync')

// criando vetor
listaDeNumeros= []



for (i = 1;  i <= 5; i++){
    Num = readline.questionFloat(`Digite o ${i}º número:  `)
    listaDeNumeros.push(Num)
}



console.log('\nFiltrando números negativos:')
const negativos = listaDeNumeros.filter(n => n < 0)
console.log(negativos)





console.log('\nSomando todos os numeros da lista: ')
const soma = listaDeNumeros.reduce ((soma, total) => soma + total, 0)
console.log(soma)


