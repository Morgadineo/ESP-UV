# ESP32 WITH UV SENSOR

## Planos

* 1 - Utilizar um ESP32 e um sensor UV para detectar a frequência e intensidade
    dos raios ultravioletas. 
* 2 - Desenvolver um manual extremamente simples, para que qualquer pessoa com
    conhecimentos básicos possa criar o dispositivo.
* 3 - Desenvolver um sistema web para armazenar *(automaticamente: o arduino
    automaticamente envia os valores coletados para a web; manualmente: o
    usuário insere os valores exibidos pelo arduino)* as frequências obtidas
    pelo arduino.
* 3.1 - Modelar o banco de dados para armazenar as frequências.


**IDEIA: Poderia criar uma página web local onde o dispositivo mostra os
dados obtidos ou utilizar uma API para que seja possível acessar facilmente
os dados do arduino.**

### Desenvolvimento dos planos

#### 1

Já pesquisei e encontrei 2 projetos utilizando  ESP32 com sensores UV, porém
nenhum deles utiliza a conexão com a internet para armazenar os valores obtidos.
Na realidade, os dois projetos apenas mostravam em um leitor LCD. Essa parte do
hardware é relativamente tranquila, a parte complicada mesmo está em como
armazenar e salvar os dados obtidos pelo sensor.


## Parte de Hardware

Para o hardware, estamos utilizando um ESP32 pois já vem com componentes para se
conectar com a internet. O sensor UV que será utilizado ainda não foi decidido.

### GET https://api.meersens.com/environment/public/uv/current

