# -*- coding: utf-8 -*- 
"""
Created on Thu Oct 17 16:58:04 2024

@author: Mateo Velásquez - Galo Estrella - 
"""

import shutil
import os
import csv

# Definir las rutas de los directorios que van a reemplazar a los servidores sftp
entrada_path = r"C:\Users\maten\OneDrive\Escritorio\Universidad\Integración de Sistemas\Servidor Compartido"
procesamiento_path = r"C:\Users\maten\OneDrive\Escritorio\Universidad\Integración de Sistemas\Servidor Consultora"
salida_path = r"C:\Users\maten\OneDrive\Escritorio\Universidad\Integración de Sistemas\Servidor Compartido"

# Verificar y crear el directorio de salida si no existe
os.makedirs(salida_path, exist_ok=True)

# Generación del archivo csv del reclamo a la aseguradora
def generar_archivo_reclamo(numero_poliza, monto, fecha, descripcion):
    archivo_nombre = f'reclamo_{numero_poliza}.csv'
    archivo_path = os.path.join(entrada_path, archivo_nombre)
    
    # Verificar y crear el directorio de entrada si no existe
    os.makedirs(entrada_path, exist_ok=True)
    
    with open(archivo_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Número de Póliza', 'Monto', 'Fecha', 'Descripción'])
        writer.writerow([numero_poliza, monto, fecha, descripcion])
        
    print(f"Archivo de reclamo generado: {archivo_path}")
    

# Generar archivos de reclamos
generar_archivo_reclamo('12345', 9500, '2024-10-17', 'Daño por inundación')
generar_archivo_reclamo('54321', 1500, '2024-09-30', 'Incendio')


# Transferir archivos de entrada a procesamiento
def transferir_archivo_entrada_a_procesamiento():
    archivos = os.listdir(entrada_path)
    for archivo in archivos:
        shutil.move(os.path.join(entrada_path, archivo), procesamiento_path)
        print(f"Archivo '{archivo}' transferido al directorio de procesamiento.")

# Verificar y crear el directorio de procesamiento si no existe
os.makedirs(procesamiento_path, exist_ok=True)

transferir_archivo_entrada_a_procesamiento()


# Procesamiento de Siniestros
def procesar_siniestros():
    resultados = []
    archivos_procesados = os.listdir(procesamiento_path)

    for archivo in archivos_procesados:
        with open(os.path.join(procesamiento_path, archivo), mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                numero_poliza = row['Número de Póliza']
                monto = float(row['Monto'])
                # Validación del siniestro (puedes ajustar la lógica según tus necesidades)
                if monto <= 10000:
                    resultado = 'Aprobado'
                else:
                    resultado = 'Rechazado'
                
                resultados.append({
                    'Número de Póliza': numero_poliza,
                    'Resultado': resultado
                })

    # Generar archivo CSV de resultados
    generar_archivo_resultados(resultados)


def generar_archivo_resultados(resultados):
    archivo_nombre = 'resultados_validacion.csv'
    archivo_path = os.path.join(salida_path, archivo_nombre)
    
    with open(archivo_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Número de Póliza', 'Resultado'])
        for resultado in resultados:
            writer.writerow([resultado['Número de Póliza'], resultado['Resultado']])
    
    print(f"Archivo de resultados generado: {archivo_path}")


# Llamar a la función para procesar siniestros
procesar_siniestros()
