# examples/language_detection.py

from src.empathy_one.empathy import EmpathyOne

# Initialize without specifying a language
empathy_model = EmpathyOne()

# User input in French
user_input = "Je suis déçu par votre produit."

# Generate an empathetic response
response = empathy_model.generate_response(user_input)

print(response)
