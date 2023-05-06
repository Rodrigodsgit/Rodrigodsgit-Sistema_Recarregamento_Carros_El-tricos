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

<div id="client">  
  
# Measurer (Cliente/Medidor) 📱

## Funcionalidades 🚀

O cliente tem as seguintes funcionalidades:

- Envia dados de consumo de energia elétrica para um servidor
- Permite ao usuário configurar a taxa de consumo de energia elétrica

## Bibliotecas utilizadas 📚

Para implementar o cliente, foram utilizadas as seguintes bibliotecas Python:

- `socket`: para criar e configurar o socket de rede
- `json`: para serializar os dados em formato JSON
- `datetime`: para gerar a data e hora atuais
- `time`: para controlar o tempo de envio de dados
- `threading`: para executar o envio de dados e a configuração de taxa de consumo em threads separadas

## Como executar 🛠️

Para executar o cliente, é necessário executar o arquivo client.py.

```console
python measurer.py
```

## Como usar 📝

1. Clone este repositório em sua máquina local.
2. Certifique-se de que os requisitos estejam instalados.
3. Execute o servidor primeiro.
4. Em seguida, execute o arquivo measurer.py.
5. Siga as instruções do menu para alterar a taxa de consumo ou sair do programa.

O cliente está configurado para enviar dados para o servidor com endereço IP "172.16.103.2" e porta 4005. Para configurar a taxa de consumo de energia elétrica, siga as opções exibidas no menu. Para sair do programa, escolha a opção "4".

## Como funciona 📝

O cliente é responsável por enviar dados do consumo de energia elétrica para o servidor através de uma conexão socket TCP/IP. Ele é desenvolvido em Python e utiliza a biblioteca socket para realizar a comunicação com o servidor. O cliente é iniciado a partir da execução do arquivo measurer.py.

O código do cliente é dividido em duas principais funções:

### Função get_id()
Essa função é responsável por solicitar ao servidor um ID para o medidor de consumo de energia elétrica. Ela envia uma mensagem JSON contendo o valor 0 para o servidor e aguarda a resposta com o ID, que é armazenado na variável id.

### Função send_data()
Essa função é responsável por enviar para o servidor os dados de consumo de energia elétrica em tempo real. Ela envia uma mensagem JSON contendo o ID do medidor, o valor do consumo, a data e hora do consumo e o tipo de mensagem. A variável rate é utilizada para simular o consumo em tempo real, e a variável spent é utilizada para armazenar o total consumido pelo medidor.

Além dessas funções, o código do cliente também possui uma função menu() que permite ao usuário alterar a taxa de consumo do medidor. Essa função é executada em uma thread separada, e permite que o usuário aumente, diminua ou defina uma nova taxa de consumo. A thread principal do cliente é responsável por enviar os dados de consumo em tempo real.

Ao final da execução, o cliente é encerrado e a conexão com o servidor é fechada.

</div>

<div id="server">

# Server (API REST) 🖥️🌐

## Funcionalidades 🚀
O servidor tem as seguintes funcionalidades:

- Recebe requisições HTTP GET e POST
- Interpreta as requisições e envia a resposta adequada para cada uma delas
- Armazena os dados das requisições POST para uso posterior

## Bibliotecas utilizadas 📚

Para implementar o servidor, foram utilizadas as seguintes bibliotecas Python:

- `socket`: para criar e configurar o socket de rede
- `selectors`: para gerenciar eventos de I/O de forma eficiente
- `types`: para definir os tipos dos objetos utilizados pelo programa
- `json`: para serializar os dados em formato JSON

## Como executar 🛠️
Para executar o servidor, é necessário executar o arquivo initialize.py e estar no mesmo diretório do arquivo.

```console
python initialize.py
```
## Como funciona 📝

O código apresentado é um servidor web simples que pode lidar com as solicitações GET e POST enviadas por um cliente. Ele utiliza a biblioteca selectors para suportar operações de I/O multiplexadas, permitindo que o servidor possa lidar com várias conexões de forma eficiente.

Inicialmente, o servidor cria um objeto DefaultSelector() da biblioteca selectors que será responsável por gerenciar as operações de I/O das conexões. Em seguida, ele define um endereço IP e porta para a conexão do socket e cria um socket de escuta com o método socket(). O socket de escuta aguarda a conexão de novos clientes.

O método register() é utilizado para registrar um socket com o seletor de E/S, especificando o evento a ser monitorado (EVENT_READ para leitura ou EVENT_WRITE para escrita), bem como os dados adicionais que serão associados ao socket.

O método accept_wrapper() é chamado sempre que uma nova conexão é aceita pelo servidor. Ele extrai a conexão e o endereço do cliente e registra o socket com o seletor de E/S, especificando os eventos a serem monitorados.

O método service_connection() é responsável por processar as solicitações recebidas de cada conexão registrada. Ele verifica se há dados a serem lidos e, se sim, os armazena em um buffer. Em seguida, ele chama a função type_mensage() para analisar a solicitação recebida e determinar se ela é uma solicitação GET, POST ou outro tipo de solicitação. Dependendo do tipo de solicitação, o método service_connection() pode chamar as funções get() ou post() para processar os dados e gerar uma resposta. Se houver dados a serem escritos, o método service_connection() envia a resposta para o cliente. Se a solicitação não puder ser processada, o método type_mensage() retorna um erro.

O servidor continua a executar em um loop infinito, aguardando novas conexões e processando as solicitações recebidas. O loop é interrompido somente se o programa for interrompido por um sinal de teclado (KeyboardInterrupt). Quando o loop é interrompido, o servidor é encerrado e o seletor de E/S é fechado com o método close().

</div>

<div id ="user">

# User (Frontend) 👤💻

Este é um projeto para construir um frontend para um sistema de medição de consumo de energia elétrica. O frontend foi construído utilizando React, Tailwind CSS e TypeScript, com a configuração do ambiente utilizando Vite. Para criar a interface, foram utilizadas as bibliotecas de UI Radix UI e Material UI. O consumo de dados é feito através do Axios, que consome a API previamente desenvolvida.

## Funcionalidades 🚀
O frontend tem as seguintes funcionalidades:

- Tela de login na rota "/signin"
- Após inserir o ID válido, o cliente é redirecionado para a página de histórico, que mostra o histórico de consumo atual e gráficos relacionados a ele
- Na tela de histórico, é possível ir para a tela de fatura (invoice), que contém o valor atual da fatura e algumas informações, juntamente com o QRCode da fatura.

## Bibliotecas utilizadas 📚
Para implementar o frontend, foram utilizadas as seguintes bibliotecas:

- React: para a criação de componentes reutilizáveis
- Tailwind CSS: para a estilização da interface
- TypeScript: para o desenvolvimento de código mais seguro e com maior integridade
- Vite: para a configuração do ambiente de desenvolvimento
- Axios: para o consumo da API previamente desenvolvida
- Radix UI: para a criação de componentes de interface personalizados
- Material UI: para a utilização de ícones e componentes predefinidos

## Como executar 🛠️
Para executar o frontend, primeiro deve se  atentar a ter já seu server e alguns clientes rodando para uma melhor visualização da interface, além de evitar erros. Dito isso, é necessário  executar o seguinte comando:

```console
npm install
npm run dev
```

## Como Funciona 📝

Como não foi solicitado uma interface web para o cliente, não entraremos em muitos detalhes de como foi feito. No entanto, é possível utilizar as telas de login, histórico e fatura do sistema através das rotas "/signin", "/historic" e "/invoice", respectivamente. Para acessar a tela de fatura, é necessário ter inserido um ID válido na tela de login.

<br>

<div id="image01" style="display: inline_block" align="center">
		<img src="assets/login.png"/>
		<p>
			Tela de Login
			</p>
		</div>

</div>

<div id="image02" style="display: inline_block" align="center">
		<img src="assets/historic.png"/>
		<p>
			Tela de Histórico
			</p>
		</div>

</div>

<div id="image03" style="display: inline_block" align="center">
		<img src="assets/invoice.png"/>
		<p>
			Tela de Fatura
			</p>
		</div>

</div>

<div id="docker">

# Docker 🐳

Para gerar as imagens das aplicações em Python (Client e Server), existem arquivos Dockerfile prontos para serem utilizados. Esses arquivos contêm as instruções necessárias para gerar as imagens da aplicação, incluindo as dependências, configurações e arquivos necessários para que a aplicação seja executada.

Resumidamente você irá precisar executar dois comandos: `docker build` e `docker run`.

Por exemplo, suponha que você tem um arquivo Dockerfile na raiz do projeto do servidor (o que é o caso) em Python com o nome Dockerfile.server e quer gerar a imagem com o nome meu-servidor. Para criar a imagem, execute o seguinte comando no terminal, dentro da pasta raiz do projeto:

```console
docker build -t meu-servidor -f Dockerfile.server .
```

Nesse comando, o parâmetro -t é utilizado para definir o nome da imagem que será gerada e o parâmetro -f é utilizado para especificar o arquivo Dockerfile a ser utilizado. O ponto no final indica que o contexto para a construção da imagem é a pasta atual.

Após a criação da imagem, ela pode ser executada com o comando docker run. É possível definir as portas que a aplicação utilizará e outras configurações através de parâmetros nesse comando. Por exemplo:

```console
docker run -p 4005:4005 meu-servidor
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