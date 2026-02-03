def palavras_indesejadas():
    stopwords = {
        # --- SEUS TERMOS ESPECÍFICOS SOLICITADOS AGORA ---
        'quarta', 'sente', 'presa', 'aeroporto', 'campinas', 'sabia',
        
        # Extensões lógicas do que você pediu:
        'segunda', 'terca', 'terça', 'quinta', 'sexta', 'sabado', 'domingo', # Outros dias
        'sentir', 'sentiu', 'sabe', 'sabendo', 'preso', 'travada', # Variações de sente/presa
        'guarulhos', 'congonhas', 'viracopos', 'sao', 'paulo', 'rio', 'janeiro', # Outros locais comuns

        # --- LISTA ORIGINAL E TÉCNICA (MANTIDA) ---
        'stellantis', 'não', 'nao', 'mais', 'sim', 'muito', 'normalmente', 'maria', 'fernandes', 'alguma', 'ferreira', 'ctt', 'mgs', 'x', 'xx', 'xxx', '(x)', '(xx)', '(xxx)', 'ñ',
        'bruno', 'ir', 'malas', 'compass', 'jeep', 'fiat', 'citroen', 'peugeot', 'ram', 'coisa', 'saber', 'ate', 'amanda', 'cl', 'fagundes', 'diz', 'sempre', 'número', 'mao', 'parece',
        'às', 'desse', 'dessa', 'dele', 'dela', 'disponível', 'primeiro', 'verificação', 'titano', 'fastback', 'partidamensagem', 'strada', 'toro', 'contacto', 'seguir', 'cc',
        'real', 'disponivel', 'enviar', 'lara', 'motta', 'indisponivel', 'remover', 'necessario', 'retirada', 'fraco', 'la', 'notificando', 'reclame', 'colidiu', 'pais', 'garantia',
        'rampage', 'cynthia', 'loja', '10', 'havia', 'fecha', 'id', 'karina', 'manifesto', 'simbolo', 'defeito', 'renegade', 'un', 'recall', 'wpp', 'repare', 'rt', 'cscrayssa',
        'houve', 'recorrente', 'aqui', 'fazer', 'saida', 'defeito', 'residência', 'onde', 'todos', 'nenhum', 'trabalho', 'pela', 'entrou', 'uso', 'ela', 'novamente', 'dizendo', 'perda',
        'os', 'moto', 'retorno', 'manutenção', 'manhã', 'continua', 'caso', 'residencia', 'rodar', 'momento', 'outro', 'liguei', 'localiza', 'disso', 'silva', 'josé', 'commander', 'final',
        'gentileza', 'rebel', 'planta', 'agora', 'procon', 'dva', 'agora', 'verificar', 'depois', 'longitude', 'pouso', 'respuesta', 'funcionanada', 'atendimentos', 'europamotors', 'verifcar',
        'laramie', 'kênia', 'andré', 'día', 'confiat', 'partidabateria', 'amarelos', 'vermelhos', 'caio', 'ss', 'pulse', 'fin', 'forças', 'cadeado', 'pressa', 'del', 'amazonas', 'quebra', 'n',
        'nota', 'tratamento', 'vocês', 'segue', 'imediato', 'prezados', 'acordo', 'privilege', 'reparado', 'breve', 'própria', 'fazem',

        # --- NOVAS ADIÇÕES (Conectivos e Gramática) ---
        'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
        'de', 'do', 'da', 'dos', 'das', 'em', 'no', 'na', 'nos', 'nas',
        'por', 'pelo', 'pela', 'pelos', 'pelas', 'para', 'pra', 'pro',
        'com', 'sem', 'sob', 'sobre', 'ante', 'até', 'ao', 'aos',
        'eu', 'tu', 'ele', 'nós', 'vós', 'eles', 'me', 'mim', 'comigo', 'te', 'ti', 'contigo',
        'meu', 'minha', 'seu', 'sua', 'nosso', 'nossa', 'qual', 'quem', 'que', 'cujo',
        'e', 'mas', 'porem', 'todavia', 'contudo', 'ou', 'pois', 'porque', 'pq', 'está', 'esta',
        'foi', 'ser', 'era', 'vai', 'ter', 'tinha', 'estar', 'são', 'sao',

        # --- TERMOS DE ATENDIMENTO (Não são peças/defeitos) ---
        'cliente', 'informa', 'relata', 'reclama', 'solicita', 'contato', 'atendimento',
        'agendamento', 'agendar', 'horario', 'data', 'dia', 'hoje', 'ontem', 'amanha',
        'protocolo', 'ligacao', 'telefone', 'celular', 'email', 'mensagem', 'msg',
        'concessionaria', 'css', 'oficina', 'loja', 'consultor', 'tecnico', 'gerente',
        'analise', 'diagnostico', 'orcamento', 'ordem', 'servico', 'os', 'check',
        'aguarda', 'aguardando', 'pendente', 'andamento', 'status', 'posicao',
        'favor', 'grato', 'obrigado', 'att', 'atenciosamente', 'sr', 'sra', 'dr', 'dra',
        'informacao', 'duvida', 'questiona', 'questionamento', 'pediu', 'falar',
        'veiculo', 'carro', 'automovel', 'unidade', 'modelo', 'chassi', 'placa', 'km',
        'vcl', 'clt', 'csa', 'ce',
        
        # --- RUÍDOS TÉCNICOS VISUALIZADOS NO SEU EXCEL ---
        'diag', 'mec', 'complexa', 'execuc', 'roadside', 'assistance', 'case', 'care',
        'customer', 'solved', 'closed', 'brazil', 'complaint', 'towing', 'damaged',
        'kind', 'similar', 'telephone', 'sales', 'after', 'técnico', 'cor',

        # --- VERBOS GENÉRICOS ---
        'realizado', 'realizar', 'feito', 'efetuado', 'trocado', 'substituido',
        'apresentar', 'apresentou', 'constatado', 'verificado', 'testado', 'testes',
        'deixar', 'entregar', 'entregue', 'buscar', 'retirar', 'levar', 'chegar',
        'funcionar', 'funcionando', 'andar', 'parar', 'ligar', 'desligar',
        'fui', 'fomos', 'disse', 'falou', 'perguntou', 'cheguei', 'colocar',
        'solicitamos', 'substituição',
        
        # --- ADJETIVOS VAGOS ---
        'bom', 'ruim', 'novo', 'velho', 'usado', 'mesmo', 'outro', 'outros',
        'grande', 'pequeno', 'alto', 'baixo', 'frente', 'tras', 'lado',
        'bem', 'mal', 'pouco', 'bastante', 'apenas', 'somente', 'quase', 'logo',
        'desta',
    }
    return stopwords