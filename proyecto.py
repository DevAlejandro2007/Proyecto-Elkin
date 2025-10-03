"""
EL PROYECTO ES:

Simular una entidad financiera que gestiona creditos estudiantiles {puede ser propia de la U 
o tambien puede ser externa, la idea es implementar todos los tipos de bases de datos que hemos 
utilizado hasta la fecha}

"""

print("Alejandro Rojas Benitez")
print("Johan Yesid Tavera Zapata")
print("Jose Manuel Mesa Ospina")

import numpy as np

np.random.seed(42)
n_samples = 200

Id_estudiante = np.arange(1, n_samples+1)
Edad = np.random.randint(18, 40, n_samples)
Carrera = np.random.choice([1, 2, 3, 4, 5], n_samples, p=[0.6, 0.2, 0.10, 0.05, 0.05])
# 1=Veterinaria, 2=Ingeniería, 3=Administración, 4=Derecho, 5=Psicología
Semestre_actual = np.random.randint(2, 10, n_samples)
Promedio = np.round(np.random.uniform(3.5, 5.0, n_samples), 2)
Ingresos_mensuales_familia = np.random.randint(1600000, 5000000, n_samples)
Valor_credito_solicitado = np.random.randint(3000000, 30000000, n_samples)
Tasa_interés = np.round(np.random.uniform(0.8, 2.0, n_samples), 2)
Garantía = np.random.choice([1, 2], n_samples, p=[0.5, 0.5])
Plazo = np.random.randint(24, 60, n_samples)
Cuota_mensual = (Valor_credito_solicitado * (1 + (Tasa_interés/100)*Plazo)) // Plazo
Monto_pagado = np.random.randint(0, Valor_credito_solicitado//2, n_samples)
Saldo_pendiente = Valor_credito_solicitado - Monto_pagado
