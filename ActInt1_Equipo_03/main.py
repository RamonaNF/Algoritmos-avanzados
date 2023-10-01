from Longest_substr import longest_substr
from Manacher import Manacher
from KMP import kmp 
import os

# Directorio del codigo malicioso
m_directory = "./Mcode0"

# Directorio de las transmisiones
t_directory = "./Transmissions0"

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


for t_file in os.listdir(t_directory): # Almacenando todas las transmisiones
    f = os.path.join(t_directory, t_file)
    
    if os.path.isfile(f) and t_file.endswith('.txt'):
        with open (f, 'r') as file:
            string = ""

            for line in file:
                string += line.strip()
                
            transmission.append(string)


with open ("output0.txt", 'w') as out:
    for t_index, t in enumerate(transmission):
        out.write("\nArchivo de transmisión " + str(t_index + 1) + "\n")
        out.write(t + "\n")


    for m_index, m in enumerate(malicious):
        out.write("\nArchivo mcode" + str(m_index + 1) + "\n")
        out.write(m + "\n")
    

    for t_index, t in enumerate(transmission):
        out.write("\n T R A N S M I S S I O N " + str(t_index + 1) + "\n\n")
        

        for m_index, m in enumerate(malicious):
            out.write("mcode " + str(m_index + 1) + "\n")
            coincidences = kmp(t, m)

            if len(coincidences) > 0:
                for c in coincidences:
                    out.write("(true) ")
                    out.write("Posición inicial: " + str(c) + " ")
                    out.write("Posición final: " + str(c + len(m) - 1) + "\n")
                    #out.write("PRUEBA " + t[c:c+len(m)] + "\n") # ESTA LÍNEA ES PARA VALIDAR
            
            else:
                out.write("(false) Cadena no encontrada en la transmisión" + "\n")
            
            out.write("\n")
        


        (palindrome, index) = Manacher(t)

        if len(palindrome) > 1:
            out.write("Código espejeado: " + palindrome + "\n")
            #out.write("PRUEBA " + t[index:index+len(palindrome)] + "\n") # ESTA LÍNEA ES PARA VALIDAR
            out.write("Posición inicial: " + str(index) + " ")
            out.write("Posición final: " + str(index + len(palindrome) - 1) + "\n\n")
        
        else:
            out.write("No se encontró código espejeado en el archivo de transmisión\n\n")
        

        for tr_index, tr in enumerate(transmission):
            if tr_index != t_index:
                out.write("transmission " + str(tr_index + 1) + "\n")
                
                substr = longest_substr(t, tr)
                if substr == " ":
                    out.write("No se encontraron coincidencias\n\n")
                else:
                    out.write("Substring más largo: " + substr + "\n\n")
