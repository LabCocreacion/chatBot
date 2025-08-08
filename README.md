# Chatbot Instituto Nacional de Cancerología 🤖

Un asistente conversacional inteligente desarrollado para el **Laboratorio de Co-creación para la Innovación del Instituto Nacional de Cancerología**, utilizando tecnología de OpenAI GPT-4o-mini.

## 📋 Descripción

Este proyecto implementa una API REST que permite interacciones conversacionales con un asistente de IA especializado en brindar información y apoyo relacionado con el Instituto Nacional de Cancerología. El chatbot está diseñado para responder de manera clara, profesional y útil a las consultas de los usuarios.

### ✨ Características Principales

- 🚀 **API REST rápida y eficiente** basada en Flask
- 🧠 **Integración con OpenAI GPT-4o-mini** para procesamiento de lenguaje natural
- 🌐 **CORS habilitado** para integración con aplicaciones frontend
- 🏗️ **Arquitectura modular** con separación clara de responsabilidades
- ⚡ **Configuración simple** con variables de entorno
- 🛡️ **Manejo robusto de errores** y validación de entrada

## 🛠️ Tecnologías Utilizadas

- **Python 3.12** - Lenguaje de programación principal
- **Flask 3.1.1** - Framework web ligero
- **OpenAI 1.90.0** - SDK para integración con OpenAI API
- **Flask-CORS 6.0.1** - Manejo de Cross-Origin Resource Sharing
- **python-dotenv 1.1.0** - Gestión de variables de entorno

## 📁 Estructura del Proyecto

```
chatBot/
├── app/
│   ├── __init__.py          # Factory pattern y configuración de Flask
│   ├── openai_service.py    # Servicio de integración con OpenAI
│   └── routes.py            # Definición de endpoints REST
├── config.py                # Configuraciones del proyecto
├── requirements.txt         # Dependencias de Python
├── run.py                   # Punto de entrada de la aplicación
├── README.md               # Documentación del proyecto
└── MANUAL_TECNICO.md       # Manual técnico detallado
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior (recomendado Python 3.12)
- pip (gestor de paquetes de Python)
- Una API key válida de OpenAI

### 1. Clonar el repositorio

```bash
git clone https://github.com/LabCocreacion/chatBot.git
cd chatBot
```

### 2. Crear y activar entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```bash
OPENAI_API_KEY=tu_clave_de_openai_aqui
```

### 5. Ejecutar la aplicación

```bash
python run.py
```

La aplicación estará disponible en: `http://localhost:5003`

## 📡 Uso de la API

### Endpoint Principal

**POST** `/chat`

Procesa mensajes de usuario y retorna respuestas del chatbot.

#### Request

```http
POST /chat HTTP/1.1
Content-Type: application/json

{
  "message": "¿Qué servicios ofrece el laboratorio?"
}
```

#### Response (Éxito)

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "response": "El Laboratorio de Co-creación para la Innovación del Instituto Nacional de Cancerología ofrece diversos servicios..."
}
```

#### Response (Error)

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": "Falta el mensaje"
}
```

### Ejemplo con cURL

```bash
curl -X POST http://localhost:5003/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola, ¿cómo puedes ayudarme?"}'
```

### Ejemplo con JavaScript (Fetch)

```javascript
const response = await fetch('http://localhost:5003/chat', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: '¿Cuáles son los horarios de atención?'
  })
});

const data = await response.json();
console.log(data.response);
```

### Ejemplo con Python (requests)

```python
import requests

response = requests.post('http://localhost:5003/chat', 
  json={'message': '¿Cómo puedo obtener más información?'})

if response.status_code == 200:
    print(response.json()['response'])
else:
    print(f"Error: {response.json()['error']}")
```

## 🐳 Despliegue con Docker

### Crear Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5003

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5003", "run:app"]
```

### Construir y ejecutar

```bash
# Construir imagen
docker build -t chatbot-inc .

# Ejecutar contenedor
docker run -p 5003:5003 -e OPENAI_API_KEY=tu_clave_aqui chatbot-inc
```

## 🔧 Configuración Avanzada

### Variables de Entorno

| Variable | Descripción | Requerida | Valor por defecto |
|----------|-------------|-----------|-------------------|
| `OPENAI_API_KEY` | Clave de API de OpenAI | ✅ Sí | - |
| `FLASK_ENV` | Entorno de Flask | ❌ No | development |
| `PORT` | Puerto del servidor | ❌ No | 5003 |

### Configuración de Producción

Para entornos de producción, considera:

1. **Usar un servidor WSGI robusto:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5003 run:app
```

2. **Configurar CORS específico:**
```python
# En app/__init__.py
CORS(app, origins=["https://tu-dominio.com"])
```

3. **Implementar rate limiting:**
```bash
pip install Flask-Limiter
```

## 🧪 Testing

### Ejecutar pruebas básicas

```bash
# Verificar que el servidor responde
curl -X POST http://localhost:5003/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "test"}'

# Verificar endpoint de salud (si está implementado)
curl http://localhost:5003/health
```

### Pruebas de carga

```bash
# Usando Apache Bench
ab -n 100 -c 10 -T 'application/json' \
  -p test_data.json http://localhost:5003/chat
```

## 📊 Monitoreo y Logs

### Habilitar logs detallados

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Métricas importantes a monitorear

- ⏱️ Tiempo de respuesta por request
- 📈 Volumen de requests por minuto
- 🚨 Tasa de errores
- 💰 Uso de tokens de OpenAI
- 🖥️ Uso de memoria y CPU

## 🔍 Troubleshooting

### Problemas comunes

#### ❌ Error: "OpenAI API key not found"
```bash
# Verificar variable de entorno
echo $OPENAI_API_KEY

# Configurar correctamente
export OPENAI_API_KEY=tu_clave_aqui
```

#### ❌ Error: "ModuleNotFoundError: No module named 'openai'"
```bash
# Reinstalar dependencias
pip install -r requirements.txt
```

#### ❌ Error de CORS
```python
# Configurar CORS en app/__init__.py
from flask_cors import CORS
CORS(app, origins=["http://localhost:3000"])
```

### Logs de depuración

Para habilitar modo debug:

```python
# En run.py
if __name__ == "__main__":
    app.run(debug=True, port=5003)
```

## 🤝 Contribuir

### Pasos para contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

### Estándares de código

- Seguir PEP 8 para Python
- Documentar funciones y clases
- Incluir tests para nuevas funcionalidades
- Mantener la cobertura de tests

## 📚 Documentación Adicional

- [Manual Técnico Completo](MANUAL_TECNICO.md) - Documentación técnica detallada
- [OpenAI API Documentation](https://platform.openai.com/docs) - Documentación oficial de OpenAI
- [Flask Documentation](https://flask.palletsprojects.com/) - Documentación de Flask

## 📋 Roadmap

### Próximas funcionalidades

- [ ] 🔐 Sistema de autenticación
- [ ] 📝 Logging estructurado
- [ ] 🗄️ Persistencia de conversaciones
- [ ] 📊 Dashboard de métricas
- [ ] 🧪 Suite de tests automatizados
- [ ] 🌐 Interfaz web frontend
- [ ] 🔄 Sistema de caché con Redis
- [ ] 📱 API móvil optimizada

## ❓ FAQ

### ¿Cómo obtengo una API key de OpenAI?
Visita [platform.openai.com](https://platform.openai.com/) y crea una cuenta. En la sección de API keys, genera una nueva clave.

### ¿Puedo usar otros modelos de OpenAI?
Sí, puedes modificar el modelo en `app/openai_service.py` cambiando `gpt-4o-mini` por otro modelo disponible.

### ¿El chatbot almacena las conversaciones?
Actualmente no, cada request es independiente. La persistencia está planificada para futuras versiones.

### ¿Cómo cambio el puerto del servidor?
Modifica el puerto en `run.py` o usa la variable de entorno `PORT`.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Kevin Steven Pérez** - Ingeniero de Sistemas  
Laboratorio de Co-creación para la Innovación  
Instituto Nacional de Cancerología

---

## 🏥 Sobre el Instituto Nacional de Cancerología

El Instituto Nacional de Cancerología es una institución líder en Colombia dedicada a la prevención, diagnóstico, tratamiento e investigación del cáncer. El Laboratorio de Co-creación para la Innovación trabaja en el desarrollo de soluciones tecnológicas innovadoras para mejorar la atención médica y la experiencia de los pacientes.

---

⭐ Si este proyecto te resulta útil, ¡considera darle una estrella en GitHub!

📞 Para soporte técnico o consultas, contacta al equipo de desarrollo del Laboratorio de Co-creación.
