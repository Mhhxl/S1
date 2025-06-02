const readlineSync= require('readline-sync')

// criando função que irá receber valor inteiro
function identificar_valor(valor) {
    if (valor < 0) {
        console.log('O número é negativo')

    } else {
        console.log('O numero é positivo')
    }
    return valor
}

valor=parseInt(readlineSync.question("Digite um valor:  "))
resultado=identificar_valor(valor)