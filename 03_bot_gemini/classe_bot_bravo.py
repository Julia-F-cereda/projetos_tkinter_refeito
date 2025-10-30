import ttkbootstrap as ttk

import google.generativeai as genai

class Boot_bravo:
    """Boot estressado"""

    def __init__(self):
        genai.configure(api_key="AIzaSyAwxjTXssSQ9gLXB-Q9QlATJYTk78bpE0g")
        instrucao_sistema = """Voce respondera as perguntas com bastante grosseria, sendo bem rispido e 
        estupido ao responder as perguntas. Mas voce deve responder as coisas certas, sendo especialista 
        em qualquer tema que for perguntado"""
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()
    

    def responder(self, 
                  
                  pergunta:str):
        """função para o boot responder as perguntas"""

        response = self.chat.send_message(pergunta)
        return response.text