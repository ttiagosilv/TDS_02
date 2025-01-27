const moedaBaseInput = document.getElementById('moedaBase');
const moedaConversaoInput = document.getElementById('moedaConversao');
const resultado = document.getElementById('resultado');
const botaoConsultar = document.getElementById('botaoConsultar');
const botaoLimpar = document.getElementById('botaoLimpar');
const botaoInverter = document.getElementById('botaoInverter');

botaoConsultar.addEventListener('click', consultarPreco);
botaoLimpar.addEventListener('click', limparCampos);
botaoInverter.addEventListener('click', inverterMoedas);

function limparCampos() {
    moedaBaseInput.value = '';
    moedaConversaoInput.value = '';
    resultado.innerHTML = '';
}

function inverterMoedas() {
    const temp = moedaBaseInput.value;
    moedaBaseInput.value = moedaConversaoInput.value;
    moedaConversaoInput.value = temp;
}

async function consultarPreco() {
    if (!moedaBaseInput || !moedaConversaoInput || !resultado) return;

    if (!moedaBaseInput.value || !moedaConversaoInput.value) {
        resultado.innerHTML = 'Erro: Por favor, preencha ambos os campos de moeda.';
        return;
    }

    const moedaBase = moedaBaseInput.value.toUpperCase().trim();
    const moedaConversao = moedaConversaoInput.value.toUpperCase().trim();
    
    const url = `https://api.binance.com/api/v3/ticker/price?symbol=${moedaBase}${moedaConversao}`;
    
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Par de moedas não encontrado ou indisponível');
        }
        const json = await response.json();
        const preco = parseFloat(json.price);
        let precoFormatado;
        
        if (preco < 0.000001) {
            precoFormatado = preco.toFixed(12);
        } else if (preco < 0.01) {
            precoFormatado = preco.toFixed(8);
        } else if (preco < 1) {
            precoFormatado = preco.toFixed(6);
        } else {
            precoFormatado = preco.toFixed(2);
        }
        
        resultado.innerHTML = `
            <p><strong>Par de Moedas:</strong> ${moedaBase}/${moedaConversao}</p>
            <p><strong>1 ${moedaBase} =</strong> ${precoFormatado} ${moedaConversao}</p>
        `;
    } catch (error) {
        resultado.innerHTML = `Erro: Par de moedas ${moedaBase}/${moedaConversao} não encontrado ou indisponível`;
    }
}