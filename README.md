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
  
**IDEIA: Poderia criar uma página web local onde o dispositivo mostra os
dados obtidos ou utilizar uma API para que seja possível acessar facilmente
os dados do arduino.**

### GET https://api.meersens.com/environment/public/uv/current

