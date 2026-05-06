# Vyreon

Um aplicativo experimental com Python, Django e Bootstrap 5.

## Instruções

1. Faça _fork_ deste repositório;
2. _Clone_ o fork no seu PC;
3. Abra no VSCode;
4. Abra um _CMD_ e crie o `venv` → `python -m venv .venv`;
5. Ative o `venv` → `.venv\Scripts\activate`;
6. Instale as dependências → `pip install -r requirements.txt`;
7. Rode o servidor HTTP → `python manage.py rubnserver`;
8. Acesse, pelo navegador, no endereço `http://localhost:8000`.

## Templates do Usuário

Todos os templates personalizados, relacionados ao **fluxo do usuário**, estão em `vyreon\templates\user`.

## Reset da Senha

Por padrão, ao solicitar uma nova senha, a mensagem com o link de _Reset_ é enviada para o terminal em que o serviço está rodando.
Isso é definido em `core\settings.py`, na linha:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Para "realmente" enviar um e-mail para o usuário solicitante, altere a linha acima para:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

Também, adicione as linhas, logo abaixo da anterior:

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Sua conta de e-mail do Gmail
EMAIL_HOST_USER = 'você@gmail.com'
# Acesse https://myaccount.google.com/apppasswords para gerar a senha de aplicativo abaixo
EMAIL_HOST_PASSWORD = 'aaaa bbbb cccc dddd'
# Sua conta de e-mail do Gmail, a mesma acima
DEFAULT_FROM_EMAIL = 'você@gmail.com'
```

Para usar o Gmail como servidor de envio você precisa de uma senha de app, **não da senha normal da conta**.

Siga as instruções dos comentários acima, lembrando que a senha de aplicativo só pode ser gerada se você ativou a [**autenticação multifatores**](https://support.google.com/mail/answer/185839?hl=pt-BR&ref_topic=3394217) em sua conta Google.

