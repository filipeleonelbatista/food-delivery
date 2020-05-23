
    // obtendo cidades dos formularios de endereço
    let state_select = document.getElementById('UF');
    let city_select = document.getElementById('municipio');    
    let natural_select = document.getElementById('naturalidade');

    let cnpj_consulta = document.getElementById('CNPJ');

    cnpj_consulta.onchange = function(){
        consulta = cnpj_consulta.value.replace(/\D/g, '');;
        //Cria um elemento javascript.
        var script = document.createElement('script');

        //Sincroniza com o callback.
        script.src = 'https://www.receitaws.com.br/v1/cnpj/'+ consulta +'?callback=meu_callback_cnpj';

        //Insere script no documento e carrega o conteúdo.
        document.body.appendChild(script);
    }

    state_select.onchange = function(){
        state = state_select.value;
        fetch('/municipios/'+state).then(function(response){
            response.json().then(function(data){
                let optionHTML = "";

                for(let cidade of data.municipios){
                    optionHTML += "<option value='"+cidade.id+"'>"+cidade.name+"</option>";
                }

                city_select.innerHTML = optionHTML;
                natural_select.innerHTML = optionHTML;
            });
        });
    }

 
function limpa_formulário_cep() {
    //Limpa valores do formulário de cep.
    document.getElementById('endereco').value=("");
    document.getElementById('bairro').value=("");
    document.getElementById('municipio').value=("");
    document.getElementById('UF').value=("");
}

function selecionarCidade(estado){
    let city_select = document.getElementById('municipio');    
    let natural_select = document.getElementById('naturalidade');

    state = estado;
    fetch('/municipios/'+state).then(function(response){
        response.json().then(function(data){
            let optionHTML = "";

            for(let cidade of data.municipios){
                optionHTML += "<option value='"+cidade.id+"'>"+cidade.name+"</option>";
            }

            city_select.innerHTML = optionHTML;
            natural_select.innerHTML = optionHTML;
        });
    });
}

function meu_callback(conteudo) {
    if (conteudo.status == "ERROR"){
        alert('CEP inválido!');
    }else{
        if (!("erro" in conteudo)) {
            //Atualiza os campos com os valores.
            document.getElementById('endereco').value=(conteudo.logradouro);
            document.getElementById('bairro').value=(conteudo.bairro);
            document.getElementById('UF').value=(conteudo.uf);  
            selecionarCidade(conteudo.uf);  
            setTimeout(function(){                 
                document.getElementById('municipio').value=(conteudo.localidade.toUpperCase());
                document.getElementById('naturalidade').value=(conteudo.localidade.toUpperCase());
             },
             350);
            
            
        } //end if.
        else {
            //CEP não Encontrado.
            limpa_formulário_cep();
            alert("CEP não encontrado.");
        }
    }
}

function pesquisacep(valor) {

//Nova variável "cep" somente com dígitos.
var cep = valor.replace(/\D/g, '');

//Verifica se campo cep possui valor informado.
if (cep != "") {

    //Expressão regular para validar o CEP.
    var validacep = /^[0-9]{8}$/;

    //Valida o formato do CEP.
    if(validacep.test(cep)) {

        //Preenche os campos com "..." enquanto consulta webservice.
        document.getElementById('endereco').value="...";
        document.getElementById('bairro').value="...";
        document.getElementById('municipio').value="...";
        document.getElementById('UF').value="...";

        //Cria um elemento javascript.
        var script = document.createElement('script');

        //Sincroniza com o callback.
        script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

        //Insere script no documento e carrega o conteúdo.
        document.body.appendChild(script);

    } //end if.
    else {
        //cep é inválido.
        limpa_formulário_cep();
        alert("Formato de CEP inválido.");
    }
} //end if.
else {
    //cep sem valor, limpa formulário.
    limpa_formulário_cep();
}
}

function meu_callback_cnpj(conteudo) {
    if (conteudo.status == "ERROR"){
        alert('CNPJ inválido!');
    }else{
        if (!("erro" in conteudo)) {
            //Atualiza os campos com os valores.
            document.getElementById('cliente').value=(conteudo.nome);
            document.getElementById('nomeFantasia').value=(conteudo.fantasia);            
            document.getElementById('dataNascimento').value=(conteudo.abertura);
            document.getElementById('telefone').value=(conteudo.telefone); 
            document.getElementById('email').value=(conteudo.email); 
            document.getElementById('numero').value=(conteudo.numero);
            document.getElementById('CEP').value=(conteudo.cep); 
            pesquisacep(conteudo.cep); 
            
        } //end if.
        else {
            //CEP não Encontrado.
            limpa_formulário_cep();
            alert("CEP não encontrado.");
        }
    }
    
}