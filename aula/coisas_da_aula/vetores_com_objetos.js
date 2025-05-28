const usuarios= [
    {nome: 'Ana', idade: 25},
    {nome: 'Marta', idade: 32},
    {nome: 'Maria', idade: 45}
]

console.log("Exibindo todos os elementos do vetor:")
usuarios.forEach(usuarios => (
    console.log(`${usuarios.nome} tem ${usuarios.idade} anos`)
))



console.log('filtrando usuarios.')
console.log('apenas usuarios até 30 anos')
const menorQueTrintaAnos = usuarios.filter(usuarios => usuarios.idade < 30)
menorQueTrintaAnos.forEach(usuarios => console.log(`${usuarios.nome}tem ${usuarios.idade}Anos`))

console.log("\n Exibindo Apenas o nome dos usuarios.")
const nomes= usuarios.map(usuarios => usuarios.nome)
nomes.forEach(nome => (
    console.log(`nome: ${++index}: ${nome}`)
))
