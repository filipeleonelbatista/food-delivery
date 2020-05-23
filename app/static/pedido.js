function enviarAlerta(mensagem,cor){
    document.getElementById('mensagemJs').innerHTML = document.getElementById('mensagemJs').innerHTML = "<div class='alert alert-"+ cor +"'><button type='button' class='close' data-dismiss='alert'>&times;</button>"+ mensagem +"</div>";
}
function editar(){
    var teste = {
        cliente:[],
        itens:[],
        resumo:[]
    }

    var controle=0;
     // Captura a referência da tabela com id “minhaTabela”
     var table = document.getElementById("tabelaPedido");
     if(table==null){
        confirm("Pedido vazio");
        controle = 1;
        return false;
     }else{
        // Captura a quantidade de linhas já existentes na tabela
        var numOfRows = table.rows.length;
        // Captura a quantidade de colunas da última linha da tabela
        var numOfCols = table.rows[numOfRows-1].cells.length;
        // Faz um loop para criar as colunas
        for (var i = 1; i < numOfRows; i++) {
            for (var j = 0; j < numOfCols-1; j++) {
                // confirm("Linha: " + i + " Coluna: " + j + " Conteudo: "+table.rows[i].cells[j].innerHTML);
                if(j==1){
                    qtd = table.rows[i].cells[j].getElementsByTagName('input')[0].value;
                }
                if(j==2){
                    nomeProd = table.rows[i].cells[j].getElementsByTagName('input')[0].value;
                }
                if(j==3){
                    precoUnit = table.rows[i].cells[j].getElementsByTagName('input')[0].value;
                }
                if(j==4){
                    precoTotal = table.rows[i].cells[j].getElementsByTagName('input')[0].value;
                }
            }
            let item = {
                linha: i,
                quantidade: qtd,
                nomeProduto: nomeProd,
                preco: precoUnit.replace(',','.'),
                total: precoTotal.replace('R$ ','').replace(',','.')
            }
            teste.itens.push(item);
            // itens.push(item);
        }
     }

    let cliente = {
        id: document.getElementById('idCliente').innerHTML
    }
    teste.cliente.push(cliente);

    let resumo = {
        subtotal: document.getElementById('subtotal').value.replace('R$ ','').replace(',','.'),
        frete: document.getElementById('frete').value.replace(',','.'),
        desconto: document.getElementById('desconto').value.replace(',','.'),
        pagamento: document.getElementById('formasPagamento').value,
        status: document.getElementById('statusPedido').value,
        total: document.getElementById('Total').value.replace('R$ ','').replace(',','.'),
        obs: document.getElementById('observacao').value
    }
    teste.resumo.push(resumo);
    var controle=0;
    //Validações antes do post

    if(teste.cliente[0].id==''){
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

    let pedidoId = document.getElementById('idPedido').innerHTML;
    if (controle==0){
        // console.log(JSON.stringify(pedido));

        console.log(JSON.stringify(teste));
        // $.post("/pdvSalvar", JSON.stringify(pedido));
        $.ajax({
            method: 'POST',
            url: "/pedidos/editar/"+pedidoId,
            dataType: 'json',
            data: JSON.stringify(teste),
            // data: JSON.stringify(pedido)
            success:function(err, req, resp) {
                if(resp["responseJSON"]["0"]!=true){
                    window.location.href = ""+resp["responseJSON"]["1"];
                }else{
                    window.location.href = ""+resp["responseJSON"]["2"];
                }
                // window.location.href = "/results/"+resp["responseJSON"]["uuid"];
            },
        });
    }
}
function enviar(){
    var teste = {
        cliente:[],
        itens:[],
        resumo:[]
    }

    var controle=0;
     // Captura a referência da tabela com id “minhaTabela”
     var table = document.getElementById("tabelaPedido");
     if(table==null){
        enviarAlerta("Pedido vazio","danger");
        controle = 1;
     }else{
        // Captura a quantidade de linhas já existentes na tabela
        var numOfRows = table.rows.length;
        // Captura a quantidade de colunas da última linha da tabela
        var numOfCols = table.rows[numOfRows-1].cells.length;
        // Faz um loop para criar as colunas
        for (var i = 1; i < numOfRows; i++) {
            for (var j = 0; j < numOfCols-1; j++) {
                // confirm("Linha: " + i + " Coluna: " + j + " Conteudo: "+table.rows[i].cells[j].innerHTML);
                if(j==1){
                    qtd = table.rows[i].cells[j].getElementsByTagName('input')[0].value;
                }
                if(j==2){
                    nomeProd = table.rows[i].cells[j].getElementsByTagName('input')[0].value;
                }
                if(j==3){
                    precoUnit = table.rows[i].cells[j].getElementsByTagName('input')[0].value;
                }
                if(j==4){
                    precoTotal = table.rows[i].cells[j].getElementsByTagName('input')[0].value;
                }
            }
            let item = {
                linha: i,
                quantidade: qtd,
                nomeProduto: nomeProd,
                preco: precoUnit.replace(',','.'),
                total: precoTotal.replace('R$ ','').replace(',','.')
            }
            teste.itens.push(item);
            // itens.push(item);
        }
     }

    let cliente = {
        id: document.getElementById('idCliente').innerHTML
    }
    teste.cliente.push(cliente);

    let resumo = {
        subtotal: document.getElementById('subtotal').value.replace('R$ ','').replace(',','.'),
        frete: document.getElementById('frete').value.replace(',','.'),
        desconto: document.getElementById('desconto').value.replace(',','.'),
        pagamento: document.getElementById('formasPagamento').value,
        total: document.getElementById('Total').value.replace('R$ ','').replace(',','.'),
        obs: document.getElementById('observacao').value
    }
    teste.resumo.push(resumo);
    var controle=0;
    //Validações antes do post

    if(teste.cliente[0].id==''){
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

    if (controle==0){
        console.log(JSON.stringify(teste));
        $.ajax({
            method: 'POST',
            url: "/pedidos/cadastroPedido",
            dataType: 'json',
            data: JSON.stringify(teste),
            success:function(err, req, resp) {
                console.log(resp)
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
function limparFormulario(){

    document.getElementById('InfosCliente').setAttribute("style","display:none;");
    document.getElementById('NomeCliente').innerHTML = '';
    document.getElementById('CPFCliente').innerHTML = '';
    document.getElementById('EnderecoCliente').innerHTML = '';
    document.getElementById('TelefoneCliente').innerHTML = '';
    document.getElementById('CelularCliente').innerHTML = '';
    document.getElementById('idCliente').innerHTML= '';
    document.getElementById('frete').value = "0,00";
    document.getElementById('desconto').value = "0,00";

    document.getElementById('Total').value = "R$ 0,00";
    document.getElementById('subtotal').value = "R$ 0,00";
    document.getElementById('tabelaPedido').setAttribute("style","display:none;");
    // Captura a referência da tabela com id “minhaTabela”
    var table = document.getElementById("tabelaPedido");
    while (table.rows.length > 1){
        table.deleteRow(1);
    }

}
function cancelar(){
    limparFormulario();
    window.open("/pedidos","_self");
}
function atualizaPreco(){
    // Captura a referência da tabela com id “minhaTabela”
    var table = document.getElementById("tabelaPedido");
    // Captura a quantidade de linhas já existentes na tabela
    var numOfRows = table.rows.length;
    // Captura a quantidade de colunas da última linha da tabela
    var numOfCols = table.rows[numOfRows-1].cells.length;
    //Verifica a soma em toda a tabela por linhas
    var soma = 0;
    for(var i = 1; i < numOfRows; i++){
        for(var j = 0; j<numOfCols; j++){
            if(j==1){
               qtd = table.rows[i].cells[j].getElementsByTagName('input')[0].value;
            }
            if(j==3){
                precoUnit = parseFloat(table.rows[i].cells[j].getElementsByTagName('input')[0].value.replace(',','.'));
            }
            if(j==4){
                result = qtd * precoUnit
                table.rows[i].cells[j].getElementsByTagName('input')[0].value = "R$ " + parseFloat(result).toFixed(2).replace('.',',');
            }
        }
        soma = parseFloat(soma) + parseFloat(result);
    }

    document.getElementById('subtotal').value = "R$ " + soma.toFixed(2).replace('.',',');


    subtotal = parseFloat(document.getElementById('subtotal').value.replace('R$ ','').replace(',','.'));
    desconto = parseFloat(document.getElementById('desconto').value.replace(',','.'));
    frete = parseFloat(document.getElementById('frete').value.replace(',','.'));
    total = subtotal + frete - desconto;
    document.getElementById('Total').value = "R$ " + total.toFixed(2).replace('.',',');

}
function deleteRow(i){
    document.getElementById('tabelaPedido').deleteRow(i)
    // Captura a referência da tabela com id “minhaTabela”
    var table = document.getElementById("tabelaPedido");
    if (table.rows.length == 1){
        document.getElementById("tabelaPedido").setAttribute("style","display:none;");
        document.getElementById("resumoPedido").setAttribute("style","display:none;");
    }
    atualizaPreco();
}
function setCliente(id, nome, cpf, endereco, telefone, celular, frete){
    document.getElementById('InfosCliente').removeAttribute("style");
    document.getElementById('resumoPedido').removeAttribute("style");
    document.getElementById('NomeCliente').innerHTML = nome;
    document.getElementById('CPFCliente').innerHTML = cpf;
    var novoEndereco = endereco.replace(/,/g,'%2C').replace(' ','+');
    document.getElementById('EnderecoCliente').innerHTML = "<a target=" + "_blank" + " href='https://www.google.com/maps/search/?api=1&query=" + novoEndereco + "'>" + endereco + "</a>";
    document.getElementById('TelefoneCliente').innerHTML = "<a target=" + "_blank" + " href='tel:" + telefone + "'>" + telefone + "</a>";
    document.getElementById('CelularCliente').innerHTML = "<a target=" + "_blank" + " href='tel:" + celular + "'>" + celular + "</a>";
    document.getElementById('idCliente').innerHTML= id;
    // verificando se o frete é 0
    if ((frete == '0,00')||(frete == '')){
        frete = prompt("Digite o preço do frete para este pedido: ");
        frete = frete.replace('.',',');
    }
    valorFrete = parseFloat(frete.replace(',','.'));
    document.getElementById('frete').value = valorFrete.toFixed(2).replace('.',',');


    atualizaPreco();

}
function setProduto(id, nome, preco){
    document.getElementById("tabelaPedido").removeAttribute("style");
    document.getElementById("resumoPedido").removeAttribute("style");
    // Captura a referência da tabela com id “minhaTabela”
    var table = document.getElementById("tabelaPedido");
    // Captura a quantidade de linhas já existentes na tabela
    var numOfRows = table.rows.length;
    // Captura a quantidade de colunas da última linha da tabela
    var numOfCols = table.rows[numOfRows-1].cells.length;
    // Insere uma linha no fim da tabela.
    var newRow = table.insertRow(numOfRows);

    precoUnitario = parseFloat(preco.replace(',','.')).toFixed(2).replace('.',',');

    // verificando se o preço é 0
    if ((precoUnitario == '0,00')||(precoUnitario == '')){
        precoUnitario = prompt("Digite o preço do produto selecionado");
        precoUnitario = precoUnitario.replace('.',',');
    }

    //Verifica a ultima linha livre e insere o produto nela

        for(var j = 0; j<numOfCols; j++){
            //Insere uma coluna na nova linha
            newCell = newRow.insertCell(j);
            // Insere um conteúdo na coluna
            // newCell.innerHTML = "Linha "+ numOfRows + " – Coluna "+ j;
            if(j==0){
                newCell.innerHTML = "<strong>"+ numOfRows +"</strong>";                
                newCell.setAttribute("style", "vertical-align: middle;");
            }
            if(j==1){
                newCell.innerHTML = "<input inputmode='numeric' onkeyup='atualizaPreco();' type='text' id='qtd' placeholder='Quantidade' class='form-control' value='1'>";                
                newCell.setAttribute("style", "vertical-align: middle;");
                
            }
            if(j==2){
                newCell.innerHTML = "<input readonly='readonly' type='text' id='produto' placeholder='Produto' class='form-control' value='"+ nome +"'>";                
                newCell.setAttribute("style", "vertical-align: middle;");                
            }
            if(j==3){
                newCell.innerHTML ="<input inputmode='numeric' readonly='readonly' value='"+ precoUnitario +"' type='text' placeholder='Valor unitário' id='valorUnitario' class='form-control'>";                
                newCell.setAttribute("style", "vertical-align: middle;");                
            }
            if(j==4){
                newCell.innerHTML = "<input inputmode='numeric' readonly='readonly' value='"+ precoUnitario +"' type='text' id='valorTotal' class='form-control'>";                
                newCell.setAttribute("style", "vertical-align: middle;");                
            }
            if(j==5){
                newCell.innerHTML = "<button type='button' class='btn btn-sm btn-danger' onclick='deleteRow(this.parentNode.parentNode.rowIndex);'><i class='fas fa-trash'></i></button> ";                
                newCell.setAttribute("style", "vertical-align: middle;");                
            }
        }

    if(document.getElementById('frete').value == ''){
        document.getElementById('frete').value = "0,00"
    }
    if(document.getElementById('desconto').value == ''){
        document.getElementById('desconto').value = "0,00"
    }
    atualizaPreco();

}
