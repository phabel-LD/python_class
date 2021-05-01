
## Abrir archivo como lectura con open("","r+")
data = open("../Listas_y_loops/4_dna_sequences.txt", "r+") ## Recordar comprobar la ruta del archivo input.

lines = data.readlines() ## Leer cada linea.

data.close() ## Cerrar el archivo, pues ya no es necesario.

file = open("dna_sequences.fasta", "w") ## Crear el archivo output.

for line in lines: ## Iterar sobre cada linea y anexar lo necesario al nuevo archivo fasta
    file.write(">" + line[:5] + "\n") ## Escribir encabezado
    line = line.upper() ## Asegurarse que todos los nucleotidos sean mayusculas.
    line = line.replace('-', '') ## Eliminar gaps.
    line = line.replace('"', '') ## Eliminar comillas
    ## print(line)  ## Este es un buen checkpoint para revisar el output
    file.write(line[8:]) ## Escribir la secuencia en otro renglon.

file.close() ## Cerrar el archivo output: fasta
