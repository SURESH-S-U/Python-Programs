import os
import google.generativeai as genai

# We implement these code by using the API key


os.environ['GOOGLE_API_KEY'] = "AIzaSyC-NPDjZCn0BByzDbjEG2j7sjxWMCnLFWQ" 
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

def llm_function(query):
    response = model.generate_content(query)
    return response.text

print("Bot: Hello! How can I assist you today?")

while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit', 'stop']:
        print("Bot: Goodbye!")
        break
    
    bot_response = llm_function(user_input)

    print(f"Bot: {bot_response}")

#dependencies
#pip install operativeai
#pip install google.generativeai