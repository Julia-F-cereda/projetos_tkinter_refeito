from google import genai

client = genai.Client( api_key= "AIzaSyDBoTTE06H5ADrvPqwDbqLH_piX3jt0NoQ")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="como cozinhar?"
)
print(response.text)