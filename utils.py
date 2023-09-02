import openai


def open_ai(data_id):
    # Ваш API ключ от OpenAI
    api_key = "YOUR_API_KEY"

    # Текст запроса
    query = f"ID Х{data_id}"

    # Отправка запроса к OpenAI GPT-3
    response = openai.Completion.create(
        engine="davinci",  # Модель GPT-3
        prompt=query,  # Текст запроса
        max_tokens=50,  # Максимальное количество токенов в ответе
        api_key=api_key  # Ваш API ключ
    )

    # Получение ответа от GPT-3
    if response.choices:
        # Вывод сгенерированного ответа
        generated_response = response.choices[0].text
        print("Сгенерированный ответ:", generated_response)
        return {"status": 200, "message": generated_response}
    else:
        print("Не удалось получить ответ от GPT-3")
        return {"status": 404, "message": "Не удалось получить ответ от GPT-3"}
