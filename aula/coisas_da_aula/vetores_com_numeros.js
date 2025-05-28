//criando uma lista
const numeros= [1,2,3,4,5,6]

console.log('exibindo numeros da lista: ')
console.log(numeros)

console.log('\n multiplicando elementos da lista: ')
const dobrados= numeros.map(n => n * 2)
console.log(dobrados)


console.log('Filtrando numeros pares: ')
const pares = numeros.filter(n => n % 2 === 0 )
console.log(pares)

console.log('Somando todos os numeros do vetor: ')
const total= numeros.reduce((soma,atual) => soma * atual, 0)
console.log(total)
