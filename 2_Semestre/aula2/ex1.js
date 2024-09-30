
//procura o botão na página
var elementBtn = document.querySelector("button")

//adiciona um ouvinte de eventos
//se ouvir um clock executa uma função
elementBtn.addEventListener('click', function(){
    var campoNome = document.querySelector('input[name="nome"]');
    var campoNota = document.querySelector('input[name="nota"]');

    var tabela = document.querySelector('table');
    var tbody = tabela.querySelector('tbody');

    var linha = tbody.insertRow();
    var celula1 = linha.insertCell();
    var celula2 = linha.insertCell();

    celula1.innerText = campoNome.value;
    celula2.innerText = campoNota.value;
    
    alert(campoNome.value + ' Você tirou a nota ' + campoNota.value);

})

