
const readlineSync= require('readline-sync')



let idade= parseInt(readlineSync.question("Digite sua idade: "))


if (idade < 16){
    console.log('Não pode votar')
} else if (idade <= 17) {
    console.log('Voto opicional')

}else if (idade === 18) {
    console.log('Voto obrigatório')

} else if (idade >= 65); {
    console.log('Não é obrigado a votar')

}



//pro código funcionar eu preciso acessar a pasta (cd) e depois abrir o arquivo (node(nome do arquivo))
