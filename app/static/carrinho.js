window.onload = function() {
    AtualizaCarrinho();
    montarTabela();
  };

function AddCarrinho(produto, qtd, valor, posicao, lastId, img)
	{   
        if(sessionStorage.length != 0){
            var qtditens = parseInt(sessionStorage.getItem("itens"));
            qtditens++;            
            sessionStorage.setItem("itens", qtditens);

        }else{            
            sessionStorage.setItem("itens", 1);
        }
        sessionStorage.setItem("lastId", lastId);

		sessionStorage.setItem("produto" + posicao, produto);
		sessionStorage.setItem("id" + posicao, posicao);
		sessionStorage.setItem("img" + posicao, img);
		sessionStorage.setItem("qtd" + posicao, qtd);
		valor = valor * qtd;
		sessionStorage.setItem("valor" + posicao, valor);
        document.getElementById('msgSCSuccess'+posicao).innerHTML = "<div class='alert alert-success' role='alert'>Adicionado ao carrinho de compras!</div>";
        document.getElementById('scButton').innerHTML = sessionStorage.getItem("itens");
        document.getElementById('scButton').removeAttribute('style');
    }

function AtualizaCarrinho(){
    if(sessionStorage.length == 0){
        document.getElementById('scButton').setAttribute("style","display:none;");
    }else{
        document.getElementById('scButton').innerHTML = sessionStorage.getItem("itens");
        document.getElementById('scButton').removeAttribute('style');
    }
}
function removerItem(produto, qtd, valor, id, imagem){
    sessionStorage.removeItem(produto);
    sessionStorage.removeItem(qtd);
    sessionStorage.removeItem(valor);
    sessionStorage.removeItem(id);
    sessionStorage.removeItem(imagem);
    var qtditens = parseInt(sessionStorage.getItem("itens"));
    if (qtditens == 1){
        qtditens--;
        sessionStorage.removeItem('itens');
        sessionStorage.removeItem('lastId');
    }else{
        qtditens--;
        sessionStorage.setItem('itens',qtditens);
    }
    AtualizaCarrinho();

}
function VerCarrinho()      
    {
        if(sessionStorage.length == 0){
            document.getElementById('carrinhoLista').innerHTML = "<a class='dropdown-item' href='#'>Carrinho de compras vazio!</a>";
        }else{
            var qtdItens = parseInt(sessionStorage.getItem("itens"));
            var lastId = parseInt(sessionStorage.getItem("lastId"));
            var linha = "";
            var total = 0.0;

            for(var i=0; i<=lastId; i++){
                var prod = sessionStorage.getItem("produto" + i + ""); // verifica se há recheio nesta posição. 
	            if(prod != null) {
                    args = "'produto"+i+"','qtd"+i+"','valor"+i+"','id"+i+"','img"+i+"'";
                    linha += "<div class='dropdown-item'><table><tr><td>"+ sessionStorage.getItem("produto" + i) +"</td><td> <b>Qtd:</b> </td><td>"+ sessionStorage.getItem("qtd" + i) +"</td><td> <b>R$:</b></td><td> "+ parseFloat(sessionStorage.getItem("valor" + i)).toFixed(2).replace(".",",") +"</td><td><button style='margin-left: 10px;' class='btn btn-sm btn-danger' onclick=removerItem("+args+");><i class='fas fa-times' style='color: white;'></i></a></td></table> </div>";
                    valor = parseFloat(sessionStorage.getItem("valor" + i));
                    total = (total + valor);
                }
                
                
            }
            document.getElementById('carrinhoLista').innerHTML = linha + "<a class='dropdown-item' href='#'><b>Total:</b> R$ "+ total.toFixed(2).replace(".",",") +"</a><div class='dropdown-divider'></div><a class='dropdown-item text-center' href='/carrinho'>Ver carrinho de compras</a>";
        }

    }

function montarTabela(){
    if(sessionStorage.length == 0){
        setTimeout(function(){  
            document.getElementById('carregamento').setAttribute("style", "display:none;");
            document.getElementById('carrinho').innerHTML = "Carrinho de compras vazio!";
                    }, 1500);
    }else{
        
        var qtdItens = parseInt(sessionStorage.getItem("itens"));
        var lastId = parseInt(sessionStorage.getItem("lastId"));
        var linha = "";
        var total = 0.0;

        for(var i=0; i<=lastId; i++){
            var prod = sessionStorage.getItem("produto" + i + ""); // verifica se há recheio nesta posição. 
            if(prod != null) {
                args = "'produto"+i+"','qtd"+i+"','valor"+i+"','id"+i+"','img"+i+"','"+i+"'";
                linha += "<tr><td><img src='/static/images/"+ sessionStorage.getItem("img" + i) +"' width='50px'></td><td>"+ sessionStorage.getItem("id" + i) +"</td><td>"+ sessionStorage.getItem("produto" + i) +"</td><td><input type='nummber' class='form-control' size='3' value='"+ sessionStorage.getItem("qtd" + i) +"'></td><td>R$ "+ parseFloat(sessionStorage.getItem("valor" + i)).toFixed(2).replace(".",",") +"</td><td></td><td><button style='margin-left: 10px;' class='btn btn-sm btn-danger' onclick=removerItemTabela("+args+");><i class='fas fa-times' style='color: white;'></i></a></td></tr>";
                valor = parseFloat(sessionStorage.getItem("valor" + i));
                total = (total + valor);
            }
            
            
        }
        document.getElementById('carrinhoCorpo').innerHTML = linha;
        document.getElementById('carrinhoFoot').innerHTML = "<tr><td></td><td></td><td></td><td><b>Total:</b></td><td> R$ "+ total.toFixed(2).replace(".",",") +"</td><td></td><td></td></tr>";

        setTimeout(function(){  
                    document.getElementById('carregamento').setAttribute("style", "display:none;");
                    document.getElementById('carrinho').removeAttribute("style");
                            }, 1500);
    }

}
function removerItemTabela(produto, qtd, valor, id, imagem, i){
    sessionStorage.removeItem(produto);
    sessionStorage.removeItem(qtd);
    sessionStorage.removeItem(valor);
    sessionStorage.removeItem(id);
    sessionStorage.removeItem(imagem);
    var qtditens = parseInt(sessionStorage.getItem("itens"));
    if (qtditens == 1){
        qtditens--;
        sessionStorage.removeItem('itens');
        sessionStorage.removeItem('lastId');
    }else{
        qtditens--;
        sessionStorage.setItem('itens',qtditens);
    }


    document.getElementById('tabelaCarrinho').deleteRow(i)
    // Captura a referência da tabela com id “minhaTabela”
    var table = document.getElementById("tabelaCarrinho");
    if (table.rows.length == 1){
        document.getElementById("tabelaCarrinho").setAttribute("style","display:none;");
    }

    AtualizaCarrinho();

}