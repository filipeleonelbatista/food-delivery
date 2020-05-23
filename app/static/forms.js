window.onload=function(){

    $("#valorentregue").keydown(function(){
        try {
            $("#valorentregue").unmask();
        } catch (e) {}
        
        var tamanho = $("#valorentregue").val().length;
        
        if(tamanho <= tamanho+1){
            $('#valorentregue').mask('000.000.000.000.000,00', {reverse: true});
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#precoVenda").keydown(function(){
        try {
            $("#precoVenda").unmask();
        } catch (e) {}
        
        var tamanho = $("#precoVenda").val().length;
        
        if(tamanho <= tamanho+1){
            $('#precoVenda').mask('000.000.000.000.000,00', {reverse: true});
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#frete").keydown(function(){
        try {
            $("#frete").unmask();
        } catch (e) {}
        
        var tamanho = $("#frete").val().length;
        
        if(tamanho <= tamanho+1){
            $('#frete').mask('000.000.000.000.000,00', {reverse: true});
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });
   
    $("#CPF").keydown(function(){
        try {
            $("#CPF").unmask();
        } catch (e) {}
        
        var tamanho = $("#CPF").val().length;

        if(tamanho < 11){
            $("#CPF").mask("999.999.999-99");
        } else {
            $("#CPF").mask("99.999.999/9999-99");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#cpf").keydown(function(){
        try {
            $("#cpf").unmask();
        } catch (e) {}
        
        var tamanho = $("#cpf").val().length;
        
        if(tamanho <= 11){
            $("#cpf").mask("999.999.999-99");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#CNPJ").keydown(function(){
        try {
            $("#CNPJ").unmask();
        } catch (e) {}
        
        var tamanho = $("#CNPJ").val().length;
        
        if(tamanho < 11){
            $("#CNPJ").mask("999.999.999-99");
        } else {
            $("#CNPJ").mask("99.999.999/9999-99");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#RegGer").keydown(function(){
        try {
            $("#RegGer").unmask();
        } catch (e) {}
        
        var tamanho = $("#RegGer").val().length;
        
        if(tamanho <= 9){
            $("#RegGer").mask("99.999.999-9");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#limiteCredito").keydown(function(){
        try {
            $("#limiteCredito").unmask();
        } catch (e) {}
        
        var tamanho = $("#limiteCredito").val().length;
        
        if(tamanho <= tamanho+1){
            $('#limiteCredito').mask('000.000.000.000.000,00', {reverse: true});
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#rendaMensal").keydown(function(){
        try {
            $("#rendaMensal").unmask();
        } catch (e) {}
        
        var tamanho = $("#rendaMensal").val().length;
        
        if(tamanho <= tamanho+1){
            $('#rendaMensal').mask('000.000.000.000.000,00', {reverse: true});
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#salarioBruto").keydown(function(){
        try {
            $("#salarioBruto").unmask();
        } catch (e) {}
        
        var tamanho = $("#salarioBruto").val().length;
        
        if(tamanho <= tamanho+1){
            $('#salarioBruto').mask('000.000.000.000.000,00', {reverse: true});
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#dataNascimento").keydown(function(){
        try {
            $("#dataNascimento").unmask();
        } catch (e) {}
        
        var tamanho = $("#dataNascimento").val().length;
        
        if(tamanho <= tamanho+1){
            $('#dataNascimento').mask("00/00/0000");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#CEP").keydown(function(){
        try {
            $("#CEP").unmask();
        } catch (e) {}
        
        var tamanho = $("#CEP").val().length;
        
        if(tamanho <= tamanho+1){
            $('#CEP').mask("00000-000");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#telefoneTrabalho").keydown(function(){
        try {
            $("#telefoneTrabalho").unmask();
        } catch (e) {}
        
        var tamanho = $("#telefoneTrabalho").val().length;
        
        if(tamanho <= tamanho+1){
            $('#telefoneTrabalho').mask("(00)0000-0000");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#telefone").keydown(function(){
        try {
            $("#telefone").unmask();
        } catch (e) {}
        
        var tamanho = $("#telefone").val().length;
        
        if(tamanho <= tamanho+1){
            $('#telefone').mask("(00)0000-0000");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#celular").keydown(function(){
        try {
            $("#celular").unmask();
        } catch (e) {}
        
        var tamanho = $("#celular").val().length;
        
        if(tamanho <= tamanho+1){
            $('#celular').mask("(00)00000-0000");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#whatsapp").keydown(function(){
        try {
            $("#whatsapp").unmask();
        } catch (e) {}
        
        var tamanho = $("#whatsapp").val().length;
        
        if(tamanho <= tamanho+1){
            $('#whatsapp').mask("(00)00000-0000");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });
    
    verificaSmart(); 
}