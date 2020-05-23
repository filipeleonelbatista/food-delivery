window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove(); 
    });
}, 4000);


function setFornecedor(id){
        
    document.getElementById('codFornecedor').setAttribute("value", id);

}
// function setCliente(id, nome, cpf, endereco, telefone, celular){
//     document.getElementById('InfosCliente').classList.remove("esconder");
//     document.getElementById('NomeCliente').innerHTML = nome;
//     document.getElementById('CPFCliente').innerHTML = cpf;
//     document.getElementById('EnderecoCliente').innerHTML = endereco;
//     document.getElementById('TelefoneCliente').innerHTML = telefone;    
//     document.getElementById('CelularCliente').innerHTML = celular;
//     document.getElementById('cliente').setAttribute("value", id);
    
//     document.getElementById('InfosCliente').removeAttribute("Style");
    

// }
// function setProduto(nome, qtdAtual, qtdMinima, preco){
//     if((qtdAtual < qtdMinima)&&(qtdAtual != 0)){
//         confirm("Quantidade do produto em nivel baixo");
//     }
//     if( qtdAtual > qtdMinima){
//         confirm("Produto em estoque");
//     }
//     if(qtdAtual == 0){
//         confirm("Produto Fora de estoque");
//     }
//     document.getElementById('produto').value = nome;
//     document.getElementById('precoUnitario').value = preco;
// }
function imprimir(){
    var model = "<html><head><link href='//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' rel='stylesheet'> <link rel='stylesheet' type='text/css' href='/static/styles.css'> <link rel='stylesheet' type='text/css' href='/static/main.css'></head><body>";
    var impressao =  document.getElementById('imprimir').innerHTML;
    var footer = "</body></html>";
    
    var conteudo = model + impressao + footer,
                tela_impressao = window.open('about:blank');

            tela_impressao.document.write(conteudo);
            setTimeout(function(){ 
                tela_impressao.window.print();
                tela_impressao.window.close();
                 }, 1000);          
}
function imprimirEtiqueta(id){
    var conteudo = document.getElementById(id).innerHTML,
                tela_impressao = window.open('about:blank');

            tela_impressao.document.write(conteudo);
            tela_impressao.window.print();
            tela_impressao.window.close();
}
function screenshot(){
    html2canvas(document.querySelector("#card")).then(canvas => {
        // document.body.appendChild(canvas)        
        saveAs(canvas.toDataURL(), 'file-name.png');
    });
    screenshot = document.getElementsByTagName("canvas");
    
}
function saveAs(uri, filename) {

    var link = document.createElement('a');

    if (typeof link.download === 'string') {

        link.href = uri;
        link.download = filename;

        //Firefox requires the link to be in the body
        document.body.appendChild(link);

        //simulate click
        link.click();

        //remove the link when done
        document.body.removeChild(link);

    } else {

        window.open(uri);

    }
}