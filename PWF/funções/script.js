function adicionarZeros() {
    var numero = document.getElementById("numero").value;
    var resultado = numero.padStart(numero.length + 5, '0');
    document.getElementById("resultadoZeros").innerHTML = "Número com zeros à esquerda: " + resultado;
}

function operacoes() {
    var num1 = parseFloat(document.getElementById("num1").value);
    var num2 = parseFloat(document.getElementById("num2").value);
    
    var soma = num1 + num2;
    var subtracao = num1 - num2;
    var multiplicacao = num1 * num2;
    var divisao = num1 / num2;

    var resultado = `
        Soma: ${soma}<br>
        Subtração: ${subtracao}<br>
        Multiplicação: ${multiplicacao}<br>
        Divisão: ${divisao}
    `;
    
    document.getElementById("resultadoOperacoes").innerHTML = resultado;
}

function converterTemperatura() {
    var celsius = parseFloat(document.getElementById("celsius").value);
    var fahrenheit = (celsius * 9/5) + 32;
    document.getElementById("resultadoTemperatura").innerHTML = `${celsius}°C é igual a ${fahrenheit.toFixed(2)}°F`;
}

function exibirData() {
    var hoje = new Date();
    var dia = hoje.getDate().toString().padStart(2, '0'); 
    var mes = (hoje.getMonth() + 1).toString().padStart(2, '0'); 
    var ano = hoje.getFullYear();
    
    var dataFormatada = dia + '/' + mes + '/' + ano;
    document.getElementById("resultadoData").innerHTML = "Data Atual: " + dataFormatada;
}

function copiarTexto() {
    var texto = document.getElementById("caixa1").value;
    document.getElementById("caixa2").value = texto;
}
