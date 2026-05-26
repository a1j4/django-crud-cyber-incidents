# 📄 SECURITY.md — CyberLab Incident Tracker

## 🎓 Universidad Laica Eloy Alfaro de Manabí

**Curso:** Ethical Hacking
**Práctica:** Django Authentication & Security Hardening

---

# 🔐 Q0. ¿Por qué un sistema de incidentes sin autenticación es un problema de seguridad?

Un sistema de gestión de incidentes sin autenticación permite que cualquier usuario acceda, modifique o elimine información sensible.
Esto representa una vulnerabilidad crítica porque expone datos internos del sistema, permite manipulación de registros y rompe la confidencialidad, integridad y disponibilidad de la información.

En un entorno real, esto podría permitir ataques como:

* modificación de incidentes sin autorización
* eliminación de registros críticos
* filtración de información sensible

---

# 👤 Q1. Diferencia entre User y UserProfile + uso de OneToOneField

Django proporciona un modelo `User` que maneja autenticación básica (username, password, email).

Sin embargo, para agregar información adicional como roles, se creó el modelo `UserProfile`.

### Diferencia:

* **User:** autenticación base (login, password)
* **UserProfile:** información extendida (roles, bio, permisos)

### ¿Por qué OneToOneField?

Se utiliza `OneToOneField` porque:

* cada usuario tiene exactamente un perfil
* mantiene separación entre autenticación y datos adicionales
* evita modificar el modelo base de Django

---

# Q2. ¿Qué es el parámetro ?next= y cuál es su riesgo?

El parámetro `next=` indica a qué página debe redirigirse el usuario después de iniciar sesión.

Ejemplo:

```
/accounts/login/?next=/incidents/
```

### Riesgo de seguridad:

Si no se valida correctamente, puede permitir **Open Redirect**, donde un atacante redirige al usuario a sitios maliciosos después del login.

---

#  Q3. Autenticación vs Autorización

### Autenticación:

Es el proceso de verificar la identidad del usuario.

✔ Ejemplo en el laboratorio:

* login con username y password

### Autorización:

Es el proceso de determinar qué acciones puede realizar un usuario.

✔ Ejemplo en el laboratorio:

* Analyst: solo puede ver y crear incidentes
* Admin: puede editar y eliminar incidentes

### Riesgo si falta autorización:

Aunque el usuario esté autenticado, podría acceder a funciones administrativas no permitidas.

---

# Q4. ¿Por qué usamos commit=False y qué riesgo evita?

En Django:

```python
incident = form.save(commit=False)
```

Esto permite modificar el objeto antes de guardarlo en la base de datos.

### Uso en el laboratorio:

Se usa para asignar automáticamente:

```python
incident.reported_by = request.user
```

### Riesgo si no se usa:

Si se permitiera enviar `reported_by` desde el formulario:

* un atacante podría falsificar el creador del incidente
* se produce un ataque de **Mass Assignment**

---

# Q5. ¿Por qué ocultar botones en templates NO es seguridad?

Ocultar botones en HTML solo afecta la interfaz visual, pero no la seguridad real.

Un atacante puede:

* acceder directamente a URLs como `/edit/` o `/delete/`
* usar herramientas como Postman o curl

### Solución real implementada:

La seguridad se aplica en las vistas:

```python
if not profile.is_admin():
    return HttpResponseForbidden()
```

✔ Esto garantiza control real del acceso.

---

# Q6. Brute Force y protección con django-axes

### ¿Qué es un ataque de fuerza bruta?

Es un ataque donde se intentan múltiples combinaciones de usuario y contraseña hasta encontrar una válida.

### Mitigación con django-axes:

Se utiliza `django-axes` para:

* limitar intentos fallidos de login
* bloquear temporalmente IPs sospechosas

### Configuración usada:

* AXES_FAILURE_LIMIT = 5

### Trade-off:

Si el límite es muy bajo:

* usuarios legítimos pueden ser bloqueados accidentalmente

---

### Otras medidas de seguridad:

* rate limiting
* CAPTCHA
* bloqueo por IP
* autenticación multifactor (MFA)

---

# 🔐 CONCLUSIÓN

El sistema implementa un enfoque de **defense-in-depth**, combinando:

* autenticación segura
* autorización por roles
* protección de vistas
* validación de formularios
* prevención de ataques comunes


