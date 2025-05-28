// criando vetor
const frutas= ['maçã', 'Banana', 'Laranja']
console.log('exibindo resultados....')
console.log(frutas)

console.log('Exibindo apenas um elemento dentro do vetor');
console.log(frutas[0])
console.log(frutas[2])


console.log('Adicionando elemento ao vetor:')
frutas.push('Uvas')
console.log(frutas)

console.log('\nRemovendo o ultimo elemento do vetor')
frutas.pop()
console.log(frutas)


console.log('Removendo o primeiro elemento do vetor.')
frutas.shift()
console.log(frutas)



console.log('Percorrendo o vetor')
frutas.forEach((frutas, index) => (
    console.log(`${++index}: ${frutas}`)
))