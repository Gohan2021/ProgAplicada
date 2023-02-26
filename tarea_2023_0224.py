#Nicolás Moreno Ovalle - 20212005140
#Diccionario que organiza 20 componentes electrónicos con 3 niveles
import json
componentes_electronicos = [{
  "Pasivos": {
    "Resistencias": {
      "Tipo": { 
        "resistencia":["de película de carbón, de película metálica"]
      },
      "Uso": "Limitación de corriente, división de voltaje,                       generación de calor",
      "Tolerancia": {
        "Precisión": ["Alta", "Media", "Baja"],
        "Tolerancia a la temperatura": ["Alta", "Media", "Baja"],
        "Tolerancia al ruido": ["Alta", "Media", "Baja"]
        }
    },
    "Capacitores": {  
      "Tipo": { 
        "capacitor":["Cerámico, electrolitico, poliéster"]
      },
      "Uso": "Almacenamiento de energía eléctrica, filtrado de                    señales",
      "Tolerancia": {
        "Precisión": ["Alta", "Media", "Baja"],
        "Tolerancia a la temperatura": ["Alta", "Media", "Baja"],
        "Tolerancia a la frecuencia": ["Alta", "Media", "Baja"]
        }
    },
    "Inductores": {
      "Tipo": { 
        "inductor":["de núcleo de aire, de núcleo de ferrita, de núcleo de          polvo de hierro"]
      },
      "Uso": "Filtro de señales, almacenamiento de energía                        magnética",
      "Tolerancia": {
        "Precisión": ["Alta", "Media", "Baja"],
        "Tolerancia a la temperatura": ["Alta", "Media", "Baja"],
        "Tolerancia a la frecuencia": ["Alta", "Media", "Baja"]
        }
    },
    "Potenciometros": {
      "Tipo": "de película de carbón",
      "Uso": "Control de volumen, brillo, tono",
      "Tolerancia": {
        "Precisión": ["Alta", "Media", "Baja"],
        "Tolerancia a la temperatura": ["Alta", "Media", "Baja"],
        "Tolerancia al ruido": ["Alta", "Media", "Baja"]
        }
    },
  },
  "Activos": {
    "Diodos": {
      "Tipo": { 
        "Diodo":["LED, rectificador, zener"]
      },
      "Uso": "Rectificación de señales, protección de polaridad",
      "Tolerancia": {
        "Tensión directa": ["Alta", "Media", "Baja"],
        "Tolerancia a la temperatura": ["Alta", "Media", "Baja"],
        "Tolerancia a la frecuencia": ["Alta", "Media", "Baja"]
      }
    },
    "Transistores": {
      "Tipo": { 
        "Transistor":["bipolar de unión(BJT), efecto de campo(FET),                efecto de campo con compuerta aislada(IGBT),MOSFET"]
      },
      "Uso": "Amplificación, conmutación, control de potencia",
      "Tolerancia": {
        "Ganancia de corriente": ["Alta", "Media", "Baja"],
        "Tolerancia a la temperatura": ["Alta", "Media", "Baja"],
        "Tolerancia al ruido": ["Alta", "Media", "Baja"]
      }
    },
    "Amplificadores": {
      "Tipo": { 
        "Amplificador":["Operacional, de potencia"]
      },
      "Uso": "Amplificación de señales, sumador, diferenciador",
      "Tolerancia": {
        "Ganancia de voltaje": ["Alta", "Media", "Baja"],
        "Tolerancia a la temperatura": ["Alta", "Media", "Baja"],
        "Tolerancia al ruido": ["Alta", "Media", "Baja"]
        }
    },
    "Tiristor": {
      "Tipo": "Tirisitor(SCR)",
      "Uso": " Control de potencia, conmutación de corriente",
      "Tolerancia": {
        "Tensión de bloqueo": ["Alta", "Media", "Baja"],
        "Tolerancia a la corriente": ["Alta", "Media", "Baja"],
        "Tolerancia a la temperatura": ["Alta", "Media", "Baja"]
        }
    },
    "Circuitos integrados": {
      "Tipo": "Circuitos integrados digitales (CI)",
      "Uso": "Procesamiento de señales digitales, memoria",
      "Tolerancia": {
        "Velocidad de operación": ["Alta", "Media", "Baja"],
        "Tolerancia a la temperatura": ["Alta", "Media", "Baja"],
        "Tolerancia al ruido": ["Alta", "Media", "Baja"]
        }
    }
  },
}]
print(componentes_electronicos)

with open('componentes_electronicos.json', 'w',) as archivo:
   json.dump(componentes_electronicos,archivo)

with open('componentes_electronicos.json', 'r', encoding="utf-8") as archivo:
  componentes_electronicos_leida = json.load(archivo)
componentes_electronicos_leida