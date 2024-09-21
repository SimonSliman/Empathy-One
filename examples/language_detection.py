# examples/language_detection.py

from src.empathy_one.empathy import EmpathyOne

# Initialize the EmpathyOne model without specifying a language
empathy_model = EmpathyOne()

# List of user inputs in different languages
user_inputs = [
    "Je suis déçu par votre produit.",  # French input
    "Estoy muy frustrado con el servicio.",  # Spanish input
    "Estou insatisfeito com o atendimento.",  # Portuguese input
    "I am very happy with your service."  # English input
]

# Process each input and generate empathetic responses
for user_input in user_inputs:
    response = empathy_model.generate_response(user_input)
    print(f"User Input: {user_input}\nEmpathetic Response: {response}\n")

