BEGIN TRANSACTION;
INSERT INTO "item" ("id","id_pedido","quantidade","produto","precoUnitario","precoTotal") VALUES (1,1,'1','Hospedagem Site Profissional','15.00','15.00'),
 (2,1,'1','Hospedagem Site Profissional','15.00','15.00'),
 (3,2,'1','Sistema de pedidos interno','80.00','80.00');
INSERT INTO "pedido" ("id","dtCreate","dtUpdate","id_cliente","subtotal","desconto","frete","total","formaPagamento","observacao","id_vendedor","id_status") VALUES (1,'2019-06-06 20:36:25.203451','2019-06-06 21:00:42.113623',1,'30.00','0.00','0.00','30.00','Boleto','Vencimento dia 20 de cada mês.
Criação dia 12/08/2018 renovação no valor de 50 reais 1 ano após com reajuste no preço. 
Valores referentes a hospedagem do site da parkjardinagem e sinapark',2,7),
 (2,'2019-06-12 17:29:12.608103','2019-06-12 17:29:35.047093',1,'80.00','0.00','0.00','80.00','A vista','Serviço ativo nesta data expira em 1 mês',2,6);
INSERT INTO "cliente" ("id","cliente","CPF","dataNascimento","id_endereco","telefone","celular","email","frete","observacoes") VALUES (1,'Valdir Mendes de Oliveira Júnior','032.295.830-00','2019-06-06 00:00:00.000000',5,'(51)9202-7980','(51)99202-7980','valdiremail2015@gmail.com','0,00','');
INSERT INTO "funcionario" ("id","CPF","imagem","is_admin","password_hash","nome","telefone","celular","email","id_endereco","id_view","id_clienteview","id_inicioview") VALUES (1,'111.111.111-11','default-admin.jpg',1,'pbkdf2:sha256:50000$RvmjRcgj$63c27509f2098653fb3639e8e478e49303a2fec07f3c70653625fbe8dd4c86c7','Administrador','(51) 3128-1659','(51) 99290-4780','administrador@leonelinformatica.com.br',1,1,1,1),
 (2,'027.845.250-74','default-user.jpg',1,'pbkdf2:sha256:50000$QZ5NTc4n$2caa4a1ea0757ee18bab39c31ac19e1a486f831eec5bb1a23d525232151e9017','Filipe de Leonel Batista','(51)3128-1659','(51)99290-4780','filipe.x@live.com',2,2,2,2),
 (3,'844.846.910-00','default-user.jpg',1,'pbkdf2:sha256:50000$Ga4HnPAq$bdaa60d57a7b00f59cdf6b7df51a507439f04d30fa8f12db1ba721a26482dba1','Lisandra de Paula Kich Batista','(51)3128-1659','(51)98494-1682','lisandra.depaula@yahoo.com.br',4,3,3,3);
INSERT INTO "estoque" ("id","nomeProduto","descricaoProduto","precoVenda","imagem","id_categoria") VALUES (1,'Hospedagem Site Profissional','Sites onepage para converter em vendas.','15,00','default-produto.png',2),
 (2,'Sistema de pedidos interno','[Mensal] Sistema crm interno com pedidos que podem ser impressos em impressora normal ou termica.','80,00','default-produto.png',2),
 (3,'Sistema Delivery','[MENSAL] Sistema de pedidos internos com acompanhamento e entrega','160,00','default-produto.png',2),
 (4,'E-Commerce ','[MENSAL] Controle de pedidos, Delivery e acompanhamento externo pelo cliente','200,00','default-produto.png',2),
 (5,'Manutenção Mão de obra','Mão de obra','80,00','default-produto.png',1);
INSERT INTO "config" ("id","razaoSocial","nomeFantasia","CNPJ","imprimir","tipoImpressao","ativa","whatsapp","facebook","facebookPgId","twitter","instagram","youtube","linkedin","telefone","descricao","sobre","email","icon","logo","id_endereco") VALUES (1,'FILIPE DE LEONEL BATISTA ME','Leonel Informatica','02.784.525/074',1,1,1,'(51)98644-5578','leonelinformaticars','<SEM INFORMAÇÃO>','','','','','(51)3128-1659','Uma empresa de tecnologia','','filipe.x@live.com','default-favicon.png','default-logo.png',3);
INSERT INTO "inicioview" ("id","cliente","funcionario","pedido","estoque","graficoPedidos") VALUES (1,1,1,1,1,1),
 (2,1,1,1,1,1),
 (3,1,1,1,1,1);
INSERT INTO "view" ("id","CPFView","imagemView","is_adminView","password_hashView","nomeView","telefoneView","celularView","emailView","UFView","municipioView","paisView","CEPView","enderecoView","numeroView","complementoView","bairroView") VALUES (1,1,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1),
 (2,1,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1),
 (3,1,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1);
INSERT INTO "clienteview" ("id","cliente","CPF","dataNascimento","UF","municipio","pais","CEP","endereco","numero","complemento","bairro","telefone","celular","email1","obs") VALUES (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
 (2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
 (3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1);
INSERT INTO "categoria" ("id","categoria") VALUES (1,'Padrão'),
 (2,'Hospedagem'),
 (3,'Serviços');
INSERT INTO "endereco" ("id","uf","municipio","pais","cep","endereco","numero","complemento","bairro") VALUES (1,'RS','Gravataí','Brasil','94170-244','Tv. Itacolomi Dois',343,'<vazio>','Santa Cruz'),
 (2,'RS','GRAVATAÍ','Brasil','94170-244','Travessa Itacolomi Dois',343,'','Santa Cruz'),
 (3,'RS','GRAVATAÍ','Brasil','94170-244','Travessa Itacolomi Dois',343,'','Santa Cruz'),
 (4,'RS','GRAVATAÍ','Brasil','94170-244','Travessa Itacolomi Dois',343,'','Santa Cruz'),
 (5,'RS','GRAVATAÍ','Brasil','94155-050','Rua Cristóvão Colombo',536,'','São Vicente');
INSERT INTO "status" ("id","ordem","nome","cor") VALUES (1,0,'Aguardando Confirmação','warning'),
 (2,1,'Aberto','primary'),
 (3,2,'Em produção','success'),
 (4,3,'Saiu para entrega','warning'),
 (5,4,'Finalizado','success'),
 (6,5,'Serviço ativo','info'),
 (7,6,'Serviço desabilitado','danger');
COMMIT;
