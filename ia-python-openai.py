#instalar a lib da Openai
!pip install openai

import openai

# seta a API key
openai.api_key = 'INSERIR AQUI SUA API KEY ENTRE ASPAS'

# Definição de persona do sistema e cria histórico de mensagens
messages = [
        {"role": "system", "content": "Você é um assistente prestativo."}
]

input_message = input('Esperando input: ')

messages.append({"role": "user", "content": input_message})  # adiciona a primeira pergunta no histórico do chat

# enquanto o input não for a palavra 'fim'
while input_message != 'fim':
    # Chamada à API
    response = openai.ChatCompletion.create(
        model = 'gpt-4',
        messages = messages,
        max_tokens = 200,
        temperature = 1
    )

    # Extrai a resposta de dentro do JSON de resposta
    answer = response['choices'][0]['message']['content']
	
    messages.append({"role": "assistant", "content": answer})  # adiciona a resposta no histórico do chat

    # Imprime a resposta
    print("Resposta: ", answer, '\n\n')

    input_message = input('Esperando input: ')
	
    messages.append({"role": "user", "content": input_message})  # adiciona a nova pergunta no histórico do chat