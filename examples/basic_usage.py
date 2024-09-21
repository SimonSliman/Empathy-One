# examples/basic_usage.py

from src.empathy_one.empathy import EmpathyOne

# Initialize the Empathy-One model for Spanish
empathy_model = EmpathyOne(language='es')

# User input in Spanish
user_input = "Estoy muy frustrado con el servicio."

# Generate an empathetic response
response = empathy_model.generate_response(user_input)

print(response)
