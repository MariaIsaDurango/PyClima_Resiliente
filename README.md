# PyClima Resiliente 🌦️

**Sistema Avanzado de Monitoreo Climático con Detección Inteligente de Riesgos**

Aplicación de consola Python desarrollada como parte del Bootcamp AI4Inclusion para el Ayuntamiento de Madrid, con foco en la experiencia del usuario (UX) y la detección automática de situaciones de riesgo climático.

Aporta datos al Departamento de Resiliencia Urbana y Smart City del Ayuntamiento para activar protocolos de emergencia.

## 📋 Tabla de Contenidos

- [Características Principales](#características-principales)
- [Instalación](#instalación)
- [Cómo Usar](#cómo-usar)
- [Sistema de Alertas](#sistema-de-alertas)
- [Estructura del Proyecto](#estructura-del-proyecto)

## ✨ Características Principales

### 1. **Interfaz Intuitiva**
- Menú principal claro y navegable
- Indicadores visuales para orientar al usuario
- Mensajes de error comprensibles sin crashes

### 2. **Registro Robusto de Datos**
- Captura validada de: Fecha, Zona, Temperatura, Humedad, Viento, Lluvia
- Validación automática contra distritos oficiales de Madrid
- Confirmación antes de guardar
- Prevención de duplicados

### 3. **Sistema de Alertas Inteligente** ⚠️

Detección automática de **3 tipos principales de riesgos**:

#### 🔴 **Calor Extremo**
- Nivel Crítico: > 45°C
- Nivel Alto: > 40°C

#### 🔴 **Viento Peligroso**
- Nivel Crítico: > 70 km/h
- Nivel Alto: > 50 km/h

#### 🟡 **Lluvia/Humedad Anómala**
- Lluvia activa
- Humedad muy alta (> 95%)
- Humedad muy baja (< 20%)

### 4. **Consulta y Análisis**
- Filtrado por zona/distrito
- Visualización de histórico completo
- Listados organizados

## 🚀 Instalación Rápida

### 1. Crear entorno virtual
```bash
python -m venv .venv
```

### 2. Activar entorno (Windows PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar aplicación
```bash
python main.py
```

## 📖 Cómo Usar

### Menú Principal
```
1. Registrar Nuevos Datos Climáticos
2. Consultar Datos por Zona
3. Ver Histórico Completo
4. Ver Alertas Activas
5. Salir del Sistema
```

### Flujo de Registro
1. Ingresa fecha (DD/MM/AAAA)
2. Selecciona zona (21 distritos de Madrid)
3. Captura datos: temperatura, humedad, viento, lluvia
4. Revisa resumen
5. Sistema analiza alertas automáticamente
6. Confirma guardado en JSON

El sistema **nunca falla** con inputs inválidos - solo pide reintentar.

## ⚠️ Sistema de Alertas

### Análisis Inteligente
- Detecta automáticamente condiciones de riesgo
- Genera alertas visuales e informativas
- Sugiere acciones recomendadas

### Umbrales Configurables
Edita en `validaciones.py`:
```python
UMBRAL_TEMP_CALOR = 40.0      # °C
UMBRAL_VIENTO_ALTO = 50.0     # km/h
UMBRAL_HUMEDAD_BAJA = 20.0    # %
UMBRAL_HUMEDAD_ALTA = 95.0    # %
```

## 📁 Estructura del Proyecto

```
PyClima_Resiliente/
├── main.py              # Interfaz de usuario (DEV 4)
├── persistencia.py      # Lógica JSON (DEV 3)
├── validaciones.py      # Alertas y validaciones (DEV 4)
├── config.json         # Distritos de Madrid
├── datos_clima.json    # Base de datos
├── requirements.txt    # Dependencias
└── README.md          # Este archivo
```

## 👥 Desarrollo

**DEV 4: Interfaz + Alertas**
- Interfaz de consola
- Sistema de detectores de riesgo
- Validación robusta
- Experiencia del usuario

**DEV 3: Persistencia JSON**
- Lectura/escritura
- Validación de duplicados

**DEV 1: Lógica**
- Coordinación general

## 🧪 Testing

```bash
# Test simple
python test_simple.py

# Suite completa
python test_alertas.py
```

## 📝 Estado

- ✅ Interfaz completa
- ✅ Sistema de alertas (3 tipos de riesgos)
- ✅ Validación robusta
- ✅ Testing básico
- ⏳ Integración con DEV 1

---

**Versión**: 1.0  
**Fecha**: 3 de Abril de 2026  
**Bootcamp**: AI4Inclusion - Ayuntamiento de Madrid
