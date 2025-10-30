import google.generativeai as genai

class Boot_gemini:
    """Boot especialista em responder perguntas sobre culinaria"""

    def __init__(self):
        genai.configure(api_key="AIzaSyDBoTTE06H5ADrvPqwDbqLH_piX3jt0NoQ")
        instrucao_sistema = """Voce é uma chefe de cozinha, especialista em tecnicas de culinaria, 
        com vinte anos de experiencia. Seu nome será Ms. Sookie.Você deve responder a todas as perguntas de forma 
            profissional, detalhada e focada exclusivamente no mundo da culinaria. 
            Se o usuário perguntar sobre outro assunto, gentilmente redirecione a conversa 
            de volta para culinaria, afirmando que seu conhecimento é especializado."""
        
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
    
if __name__ == "__main__":
    robo = Boot_gemini()
    resposta = robo.responder("Me ajude a fazer algo em croche")
    print(resposta)
