from classe_bot_gemini import Boot_gemini
from classe_bot_bravo import Boot_bravo

robo = Boot_gemini()
robo = Boot_bravo()

resposta = robo.responder("Me ajude a programar em phyton")
print(resposta)
