## Funcionalidades

### Gerenciamento de torneios:
/create-tour <name>: cria um torneio
/add-desc <text>: adiciona descrição do torneio (sobrescreve caso já tenha)
/add-rules <text>: adiciona as regras do torneio (sobrescreve caso já tenha)

/registration <id-tour>: abre as inscrições
/register: registra o participante no torneio

/checkin-open <id-tour>: inicia o check-in (se tiver lista de registro apenas registrados podem entrar)
/checkin-close <id-tour>: finaliza o check-in
/checkin or /check-in: realiza o check-in do participante

/gen-swiss <id><number of rounds>: cria chaves no formato suíço com os participantes que fizeram chack-in (adiciona bye caso seja um número ímpar)
/gen-elimination <id><number of rounds>: cria chaves no formato mata-mata (adiciona bye até a potência de dois mais próxima)

/report <id-match><winner>: reporta o resultado (só os jogadores da partida e o administrador podem alterar isso)

/show-tour: mostra os torneios em aberto
/last-champion: mostra o último campeão
/champions: mostra todos os campeões

/nick <username>: mostra o nickname do ptcgo do user marcado
/set-nick <nickname>: seta o próprio nickname

/wooper: send a wooper image
