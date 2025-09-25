from groq import Groq

class CarbonEfficientChatbot:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def get_reply(self, user_input):
        completion = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful and sustainable AI assistant."},
                {"role": "user", "content": user_input}
            ],
        )
        return completion.choices[0].message.content
