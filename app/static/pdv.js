function enviarAlerta(mensagem,cor){
    document.getElementById('mensagemJs').innerHTML = document.getElementById('mensagemJs').innerHTML = "<div class='alert alert-"+ cor +"'><button type='button' class='close' data-dismiss='alert'>&times;</button>"+ mensagem +"</div>";
}

function limparFormulario(){
    document.getElementById('nomeCliente').innerHTML = '';
    document.getElementById('telefoneCliente').innerHTML = '';
    document.getElementById('enderecoCliente').innerHTML = '';

    document.getElementById('subtotal').innerHTML = 'R$ 00,00';
    document.getElementById('frete').innerHTML = 'R$ 00,00';
    document.getElementById('pagamento').innerHTML = '';
    document.getElementById('Total').innerHTML = 'R$ 00,00';
    document.getElementById('observacao').innerHTML = '';
    document.getElementById('form7').value = '';
    document.getElementById('valorentregue').value = '';


    document.getElementById('diff').setAttribute("style","display:none;");
    document.getElementById('troco').setAttribute("style","display:none;");

    // Captura a referência da tabela com id “minhaTabela”
    var table = document.getElementById("tabelaNota");
    while (table.rows.length > 1){
        table.deleteRow(1);
    }
}
function cancelar(){
    limparFormulario();
    window.open("/pedidos","_self");
}
function pesquisar(valor){
    if (valor!=''){
        valor.toLowerCase().replace(' ','');
        document.getElementById('myTabContent').setAttribute('style', 'display:none');
        document.getElementById('resultSearchTabs').removeAttribute("style");
        allIds = document.getElementById('myTabContent').querySelectorAll('div[id]');
        idsArray = Array.from(allIds);

        // criando array apenas com os id's que tenham a palavra
        resultArray = [];
        for(var i=0; i<idsArray.length; i++){
            strteste = ""+idsArray[i].id;
            compara = strteste.indexOf(valor);
            if(compara != -1){
                resultArray.push(strteste);
            }
        }
        apresenta = [];
        resultapresenta = '';

        //apresentação
        for(var i = 0; i<resultArray.length; i++){
            apresenta = document.getElementById(resultArray[i]);
            resultapresenta += apresenta.outerHTML;
        }
        document.getElementById('apresenta').innerHTML = resultapresenta;

    }else{

        document.getElementById('resultSearchTabs').setAttribute('style', 'display:none');
        document.getElementById('myTabContent').removeAttribute("style");
        document.getElementById('apresenta').innerHTML = "";
    }
}
function enviar(){
    var teste = {
        cliente:[],
        itens:[],
        resumo:[]
    }
     // Captura a referência da tabela com id “minhaTabela”
     var table = document.getElementById("tabelaNota");
     // Captura a quantidade de linhas já existentes na tabela
     var numOfRows = table.rows.length;
     // Captura a quantidade de colunas da última linha da tabela
     var numOfCols = table.rows[numOfRows-1].cells.length;
     // Faz um loop para criar as colunas
     for (var i = 1; i < numOfRows; i++) {
         for (var j = 0; j < numOfCols-1; j++) {
            // confirm("Linha: " + i + " Coluna: " + j + " Conteudo: "+table.rows[i].cells[j].innerHTML);
            if(j==0){
                cod = table.rows[i].cells[j].innerHTML;
            }
            if(j==1){
                qtd = table.rows[i].cells[j].innerHTML;
            }
            if(j==2){
                nomeProd = table.rows[i].cells[j].innerHTML;
            }
            if(j==3){
                preco = table.rows[i].cells[j].innerHTML;
            }
         }
        let item = {
            id_estoque: cod,
            linha: i,
            quantidade: qtd,
            nomeProduto: nomeProd,
            preco: preco.replace('R$ ','').replace(',','.'),
            total: preco.replace('R$ ','').replace(',','.')
        }
        teste.itens.push(item);
        // itens.push(item);
     }
    let cliente = {
        id: document.getElementById('idCliente').innerHTML
    }
    teste.cliente.push(cliente);

    let resumo = {
        subtotal: document.getElementById('subtotal').innerHTML.replace('R$ ','').replace(',','.'),
        frete: document.getElementById('frete').innerHTML.replace('R$ ','').replace(',','.'),
        pagamento: document.getElementById('pagamento').innerHTML,
        troco: document.getElementById('diff').innerHTML.replace('Troco: R$ ','').replace(',','.'),
        total: document.getElementById('Total').innerHTML.replace('R$ ','').replace(',','.'),
        obs: document.getElementById('observacao').innerHTML
    }
    teste.resumo.push(resumo);
    var controle=0;
    //Validações antes do post

    if(teste.cliente[0].id=='vazio'){
        enviarAlerta("Cliente não selecionado","danger");
        controle = 1;
        return false;
    }
    if(teste.itens.length==0){
        enviarAlerta("Pedido vazio","danger");
        controle = 1;
        return false;
    }
    if(teste.resumo[0].subtotal==''){
        enviarAlerta("Pedido vazio","danger");
        controle = 1;
        return false;
    }
    if(teste.resumo[0].frete==''){
        enviarAlerta("Selecione um Cliente","danger");
        controle = 1;
        return false;
    }
    if(teste.resumo[0].pagamento==''){
        enviarAlerta("Metodo de pagamento nao selecionado","danger");
        controle = 1;
        return false;
    }
    if (controle == 3){
        tela = window.open('about:blank');
        tela.document.write(JSON.stringify(teste));
    }
    if (controle==0){
        console.log(JSON.stringify(teste));
        $.ajax({
            method: 'POST',
            url: "/pdvSalvar",
            dataType: 'json',
            data: JSON.stringify(teste),
            success:function(err, req, resp) {
                // console.log(resp);
                if(resp["responseJSON"]["0"]==true){
                    window.location.href = ""+resp["responseJSON"]["1"];
                }else{
                    window.location.href = ""+resp["responseJSON"]["2"];
                }
                // window.location.href = "/results/"+resp["responseJSON"]["uuid"];

            },
        });
    }

}
function atualizaPreco(){
    var soma = 0.00;
    var aux;
    var troco = document.getElementById('valorentregue').value.replace('Troco: R$ ','').replace(',','.');

    // Captura a referência da tabela com id “minhaTabela”
    var table = document.getElementById("tabelaNota");
    // Captura a quantidade de linhas já existentes na tabela
    var numOfRows = table.rows.length;
    // Captura a quantidade de colunas da última linha da tabela
    var numOfCols = table.rows[numOfRows-1].cells.length;

    // Faz um loop para verificar as linhas
    for(var i= 1; i < numOfRows; i++){
        // Faz um loop para verificar as colunas
        for (var j = 0; j < numOfCols; j++) {
            if(j==3){
                aux = parseFloat(table.rows[i].cells[j].innerHTML.replace('R$ ','').replace(',','.')).toFixed(2);
                soma = parseFloat(aux) + soma;
                document.getElementById('subtotal').innerHTML = "R$ " + soma.toFixed(2).replace('.',',');
                frete = parseFloat(document.getElementById('frete').innerHTML.replace('R$ ','').replace(',','.')).toFixed(2);
                total = soma + parseFloat(frete);
                document.getElementById('Total').innerHTML = "R$ " + total.toFixed(2).replace('.',',');
                if(troco!=''){
                    document.getElementById('diff').innerHTML= "Troco: R$ "+ (parseFloat(troco)-parseFloat(total)).toFixed(2).replace('.',',');
                }
            }

        }
    }


}
function observacao(valor){
        document.getElementById('observacao').innerHTML = valor;
}
function deleteRow(i){
    document.getElementById('tabelaNota').deleteRow(i)
    // Captura a referência da tabela com id “minhaTabela”
    var table = document.getElementById("tabelaNota");
    if (table.rows.length == 1){
        document.getElementById('subtotal').innerHTML = 'R$ 00,00';
        document.getElementById('Total').innerHTML =  document.getElementById('frete').innerHTML
    }
    atualizaPreco();
}
function inserirProduto(nome, valor, id) {
    valor = valor.replace(',','.');
    // verificando se o preço é 0
    if ((valor == '0.00')||(valor == '')){
        valor = prompt("Digite o preço do produto selecionado");
        valor = valor.replace('.',',');
    }

    // Captura a referência da tabela com id “minhaTabela”
    var table = document.getElementById("tabelaNota");
    // Captura a quantidade de linhas já existentes na tabela
    var numOfRows = table.rows.length;
    // Captura a quantidade de colunas da última linha da tabela
    var numOfCols = table.rows[numOfRows-1].cells.length;

    // Insere uma linha no fim da tabela.
    var newRow = table.insertRow(numOfRows);

    // Faz um loop para criar as colunas
    for (var j = 0; j < numOfCols; j++) {
        // Insere uma coluna na nova linha
        newCell = newRow.insertCell(j);
        // // Insere um conteúdo na coluna
        // newCell.innerHTML = "Linha "+ numOfRows + " – Coluna "+ j;
        if(j==0){
            newCell.innerHTML = id;
        }
        if(j==1){
            newCell.innerHTML = "1";
        }
        if(j==2){
            newCell.innerHTML = nome;
        }
        if(j==3){
            newCell.innerHTML = "R$ " + parseFloat(valor).toFixed(2).replace('.',',');
        }
        if(j==4){
            newCell.innerHTML = "<button type='button' class='btn btn-sm btn-danger' onclick='deleteRow(this.parentNode.parentNode.rowIndex);'>X</button> ";
        }
        
    }
    atualizaPreco();

}
function inserirPagamento(tipo){
    if(tipo==1){
        document.getElementById('pagamento').innerHTML = " Cartão de Crédito";
        document.getElementById('diff').setAttribute("style","display:none;");
        document.getElementById('troco').setAttribute("style","display:none;");
    }
    if(tipo==2){
        document.getElementById('pagamento').innerHTML = " Cartão de Débito";
        document.getElementById('diff').setAttribute("style","display:none;");
        document.getElementById('troco').setAttribute("style","display:none;");
    }
    if(tipo==3){
        document.getElementById('pagamento').innerHTML = " À Vista";
        document.getElementById('troco').removeAttribute("style");
        document.getElementById('diff').removeAttribute("style");
    }

}
function selecionarCliente(id, nome, telefone, endereco, frete){
    urlEnder = endereco.replace(/,/g,'%2C').replace(/ /g,'+');

    document.getElementById('idCliente').innerHTML = id;

    document.getElementById('nomeCliente').innerHTML = nome;
    document.getElementById('telefoneCliente').innerHTML = telefone;
    document.getElementById('enderecoCliente').innerHTML = "<a target='_blank' href=https://www.google.com/maps/search/?api=1&query=" + urlEnder + ">"+endereco+"</a>";
    // verificando se o frete é 0
    if ((frete == '0,00')||(frete == '')){
        frete = prompt("Digite o preço do frete para este pedido: ");
        frete = frete.replace('.',',');
    }
    frete = parseFloat(frete.replace(',','.')).toFixed(2);
    frete = frete.replace('.',',');
    document.getElementById('frete').innerHTML = "R$ " + frete;
    atualizaPreco();
}
function insereTroco(valor){
    var total = document.getElementById('Total').innerHTML.replace('R$ ','').replace(',','.');
    valor = valor.replace(',','.');
    troco = parseFloat(valor) - parseFloat(total);
    document.getElementById('diff').removeAttribute("style");
    document.getElementById('diff').innerHTML = "Troco: R$ "+ troco.toFixed(2).replace('.',',');
}