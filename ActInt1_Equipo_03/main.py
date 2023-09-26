import os
import re

# Directorio del codigo malicioso
m_directory = "./Mcode"

# Directorio de las transmiciones
t_directory = "./Transmissions"

transmission = []
malicious = []


for m_file in os.listdir(m_directory): # Almacenando todos los códigos que pueden ser maliciosos
    f = os.path.join(m_directory, m_file)
    
    if os.path.isfile(f) and m_file.endswith('.txt'):
        with open (f, 'r') as file:
            string = ""
            
            for line in file:
                string += line.strip()
            
            malicious.append(string)


for t_file in os.listdir(t_directory): # Almacenando todas las transmiciones
    f = os.path.join(t_directory, t_file)
    
    if os.path.isfile(f) and t_file.endswith('.txt'):
        with open (f, 'r') as file:
            string = ""

            for line in file:
                string += line.strip()
                
            transmission.append(string)


