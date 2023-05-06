<div id="image03" style="display: inline_block" align="center">
		<img src="assets/logo.png"/>
</div>

<div style="display: inline_block" align="center">
<a href="#en"> English </a> |
<a href="#pt"> Portuguese  </a> 
</div>

<br>

<div id="en">


</div>

<div id="pt">

<h1 align="center"> Sumário 📖 </h1>
<div id="sumario" style="display: inline_block" align="center">
	<a href="#intro"> Introdução  </a> |
	<a href="#conceitos"> Conceitos & Metodologia </a> |
	<a href="#docker"> Docker </a> |
	<a href="#conclusao"> Conclusão </a>
</div>
<br>

<div id="intro">

# Introdução 🎉

Com o crescente aumento do uso de carros elétricos nas cidades, a demanda por postos de recarga tem se tornado uma preocupação para governos e empresas. O gerenciamento de filas em postos de recarga é um problema real, que pode levar a congestionamentos e atrasos, o que pode afetar negativamente a experiência do usuário.

Para resolver essa questão, sua empresa startup foi contratada para desenvolver um sistema inteligente de carregamento de veículos elétricos. A ideia era criar uma aplicação capaz de orientar os motoristas a partir de um certo nível crítico de carga da bateria, distribuindo a demanda entre os pontos de recarga disponíveis e reduzindo o tempo necessário para a recarga dos veículos.

A aplicação desenvolvida pela sua equipe utiliza a linguagem Python e utiliza a comunicação MQTT entre os postos de recarga e nevoas, além de HTTP entre carros e nevoas. O sistema acompanha as filas de espera em cada posto de recarga, identifica os pontos disponíveis e direciona os motoristas para os postos de recarga mais próximos e com menor tempo de espera.

Para garantir o desempenho da aplicação, sua equipe adotou uma infraestrutura distribuída, que permite reduzir os atrasos e o excesso de dados enviados para a nuvem. O resultado é um sistema eficiente, capaz de gerenciar as filas de espera em postos de recarga de forma inteligente e em tempo real, tornando o processo de recarga de carros elétricos mais conveniente para os motoristas e incentivando o uso desses veículos nas cidades.

</div>

<div id="conceitos">

# Conceitos & Metodologia 📚

O sistema foi desenvolvido seguindo uma arquitetura de microsserviços, onde cada componente é responsável por uma funcionalidade específica. A aplicação é dividida em quatro partes principais: o servidor, o GasStation, a Fog e o Car.

O servidor é a peça central do sistema e é responsável por gerenciar as conexões entre os componentes e o fluxo de dados entre eles. Para isso, foi utilizado uma imagem docker que inicializa um broker Mosquitto para comunicação MQTT.

O GasStation representa os postos de recarga de carros elétricos. Cada posto envia informações sobre a fila de recarregamento para o broker MQTT. Isso permite que a Fog, que é um cliente inscrito nos tópicos do broker, receba as informações em tempo real e possa direcionar os motoristas para os postos mais próximos e com menor tempo de espera.

A Fog é a parte do sistema responsável por gerenciar as solicitações dos motoristas e direcioná-los para os postos de recarga disponíveis. A Fog também funciona como um servidor, pois possui rotas para o acesso do carro via API REST.

O Car representa o carro elétrico e, quando sua bateria está ficando descarregada, faz uma requisição HTTP para a Fog mais próxima dele para saber qual o posto de recarga mais indicado para sua situação.

Por fim, o frontend feito em React permite a fácil visualização do mapa com os servidores, postos de recarga e carros em tempo real. O usuário pode ver onde estão os postos de recarga e a disponibilidade deles, bem como a localização dos carros elétricos na cidade.

Essa arquitetura de microsserviços permite que cada componente do sistema seja desenvolvido e testado de forma independente, facilitando a manutenção e o aprimoramento da aplicação como um todo.

<lu>
    <li><a href="#car">Car</a></li>
    <li><a href="#station">GasStation</a></li>
    <li><a href="#fog">Fog</a></li>
    <li><a href="#server">Server</a></li>
</lu>
</div>

<br>

<div id="car">  
  
# Car 📱


</div>

<div id="station">

# Gas Station ⛽

Este é um arquivo Python que implementa um dos postos de recarga de veículos elétricos no sistema de acompanhamento de filas em postos de recarregamento de carros elétricos. A aplicação utiliza a biblioteca Paho MQTT para se comunicar com o broker MQTT e publicar informações sobre as filas de recarregamento.

## Funcionalidades 🚀

O servidor tem as seguintes funcionalidades:

- Publica a informação da fila de recarga do posto no tópico "station/queue/[client_id]" a cada 10 segundos.

- Publica as coordenadas geográficas do posto no tópico "station/map/[client_id]" assim que estabelecida a área geográfica.
## Bibliotecas utilizadas 📚

- `paho.mqtt`: biblioteca para comunicação via MQTT com o broker.
## Como executar 🛠️
1. É necessário ter o Python e a biblioteca Paho MQTT instalados na máquina.

```console
python Station.py
```

2. Execute o arquivo Station.py através do terminal com o comando: python Station.py
3. Siga as instruções para informar as coordenadas geográficas do posto.
4. As informações da fila de recarga serão publicadas automaticamente a cada 10 segundos.

## Como funciona 📝

O arquivo Station.py é um módulo do sistema de acompanhamento de filas em postos de recarregamento de carros elétricos. Ele é responsável por gerar as informações de filas de um posto de recarga e publicá-las em um tópico do broker MQTT.

A função connect_mqtt() é responsável por realizar a conexão com o broker MQTT, configurando o cliente com o ID, nome de usuário e senha fornecidos. A função também define a função de retorno on_connect() para imprimir uma mensagem informando se a conexão foi estabelecida com sucesso ou não.

A função publish() recebe como entrada um cliente MQTT e as coordenadas do posto de recarga. A função publica as coordenadas em um tópico "station/map/{client_id}" para que a Fog possa visualizar a localização do posto de recarga em um mapa. A função também inicia um loop infinito em que envia, a cada 10 segundos, um número aleatório entre 0 e 10 que representa a quantidade de carros na fila do posto de recarga, para o tópico "station/queue/{client_id}".

A função menu() é responsável por obter as coordenadas de localização do posto de recarga do usuário, que são usadas posteriormente para publicar a localização do posto de recarga no broker MQTT.

Por fim, a função run() é responsável por chamar as funções anteriores na ordem correta para executar a funcionalidade do módulo. Ela chama a função menu() para obter as coordenadas de localização, em seguida chama a função connect_mqtt() para estabelecer a conexão com o broker MQTT e, por fim, chama a função publish() para enviar as informações de filas do posto de recarga para o broker MQTT.

Dessa forma, o módulo Station.py permite a comunicação inteligente e em tempo real entre os postos de recarga de carros elétricos e a Fog, de modo que a Fog possa orientar os motoristas e distribuir a demanda entre os pontos, reduzindo o tempo necessário para a recarga dos veículos.

</div>


<div id ="fog">

# Fog 🌫

O Fog é uma aplicação que se conecta a um broker MQTT para obter informações sobre estações de recarga de carros elétricos e disponibiliza essas informações através de uma API REST. Através da API, é possível obter informações como a estação de recarga mais próxima, todas as estações disponíveis, suas posições geográficas e mais.

## Funcionalidades 🚀

A API REST disponibilizada pelo Fog possui as seguintes funcionalidades:

- */lessQueue*: retorna a estação de recarga mais próxima, levando em consideração a distância e a fila de espera.
- */station*s: retorna uma lista com todas as estações disponíveis.
- */positions*: retorna uma lista com as posições geográficas de todas as estações disponíveis.
- */allData*: retorna todas as informações disponíveis sobre as estações, como posição geográfica e fila de espera.

## Bibliotecas utilizadas 📚

O Fog utiliza as seguintes bibliotecas:

- `paho.mqtt`: biblioteca para se conectar ao broker MQTT e receber mensagens.
- `geopy.distance`: biblioteca para calcular a distância geográfica entre dois pontos.
- `flask`: biblioteca para criar a API REST.
- `flask_cors`: biblioteca para habilitar o CORS na API REST.

## Como executar 🛠️

1. Instale as dependências com o comando pip install -r requirements.txt.
2. Edite o arquivo Fog.py e altere as constantes broker, port, username e password de acordo com as configurações do seu broker MQTT.
3. Execute o comando python Fog.py para iniciar a aplicação. Será solicitado que informe a porta que a aplicação irá utilizar.

## Como funciona 📝

A parte de como funciona do código Fog.py é baseada em um modelo de arquitetura de Internet das Coisas (IoT) chamado de computação em nevoeiro (ou fog computing, em inglês). Essa arquitetura é uma extensão da computação em nuvem, porém com recursos mais próximos dos dispositivos finais, ou seja, mais próximos dos usuários ou das coisas conectadas.

No caso específico deste código, a arquitetura fog computing é utilizada para fornecer informações em tempo real sobre estações de recarga de veículos elétricos. Para isso, a aplicação é dividida em dois módulos principais: um módulo de publicação de informações, representado por uma estação de recarga que publica informações em um servidor MQTT; e um módulo de consumo de informações, que é o responsável por receber e processar as informações publicadas pelas estações de recarga.

O módulo de consumo é implementado pela aplicação Flask, que atua como um servidor web e expõe endpoints HTTP que podem ser acessados pelos usuários para consultar as informações das estações de recarga. A comunicação entre a aplicação Flask e as estações de recarga é feita por meio do protocolo MQTT, que é implementado pela biblioteca Paho MQTT.

Para realizar o cálculo do tempo de chegada de um veículo elétrico a uma estação de recarga, é utilizada a biblioteca Geopy, que fornece funções para cálculos de distâncias entre coordenadas geográficas. Além disso, a aplicação também utiliza a biblioteca threading para executar os módulos de publicação e consumo de informações em threads separadas, garantindo que a aplicação seja capaz de lidar com múltiplas conexões simultâneas.

Em resumo, o código Fog.py implementa uma arquitetura de computação em nevoeiro para fornecer informações em tempo real sobre estações de recarga de veículos elétricos. Ele utiliza o protocolo MQTT para a comunicação entre as estações de recarga e a aplicação Flask, e a biblioteca Geopy para calcular o tempo de chegada dos veículos elétricos às estações de recarga. A aplicação também é capaz de lidar com múltiplas conexões simultâneas, graças ao uso da biblioteca threading.

</div>

<div id ="server">

# Server ☁
O Server é um arquivo Dockerfile que tem como objetivo criar um container com a imagem do Mosquitto, um broker MQTT de código aberto. Ele é responsável por gerenciar as conexões entre os dispositivos IoT, como as estações de recarga e os carros elétricos, permitindo que eles troquem informações em tempo real.

## Funcionalidades 🚀

Criação de um container com a imagem do Mosquitto;
Gerenciamento de conexões entre dispositivos IoT.

## Bibliotecas utilizadas 📚

Docker.

## Como executar 🛠️

1. Instale o Docker em sua máquina;
2. No terminal, navegue até a pasta onde se encontra o arquivo Dockerfile;
3. Execute o comando docker build -t mosquitto-image . para criar a imagem do Mosquitto;
4. Em seguida, execute o comando docker run -p 1883:1883 mosquitto-image para criar o container com a imagem do Mosquitto.

## Como funciona 📝

O arquivo Dockerfile contém as instruções para criar um container com a imagem do Mosquitto. O Dockerfile inicia criando uma imagem base do sistema operacional Linux, adicionando em seguida os pacotes necessários para instalar e executar o Mosquitto. Em seguida, configura a porta padrão do Mosquitto (1883) e a porta de acesso ao protocolo WebSocket (9001). Por fim, são adicionados arquivos de configuração para o Mosquitto, permitindo a configuração do usuário e senha para acesso ao broker MQTT.

Ao executar o comando docker build, o Docker cria a imagem do Mosquitto, contendo todas as configurações necessárias. Ao executar o comando docker run, é criado um container a partir da imagem previamente criada. Esse container é executado em segundo plano, mantendo o broker MQTT ativo e aguardando conexões entre os dispositivos IoT.

Assim, o Server se torna essencial para o funcionamento da arquitetura do sistema, permitindo que os dispositivos IoT possam se conectar e trocar informações em tempo real através do broker MQTT.
</div>

<div id="docker">

# Docker 🐳

Para gerar as imagens das aplicações em Python (Car, Fog e Gas Station), existem arquivos Dockerfile prontos para serem utilizados. Esses arquivos contêm as instruções necessárias para gerar as imagens da aplicação, incluindo as dependências, configurações e arquivos necessários para que a aplicação seja executada.

Resumidamente você irá precisar executar dois comandos: `docker build` e `docker run`.

Por exemplo, suponha que você tem um arquivo Dockerfile na raiz do projeto do servidor (o que é o caso) em Python com o nome Dockerfile.server e quer gerar a imagem com o nome meu-servidor. Para criar a imagem, execute o seguinte comando no terminal, dentro da pasta raiz do projeto:

```console
docker build -t meu-servidor -f Dockerfile.server .
```

Nesse comando, o parâmetro -t é utilizado para definir o nome da imagem que será gerada e o parâmetro -f é utilizado para especificar o arquivo Dockerfile a ser utilizado. O ponto no final indica que o contexto para a construção da imagem é a pasta atual.

Após a criação da imagem, ela pode ser executada com o comando docker run. É possível definir as portas que a aplicação utilizará e outras configurações através de parâmetros nesse comando. Por exemplo:

```console
docker run -p 1883:1883 meu-servidor
```

Nesse comando, o parâmetro -p é utilizado para definir a porta da máquina host que será redirecionada para a porta da aplicação dentro do container. O primeiro valor é a porta da máquina host e o segundo valor é a porta da aplicação dentro do container.

Caso queira compartilhar a imagem gerada em um repositório Docker, basta fazer o push dessa imagem com o comando docker push passando o nome da imagem e a tag correspondente. Por exemplo:

```console
docker push meu-repositorio/meu-servidor:1.0
```
Nesse comando, o nome meu-repositorio é o nome do seu repositório no Docker Hub e a tag 1.0 é a versão da imagem que está sendo enviada.

Com esses comandos, é possível gerar e executar as imagens das aplicações em Python com o Docker.

</div>

<div id ="conclusao">

# Conclusão 🏁

Com base no projeto desenvolvido, foi possível implementar um sistema de medição de energia elétrica em Python. O projeto foi dividido em duas partes principais: o backend e o frontend. No backend, foi implementado um servidor que recebe os dados de consumo de energia elétrica enviados pelos clientes. Foi utilizado o protocolo TCP/IP para a comunicação entre os clientes e o servidor, e a biblioteca Socket do Python foi utilizada para implementar o servidor.

No frontend, foi desenvolvido um cliente que envia os dados de consumo de energia elétrica para o servidor. O cliente foi implementado utilizando a biblioteca Socket do Python para criar e configurar o socket de rede, a biblioteca JSON para serializar os dados em formato JSON, a biblioteca Datetime para gerar a data e hora atuais, e a biblioteca Threading para executar o envio de dados e a configuração de taxa de consumo em threads separadas. O cliente permite ao usuário configurar a taxa de consumo de energia elétrica e enviar os dados para o servidor.

Além disso, foi desenvolvido um frontend em React, Tailwind CSS e Typescript, utilizando as bibliotecas Radix UI e Material UI para os componentes de interface do usuário. O frontend possui três principais páginas: a página de login, a página de histórico e a página de fatura. Na página de login, o usuário insere seu ID de cadastro válido e é redirecionado para a página de histórico, que mostra o histórico de consumo atual e gráficos relacionados a ele. Nessa página, o usuário pode ir para a página de fatura, que mostra o valor atual da fatura e algumas informações juntamente com o QRCode da fatura.

O projeto foi um sucesso, e todas as funcionalidades propostas foram implementadas com sucesso. A entrega do projeto foi feita dentro do prazo estipulado e com alta qualidade. O resultado final foi um sistema de medição de energia elétrica robusto e funcional, que atende às necessidades dos usuários de forma eficiente e fácil de usar.

</div>

</div>