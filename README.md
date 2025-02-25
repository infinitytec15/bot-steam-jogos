# Bot de Ofertas da Steam para Discord

Este é um bot que busca ofertas de jogos na Steam e envia as informações para um canal do Discord. O bot envia **um jogo por vez**, com detalhes como nome, preço original, preço com desconto, desconto percentual e link para a página do jogo. Ele é executado a cada **1 minuto**, garantindo que sempre haja uma nova oferta sendo enviada.

---

## Funcionalidades

- Busca informações de jogos na Steam usando a API oficial.
- Envia os detalhes dos jogos em **embeds** organizados e com emojis.
- Envia **um jogo por vez** a cada **1 minuto**.
- Fácil de configurar e rodar na nuvem usando o Railway.

---

## Pré-requisitos

Antes de começar, você precisará de:

1. **Um webhook do Discord**:
   - Crie um webhook no canal do Discord onde deseja receber as ofertas.
   - [Como criar um webhook no Discord](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).

2. **Conta no Railway**:
   - O bot pode ser hospedado gratuitamente no Railway.
   - [Crie uma conta no Railway](https://railway.app/).

3. **Repositório Git**:
   - O código do bot deve estar em um repositório Git (GitHub, GitLab, etc.).

---

## Configuração

### 1. Clone o Repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/meu-bot-steam.git
cd meu-bot-steam
```

### 2. Instale as Dependências

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 3. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione o webhook do Discord:

```plaintext
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

### 4. Execute o Bot Localmente

Para testar o bot localmente, execute:

```bash
python main.py
```

---

## Como Rodar na Nuvem (Railway)

### 1. Suba o Projeto para um Repositório Git

Certifique-se de que o projeto está em um repositório Git (GitHub, GitLab, etc.).

### 2. Conecte o Repositório ao Railway

1. Acesse o [Railway](https://railway.app/).
2. Crie um novo projeto e conecte-o ao seu repositório Git.

### 3. Adicione as Variáveis de Ambiente

No painel do Railway, vá para a aba **Variables** e adicione a variável:

```plaintext
DISCORD_WEBHOOK_URL = https://discord.com/api/webhooks/...
```

### 4. Faça o Deploy

O Railway detectará automaticamente o `Procfile` e fará o deploy do bot.

---

## Estrutura do Projeto

- **`main.py`**: Código principal do bot.
- **`requirements.txt`**: Lista de dependências do Python.
- **`Procfile`**: Instruções para o Railway executar o bot.
- **`.env`**: Arquivo para variáveis de ambiente (usado localmente).
- **`README.md`**: Este arquivo.

---

## Exemplo de Saída no Discord

Cada mensagem enviada pelo bot terá a seguinte aparência:

![Embed Example](https://i.imgur.com/7QZQZQl.png)

- **Título**: 🎮 Nome do Jogo.
- **Descrição**:
  - 💰 **Preço Original**: R$ 99,99.
  - 🛒 **Preço com Desconto**: R$ 49,99.
  - 🎉 **Desconto**: 50%.
- **Thumbnail**: Imagem do jogo.
- **URL**: Link para a página do jogo.

---

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

Se tiver dúvidas ou sugestões, entre em contato:

- **Nome**: Gilberto Jr
- **Email**: gilberto@infinitytec.info
- **GitHub**: infinityetc15 ([https://github.com/seu-usuario](https://github.com/infinitytec15))

---

Feito com ❤️ por Gilberto JR 🚀
