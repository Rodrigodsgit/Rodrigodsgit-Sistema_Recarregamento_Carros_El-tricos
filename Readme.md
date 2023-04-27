<div id="image03" style="display: inline_block" align="center">
		<img src="assets/logo.png"/>
</div>

<div style="display: inline_block" align="center">
<a href="#en"> English </a> |
<a href="#pt"> Portuguese  </a> 
</div>

<br>

<div id="en">

<h1 align="center"> Table of Contents 📖 </h1>
<div id="table-of-contents" style="display: inline_block" align="center">
	<a href="#intro"> Introduction  </a> |
	<a href="#concepts"> Concepts & Methodology </a> |
	<a href="#docker"> Docker </a> |
	<a href="#conclusion"> Conclusion </a>
</div>
<br>

<div id="intro">

# Introduction 🎉

Efficiency in the supply of electricity is essential for a smart and sustainable city. In order to offer quality service to the population, the city government of a certain city has decided to adopt an IoT infrastructure to monitor real-time electricity consumption and promote conscious use of resources.

To achieve this goal, the city government and the electricity provider launched a bid that seeks IoT technology entrepreneurs to present solutions that allow the collection and analysis of electricity consumption data on a large scale.

In this context, our startup was invited to present a prototype that uses IoT technologies to collect, process, and present electricity consumption data in a simple and accessible way. Our system will allow each customer to have more precise control over their electricity consumption, being able to monitor it in real-time and identify possible bottlenecks that generate waste and excessive spending.

In this report, we present a prototype developed by a fictitious startup that aims to solve the problem proposed by the city government. The prototype consists of an automated data collection system, which allows for the generation of precise information about energy consumption in households, calculation of the invoice to be paid, and sending alerts to users in case of excessive consumption or variation in the bill. In addition, the solution involves a socket server that will receive data from the smart meters installed in users' homes, and it will be possible to view this data online through a web interface that consumes a REST API.

Throughout this report, we will detail the system architecture, technologies used, results obtained, and possible improvements for the future. We hope this report will be useful for other companies and city governments that wish to incorporate IoT in their services and make their cities smarter.

Let's embark on this journey together in search of a smarter and more sustainable city! 💡🌍

</div>

<div id="concepts">

# Concepts & Methodology 📚

The developed code is divided into three main parts: the first part is the meter, which functions as the client and is responsible for sending energy consumption data to the server. The second part is the server, which stores all the data sent by the meters via sockets. And the third part is the online user, where a React-based web interface was created to visualize real-time energy consumption data.

The concepts that encompass the main problem of the project are: the use of sockets for communication between different devices, REST API, which allows the data to be delivered to the client through the HTTP protocol, the use of threads and other forms to keep track of multiple connections, and Docker for containerizing the project, ensuring that the development and production environments are identical, facilitating the deployment of the system.

These concepts will be further discussed throughout the 3 parts that make up the application, as well as their methodology.

<lu>
    <li><a href="#client">Client</a></li>
    <li><a href="#server">Server</a></li>
    <li><a href="#user">User</a></li>
</lu>
</div>
<br>

<div id="client">  

# Measurer (Client) 📱

## Features 🚀
The client has the following features:

- Sends electricity consumption data to a server
- Allows the user to configure the electricity consumption rate

## Libraries Used 📚
The following Python libraries were used to implement the client:

- `socket`: to create and configure the network socket
- `json`: to serialize data in JSON format
- `datetime`: to generate the current date and time
- `time`: to control the data sending time
- `threading`: to execute data sending and consumption rate configuration in separate threads

## How to Run 🛠️
To run the client, you need to execute the measurer.py file.

```console
python measurer.py
```
## How to Use 📝

- Clone this repository on your local machine.
- Ensure that the requirements are installed.
- Run the server first.
- Then run the measurer.py file.
- Follow the menu instructions to change the consumption rate or exit the program.

The client is set to send data to the server with the IP address "172.16.103.2" and port 4005. To configure the electricity consumption rate, follow the options displayed on the menu. To exit the program, choose the option "4".

## How it Works 📝
The client is responsible for sending real-time electricity consumption data to the server through a TCP/IP socket connection. It is developed in Python and uses the socket library to communicate with the server. The client is started by executing the measurer.py file.

The client code is divided into two main functions:

### Function get_id()
This function is responsible for requesting an ID for the electricity consumption meter from the server. It sends a JSON message containing the value 0 to the server and waits for the response with the ID, which is stored in the id variable.

### Function send_data()
This function is responsible for sending electricity consumption data to the server in real-time. It sends a JSON message containing the meter ID, the consumption value, the date and time of consumption, and the message type. The rate variable is used to simulate real-time consumption, and the spent variable is used to store the total consumed by the meter.

In addition to these functions, the client code also has a menu() function that allows the user to change the meter consumption rate. This function is executed in a separate thread and allows the user to increase, decrease, or set a new consumption rate. The main thread of the client is responsible for sending real-time consumption data.

At the end of the execution, the client is terminated, and the connection with the server is closed.
</div>

<div id="server">

# Server (REST API) 🖥️🌐

## Features 🚀
The server has the following features:

- Receives HTTP GET and POST requests
- Interprets requests and sends appropriate responses to each one
- Stores POST request data for later use

## Used libraries 📚
To implement the server, the following Python libraries were used:

- `socket`: to create and configure the network socket
- `selectors`: to manage I/O events efficiently
- `types`: to define the types of objects used by the program
- `json`: to serialize data in JSON format

## How to execute 🛠️
To run the server, it is necessary to execute the initialize.py file and be in the same directory as the file.

```console
python initialize.py
```


## How it works 📝

The presented code is a simple web server that can handle GET and POST requests sent by a client. It uses the selectors library to support multiplexed I/O operations, allowing the server to handle multiple connections efficiently.

Initially, the server creates a DefaultSelector() object from the selectors library that will be responsible for managing the I/O operations of the connections. Then, it defines an IP address and port for the socket connection and creates a listening socket with the socket() method. The listening socket waits for new clients to connect.

The register() method is used to register a socket with the I/O selector, specifying the event to be monitored (EVENT_READ for reading or EVENT_WRITE for writing), as well as the additional data to be associated with the socket.

The accept_wrapper() method is called whenever a new connection is accepted by the server. It extracts the connection and client address and registers the socket with the I/O selector, specifying the events to be monitored.

The service_connection() method is responsible for processing the requests received from each registered connection. It checks if there is data to be read and, if so, stores it in a buffer. Then, it calls the type_mensage() function to parse the received request and determine if it is a GET, POST, or other type of request. Depending on the type of request, the service_connection() method may call the get() or post() functions to process the data and generate a response. If there is data to be written, the service_connection() method sends the response to the client. If the request cannot be processed, the type_mensage() method returns an error.

The server continues to run in an infinite loop, waiting for new connections and processing received requests. The loop is only interrupted if the program is interrupted by a keyboard signal (KeyboardInterrupt). When the loop is interrupted, the server is terminated and the I/O selector is closed with the close() method.

</div>

<div id ="user">

# User (Frontend) 👤💻

This is a project to build a frontend for an electricity consumption measurement system. The frontend was built using React, Tailwind CSS, and TypeScript, with the environment configuration using Vite. To create the interface, Radix UI and Material UI UI libraries were used. Data consumption is done through Axios, which consumes the previously developed API.

## Features 🚀
The frontend has the following features:

- Login screen on the "/signin" route
- After entering a valid ID, the customer is redirected to the history page, which shows the current consumption history and related graphs
- On the history page, it is possible to go to the invoice screen, which contains the current invoice amount and some information, along with the invoice QRCode.

- Used libraries 📚
The following libraries were used to implement the frontend:

- `React`: for creating reusable components
- `Tailwind CSS`: for styling the interface
- `TypeScript`: for developing more secure and integrated code
- `Vite`: for configuring the development environment
- `Axios`: for consuming the previously developed API
- `Radix UI`: for creating custom interface components
- `Material UI`: for using pre-defined icons and components

## How to run 🛠️
To run the frontend, first ensure that your server and some clients are already running for better interface visualization and to avoid errors. Having said that, the following command must be executed:

```console
npm install
npm run dev
```

## How it works 📝
Since a web interface for the client was not requested, we will not go into much detail about how it was done. However, it is possible to use the login, history, and invoice screens of the system through the "/signin", "/historic", and "/invoice" routes, respectively. To access the invoice screen, a valid ID must have been entered on the login screen.

<br>
<div id="image01" style="display: inline_block" align="center">
		<img src="assets/login.png"/>
		<p>
			Login Screen
			</p>
		</div>
</div>
<div id="image02" style="display: inline_block" align="center">
		<img src="assets/historic.png"/>
		<p>
			History Screen
			</p>
		</div>
</div>
<div id="image03" style="display: inline_block" align="center">
		<img src="assets/invoice.png"/>
		<p>
			Invoice Screen
			</p>
		</div>
</div>

<div id="docker">

# Docker 🐳
To generate the images of Python applications (Client and Server), there are ready-to-use Dockerfile files. These files contain the necessary instructions to generate the application images, including dependencies, configurations, and files needed to run the application.

In summary, you will need to execute two commands: docker build and docker run.

For example, suppose you have a Dockerfile file in the root of the server project (which is the case) in Python with the name Dockerfile.server and want to generate the image with the name my-server. To create the image, execute the following command in the terminal, within the root folder of the project:

```console
docker build -t my-server -f Dockerfile.server .
```

In this command, the -t parameter is used to set the name of the image that will be generated and the -f parameter is used to specify the Dockerfile file to be used. The period at the end indicates that the context for building the image is the current folder.

After creating the image, it can be executed with the docker run command. You can define the ports that the application will use and other settings through parameters in this command. For example:

```console
docker run -p 4005:4005 my-server
```

In this command, the -p parameter is used to define the port of the host machine that will be redirected to the application port inside the container. The first value is the host machine port, and the second value is the application port inside the container.

If you want to share the generated image in a Docker repository, simply push this image with the docker push command, passing the name of the image and the corresponding tag. For example:

```console
docker push my-repository/my-server:1.0
```

In this command, the name my-repository is the name of your repository on Docker Hub, and the tag 1.0 is the version of the image being sent.

With these commands, it is possible to generate and execute the images of Python applications with Docker.

</div>
<div id ="conclusao">

# Conclusion 🏁
Based on the developed project, it was possible to implement an electric energy measurement system in Python. The project was divided into two main parts: the backend and the frontend. In the backend, a server was implemented that receives the electric energy consumption data sent by the clients. The TCP/IP protocol was used for communication between clients and the server, and the Socket library of Python was used to implement the server.

In the frontend, a client was developed that sends the electric energy consumption data to the server. The client was implemented using the Socket library of Python to create and configure the network socket, the JSON library to serialize the data in JSON format, the Datetime library to generate the current date and time, and the Threading library to execute data transmission and consumption rate configuration in separate threads. The client allows the user to configure the electric energy consumption rate and send data to the server.

In addition, a frontend was developed in React, Tailwind CSS, and Typescript, using the Radix UI and Material UI libraries for the user interface components. The frontend has three main pages: the login page, the history page, and the invoice page. On the login page, the user enters their valid registration ID and is redirected to the history page, which shows the current consumption history and related charts. On this page, the user can go to the invoice page, which shows the current value of the invoice and some information along with the QRCode of the invoice.

The project was a success, and all proposed functionalities were successfully implemented. The project was delivered on time and with high quality. The final result was a robust and functional electricity measurement system that efficiently and easily meets the users' needs.

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

A eficiência no fornecimento de energia elétrica é essencial para uma cidade inteligente e sustentável. Visando oferecer um serviço de qualidade para a população, a prefeitura de uma cidade resolveu adotar uma infraestrutura de IoT para monitorar o consumo de energia elétrica em tempo real e promover o uso consciente dos recursos.

Para atingir esse objetivo, a prefeitura e a concessionária de abastecimento lançaram um edital que busca empreendedores de tecnologia especializados em IoT para apresentar soluções que permitam a coleta e análise dos dados de consumo de energia elétrica em larga escala.

Nesse contexto, nossa startup foi convidada a apresentar um protótipo que utiliza tecnologias de IoT para coletar, processar e apresentar os dados de consumo de energia elétrica de forma simples e acessível. Nosso sistema permitirá que cada cliente tenha um controle mais preciso sobre seu consumo de energia elétrica, podendo monitorá-lo em tempo real e identificar possíveis gargalos que gerem desperdícios e gastos excessivos.

Neste relatório, apresentaremos um protótipo desenvolvido por uma startup fictícia que visa solucionar o problema proposto pela prefeitura. O protótipo consiste em um sistema de coleta de dados automatizado, que permite a geração de informações precisas sobre o consumo de energia em residências, o cálculo da fatura a ser paga e o envio de alertas aos usuários em caso de consumo excessivo ou variação na conta. Além disso, a solução envolve um servidor soquete que irá receber dados dos medidores inteligentes instalados nas residências dos usuários, e será possível visualizar esses dados de forma online através de uma interface web que consome uma API REST.

Ao longo deste relatório, detalharemos a arquitetura do sistema, as tecnologias utilizadas, os resultados obtidos e as possíveis melhorias para o futuro. Esperamos que este relatório seja útil para outras empresas e prefeituras que desejam incorporar a loT em seus serviços e tornar suas cidades mais inteligentes.

Vamos juntos nessa jornada em busca de uma cidade mais inteligente e sustentável! 💡🌍
</div>

<div id="conceitos">

# Conceitos & Metodologia 📚

O código desenvolvido é dividido em três grandes partes: a primeira parte é o medidor, que funciona como o cliente e é responsável por enviar os dados de consumo de energia para o servidor. A segunda parte é o servidor, que armazena todos os dados enviados pelos medidores via soquete. E a terceira parte é o usuário online, onde foi criada uma interface web usando React para visualizar os dados de consumo de energia em tempo real.

Os conceitos que abrangem o problema principal do projeto são: o uso de soquetes para comunicação entre dispositivos diferentes, API REST, que permite levar esses dados para o cliente através do protocolo HTTP, o uso de threads e outras formas para acompanhar múltiplas conexões, e o Docker para containerização do projeto, garantindo que o ambiente de desenvolvimento e de produção sejam iguais, facilitando a implantação do sistema.

Esses conceitos serão mais discutidos durante as 3 partes que compõe a aplicação, assim como sua metodologia.

<lu>
    <li><a href="#client">Client</a></li>
    <li><a href="#server">Server</a></li>
    <li><a href="#user">User</a></li>
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