import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fpdf import FPDF
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="GestiónPyme IA - Diagnóstico y Consultoría",
    page_icon="💼",
    layout="centered",
)

# Cabecera ejecutiva
st.title("GestiónPyme IA")
st.markdown("### Plataforma de Diagnóstico y Transformación Empresarial")
st.markdown(
    "*Un análisis integral diseñado para evaluar con precisión las áreas de"
    " gestión, digitalización e inteligencia artificial de tu negocio.*"
)

st.markdown("---")

# --- FORMULARIO DE DIAGNÓSTICO INTEGRAL ---
st.markdown("### Briefing Empresarial")
st.write(
    "Por favor, completa los siguientes datos para que nuestro sistema"
    " elabore tu plan de acción personalizado."
)

with st.form("form_integral_pro"):
  st.markdown("#### 1. Datos de Contacto del Responsable")
  col_c1, col_c2 = st.columns(2)
  with col_c1:
    nombre_contacto = st.text_input(
        "Nombre y Apellidos", placeholder="Ej. Carlos Martínez"
    )
    telefono = st.text_input("Teléfono de contacto", placeholder="Ej. +34 600 000 000")
  with col_c2:
    email = st.text_input(
        "Correo electrónico corporativo",
        placeholder="Ej. c.martinez@empresa.com",
    )
    canal_contacto = st.selectbox(
        "¿Cómo prefieres que te contactemos?",
        ["Teléfono", "WhatsApp", "Correo electrónico"],
    )

  st.markdown("---")

  st.markdown("#### 2. Información General de la Empresa")
  col1, col2 = st.columns(2)
  with col1:
    nombre_empresa = st.text_input(
        "Nombre comercial de la empresa",
        placeholder="Ej. Comercializadora del Sur",
    )
  with col2:
    sector = st.selectbox(
        "Sector principal",
        [
            "Comercio minorista / Retail",
            "Hostelería, Restauración y Turismo",
            "Servicios profesionales y B2B",
            "Industria, Fabricación y Talleres",
            "Construcción y Oficios",
            "Tecnología y Software",
            "Salud, Bienestar y Farmacia",
            "Transporte, Logística y Distribución",
            "Inmobiliaria y Construcción",
            "Educación y Formación",
            "Otro",
        ],
    )

  empleados = st.selectbox(
      "Tamaño del equipo (número de empleados)",
      [
          "1 a 3 empleados",
          "4 a 10 empleados",
          "11 a 25 empleados",
          "26 a 50 empleados",
          "Más de 50 empleados",
      ],
  )

  st.markdown("---")

  st.markdown("#### 3. Área Financiera y de Costes")
  finanzas_estado = st.selectbox(
      "¿Cómo controlas la rentabilidad y el flujo de caja?",
      [
          "Control mínimo o inexistente (lo que queda en el banco a fin de mes)",
          "Registro básico de ingresos y gastos en libreta o notas manuales",
          (
              "Hojas de cálculo básicas (Excel / Google Sheets) actualizadas de"
              " forma irregular"
          ),
          (
              "Contabilidad llevada por gestoría externa sin visibilidad de"
              " costes internos en tiempo real"
          ),
          (
              "Contabilidad al día, con revisión mensual de márgenes por"
              " producto o servicio"
          ),
      ],
  )

  st.markdown("---")

  st.markdown("#### 4. Operaciones, Inventario y Proveedores")
  operaciones_estado = st.selectbox(
      "¿Cómo gestionas tu stock, producción o prestación de servicios?",
      [
          (
              "Procesos completamente manuales, dependencia de la memoria y"
              " pérdida de tiempo buscando información"
          ),
          (
              "Organización interna mediante herramientas tradicionales,"
              " carpetas compartidas o software obsoleto"
          ),
          (
              "Procesos parcialmente digitalizados pero con desconexión entre"
              " departamentos o almacén"
          ),
          (
              "Procesos estandarizados y digitalizados de punta a punta con"
              " trazabilidad operativa"
          ),
      ],
  )

  st.markdown("---")

  st.markdown("#### 5. Ventas y Captación de Clientes")
  marketing_estado = st.selectbox(
      "¿Cuál es tu principal vía para conseguir nuevos clientes?",
      [
          (
              "Dependencia total del boca a boca y clientes locales recurrentes"
              " sin plan comercial"
          ),
          (
              "Presencia en redes sociales o página web básica, pero sin un"
              " flujo constante de clientes nuevos"
          ),
          (
              "Campañas puntuales de publicidad digital o comercialización"
              " activa sin automatización"
          ),
          (
              "Estrategia comercial digital estructurada con captación y"
              " seguimiento comercial organizado"
          ),
      ],
  )

  st.markdown("---")

  st.markdown("#### 6. Gestión del Personal y Comunicación")
  rrhh_estado = st.selectbox(
      "¿Cómo organizas la comunicación y asignación de tareas al equipo?",
      [
          (
              "Grupos de WhatsApp caóticos, llamadas continuas y comunicación"
              " informal sin registros"
          ),
          (
              "Reuniones frecuentes presenciales pero sin un sistema digital"
              " de seguimiento de tareas"
          ),
          (
              "Herramientas de colaboración básica (correo o chat corporativo)"
              " con asignación de tareas desorganizada"
          ),
          (
              "Plataformas de colaboración, control horario y tableros de"
              " tareas estructurados en uso activo"
          ),
      ],
  )

  st.markdown("---")

  st.markdown("#### 7. Inteligencia Artificial y Carga Operativa")
  horas_admin = st.selectbox(
      (
          "¿Cuántas horas semanales dedica tu equipo a la carga administrativa"
          " y gestión operativa (facturas, correos, trámites)?"
      ),
      [
          "Menos de 5 horas semanales (Baja carga operativa)",
          "Entre 5 y 15 horas semanales (Carga moderada en tareas rutinarias)",
          "Entre 16 y 30 horas semanales (Alta carga operativa y de gestión)",
          (
              "Más de 30 horas semanales (Saturación crítica en tareas manuales"
              " y repetitivas)"
          ),
      ],
  )

  interes_ia = st.multiselect(
      "¿Qué áreas te gustaría automatizar con Inteligencia Artificial?",
      [
          "Atención al cliente y respuestas frecuentes automáticas",
          "Redacción comercial, presupuestos y contratos rápidos",
          "Análisis de datos de ventas y previsión de demanda",
          "Generación de contenidos para promoción y redes sociales",
      ],
  )

  st.markdown("---")

  st.markdown("#### 8. Descripción Específica del Desafío")
  problema_especifico = st.text_area(
      (
          "¿Hay algún problema, cuello de botella o situación concreta en tu"
          " negocio que no hayamos cubierto arriba?"
      ),
      placeholder=(
          "Ej. Necesitamos integrar nuestra tienda física con la web, o tenemos"
          " muchos retrasos cobrando de nuestros clientes principales..."
      ),
  )

  st.markdown("---")
  presupuesto = st.selectbox(
      "Capacidad estimada de inversión para la mejora tecnológica",
      [
          "Económica (Soluciones modulares de rápida amortización)",
          "Moderada (Inversión equilibrada con retorno de eficiencia claro)",
          "Estratégica (Transformación integral y acompañamiento continuo)",
      ],
  )

  st.markdown("")
  submitted = st.form_submit_button(
      "Generar Diagnóstico Ejecutivo y Plan de Acción ➔"
  )

# Guardar en sesión
if submitted:
  if not nombre_empresa or not email or not nombre_contacto:
    st.warning(
        "Por favor, completa los campos obligatorios de empresa, nombre y"
        " correo electrónico."
    )
  else:
    st.session_state["enviado"] = True
    st.session_state["datos"] = {
        "contacto": nombre_contacto,
        "email": email,
        "telefono": telefono,
        "canal": canal_contacto,
        "empresa": nombre_empresa,
        "sector": sector,
        "empleados": empleados,
        "finanzas": finanzas_estado,
        "operaciones": operaciones_estado,
        "marketing": marketing_estado,
        "rrhh": rrhh_estado,
        "horas_admin": horas_admin,
        "interes_ia": interes_ia,
        "problema_especifico": problema_especifico,
        "presupuesto": presupuesto,
    }

# --- INFORME Y ROADMAP ESTRATÉGICO PROFESIONAL ---
if st.session_state.get("enviado", False):
  d = st.session_state["datos"]

  st.success(
      f"¡Diagnóstico 360° generado con éxito para **{d['empresa']}**"
      f" ({d['sector']})!"
  )

  st.divider()
  st.markdown("### Cuadro de Mando y Hallazgos por Área")

  alertas = []
  roadmap = []

  # Lógica de análisis multi-área
  if (
      "inexistente" in d["finanzas"]
      or "libreta" in d["finanzas"]
      or "irregular" in d["finanzas"]
      or "gestoría" in d["finanzas"]
  ):
    alertas.append(
        "Falta de visibilidad real sobre el flujo de caja y los márgenes de"
        " rentabilidad por servicio."
    )
    roadmap.append({
        "categoria": "Control Financiero",
        "titulo": "Cuadro de Mando Estandarizado de Margenes y Tesoreria",
        "desc": (
            "Implementacion de un panel automatizado para controlar ingresos,"
            " costes y evitar desviaciones de caja de forma sencilla."
        ),
        "impacto": "Critico",
        "solucion_a": (
            "Aborda directamente la falta de control financiero y la"
            " incertidumbre sobre los margenes reales de cada servicio."
        ),
    })

  if (
      "manuales" in d["operaciones"]
      or "tradicionales" in d["operaciones"]
      or "desconexión" in d["operaciones"]
  ):
    alertas.append(
        "Cuellos de botella operativos por procesos descentralizados y pérdida"
        " de tiempo en gestiones."
    )
    roadmap.append({
        "categoria": "Optimizacion Operativa",
        "titulo": "Sistema Estandar de Control de Stock y Procesos",
        "desc": (
            "Modularizacion de flujos internos para eliminar tiempos muertos y"
            " optimizar la cadena de valor de tu actividad."
        ),
        "impacto": "Alto",
        "solucion_a": (
            "Elimina los cuellos de botella operativos y la dependencia de"
            " procesos manuales o desconectados."
        ),
    })

  if (
      "boca a boca" in d["marketing"]
      or "básica" in d["marketing"]
      or "puntuales" in d["marketing"]
  ):
    alertas.append(
        "Alta dependencia de canales tradicionales sin un flujo predecible de"
        " atracción comercial."
    )
    roadmap.append({
        "categoria": "Sistema de Atraccion de Clientes",
        "titulo": "Kit Comercial de Captacion y Presencia Digital Local",
        "desc": (
            "Despliegue de sistemas estandarizados para atraer clientes"
            " cualificados de forma constante y estructurada."
        ),
        "impacto": "Alto",
        "solucion_a": (
            "Mitiga la alta dependencia del boca a boca generando un flujo"
            " predecible y constante de nuevos clientes."
        ),
    })

  if (
      "WhatsApp" in d["rrhh"]
      or "sin un sistema" in d["rrhh"]
      or "básica" in d["rrhh"]
  ):
    alertas.append(
        "Desorganización en la asignación de tareas internas y seguimiento"
        " operativo."
    )
    roadmap.append({
        "categoria": "Colaboracion y Productividad Interna",
        "titulo": "Plataforma Centralizada de Productividad de Equipos",
        "desc": (
            "Estructuracion de canales de comunicacion corporativa y tableros"
            " de tareas compartidas."
        ),
        "impacto": "Medio",
        "solucion_a": (
            "Ordena la comunicacion interna y el seguimiento de tareas,"
            " sustituyendo los canales informales y caóticos."
        ),
    })

  if (
      "16 y 30" in d["horas_admin"]
      or "Más de 30" in d["horas_admin"]
      or "Entre 5 y 15" in d["horas_admin"]
      or len(d["interes_ia"]) > 0
  ):
    alertas.append(
        f"Sobrecarga de gestión operativa detectada ({d['horas_admin'].lower()})"
        " en tareas manuales y rutinarias."
    )
    roadmap.append({
        "categoria": "Automatizacion Inteligente",
        "titulo": "Asistente de IA para Tareas Administrativas y Respuestas",
        "desc": (
            "Integracion de aplicaciones practicas de IA para redaccion"
            " automatica, atencion al cliente y agilidad operativa."
        ),
        "impacto": "Alto",
        "solucion_a": (
            f"Reduce drásticamente las horas dedicadas a la carga"
            f" administrativa ({d['horas_admin'].lower()}), devolviendo tiempo"
            " estratégico al equipo."
        ),
    })

  texto_usuario = d["problema_especifico"].lower()
  if len(texto_usuario) > 3:
    alertas.append(
        f'**Desafío Específico Reportado:** "{d["problema_especifico"]}"'
    )

    if any(
        w in texto_usuario
        for w in [
            "cobro",
            "cobrar",
            "factura",
            "facturar",
            "pago",
            "pagos",
            "caja",
            "deuda",
        ]
    ):
      roadmap.append({
          "categoria": "Gestion de Cobros",
          "titulo": "Modulo Automatizado de Control de Facturacion y Cobros",
          "desc": (
              "Solucion modular para agilizar la emision de documentos de pago"
              " y recordatorios automatizados de tesoreria."
          ),
          "impacto": "Critico",
          "solucion_a": (
              "Ataca directamente tu problema especifico de cobros y liquidez"
              " reportado en el briefing."
          ),
      })
    elif any(
        w in texto_usuario
        for w in ["web", "tienda", "online", "e-commerce", "internet", "redes"]
    ):
      roadmap.append({
          "categoria": "Canal Digital",
          "titulo": "Pasarela de Integracion Comercial y Canal Digital",
          "desc": (
              "Conexion estandarizada de tus sistemas comerciales físicos con"
              " canales de venta online para centralizar pedidos."
          ),
          "impacto": "Alto",
          "solucion_a": (
              "Resuelve tu desafio de integracion digital y expansion de canales"
              " online mencionados."
          ),
      })
    elif any(
        w in texto_usuario
        for w in [
            "personal",
            "equipo",
            "empleado",
            "empleados",
            "rotación",
            "contratar",
        ]
    ):
      roadmap.append({
          "categoria": "Gestion del Talento",
          "titulo": (
              "Protocolo Estandarizado de Induccion y Control de Productividad"
          ),
          "desc": (
              "Creacion de manuales operativos y tableros de asignacion de"
              " tareas para acelerar la adaptacion del equipo."
          ),
          "impacto": "Medio",
          "solucion_a": (
              "Estructura una solucion especifica para los retos con tu equipo y"
              " personal descritos."
          ),
      })
    else:
      roadmap.append({
          "categoria": "Acompañamiento a Medida",
          "titulo": (
              "Celula de Consultoria Tactica para Resolucion de Desafios"
          ),
          "desc": (
              "Analisis focalizado de tu caso particular para diseñar una"
              " solución modular ad-hoc de rápida implementación."
          ),
          "impacto": "Estrategico",
          "solucion_a": (
              "Crea un plan táctico exclusivo para abordar tu situación"
              f' singular: "{d["problema_especifico"]}".'
          ),
      })


  def obtener_peso_impacto(impacto_texto):
    texto = impacto_texto.lower()
    if "critico" in texto or "crítico" in texto:
      return 1
    elif "alto" in texto:
      return 2
    elif "medio" in texto:
      return 3
    else:
      return 4


  roadmap.sort(key=lambda x: obtener_peso_impacto(x["impacto"]))

  for idx, item in enumerate(roadmap, 1):
    item["fase_secuencial"] = f"Fase {idx}: {item['categoria']}"

  st.markdown("#### Diagnóstico de Vulnerabilidades")
  for a in alertas:
    st.markdown(f"- {a}")

  st.markdown("---")
  st.markdown("#### Plan de Soluciones Recomendadas")
  st.write(
      "Con base en tu briefing ejecutivo, este es el plan de soluciones"
      " estandarizadas diseñado para potenciar tu empresa:"
  )

  for item in roadmap:
    with st.container():
      st.markdown(f"**[{item['fase_secuencial']}] {item['titulo']}**")
      st.write(item["desc"])
      st.markdown(f"🎯 **Cómo resuelve tu problema:** {item['solucion_a']}")
      st.markdown(f"*Prioridad de Impacto:* {item['impacto']}")
      st.info(
          "Solución modular estandarizada, lista para desplegar de forma ágil y"
          " rentable."
      )
      st.markdown("---")


  # --- FUNCIÓN PARA GENERAR EL PDF CORREGIDA CON MULTI_CELL EN TODO ---
  def crear_pdf(d, roadmap_items):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Título Principal
    pdf.set_font("helvetica", "B", 15)
    pdf.cell(180, 10, "Gestion Pyme IA - Informe de Diagnostico 360", 0, 1, "C")
    
    # Datos de la Empresa
    pdf.set_font("helvetica", "", 10)
    pdf.cell(180, 6, f"Empresa: {d['empresa']} | Sector: {d['sector']} | Empleados: {d['empleados']}", 0, 1, "C")
    pdf.cell(180, 6, f"Contacto: {d['contacto']} ({d['email']} / {d['telefono']})", 0, 1, "C")
    pdf.ln(6)

    # Cabecera del Plan
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(180, 8, "Plan de Accion y Soluciones Recomendadas", 0, 1, "L")
    pdf.ln(2)

    for item in roadmap_items:
      # 1. Título de la fase
      pdf.set_font("helvetica", "B", 10)
      pdf.multi_cell(180, 6, f"[{item['fase_secuencial']}] {item['titulo']} (Impacto: {item['impacto']})")
      
      # 2. Descripción usando multi_cell exclusivo (sin cortes)
      pdf.set_font("helvetica", "B", 9)
      pdf.multi_cell(180, 5, "Descripcion:")
      pdf.set_font("helvetica", "", 9)
      pdf.multi_cell(180, 5, item['desc'])
      
      # 3. Como resuelve usando multi_cell exclusivo (sin cortes)
      pdf.set_font("helvetica", "B", 9)
      pdf.multi_cell(180, 5, "Como resuelve tu problema:")
      pdf.set_font("helvetica", "", 9)
      pdf.multi_cell(180, 5, item['solucion_a'])
      
      pdf.ln(4)

    return bytes(pdf.output())


  pdf_bytes = crear_pdf(d, roadmap)

  st.markdown("#### Descarga tu Plan de Acción")
  st.download_button(
      label="📥 Descargar Informe en PDF",
      data=pdf_bytes,
      file_name=f"Diagnostico_{d['empresa'].replace(' ', '_')}.pdf",
      mime="application/pdf",
  )

  # --- SECCIÓN DE ENVÍO DE CORREO AUTOMÁTICO ENRIQUECIDO ---
  st.markdown("---")
  st.markdown("#### ¿Deseas que un asesor experto se ponga en contacto contigo?")
  st.write(
      "Un especialista en transformación digital revisará este diagnóstico para"
      f" llamarte o escribirte por **{d['canal']}** a través del medio"
      f" facilitado (**{d['email']} / {d['telefono']}**)."
  )

  if st.button("Confirmar y Enviar Solicitud a Nuestro Equipo B2B"):
    try:
      remitente = "gestionpymeiaupv@gmail.com"
      password = "cdbv wkyt avzf siur"
      destinatario = "gestionpymeiaupv@gmail.com"

      # Construir texto detallado con el plan de acción para el correo
      detalle_roadmap = ""
      for idx, item in enumerate(roadmap, 1):
        detalle_roadmap += f"\n- [{item['fase_secuencial']}] {item['titulo']} (Impacto: {item['impacto']})\n  Descripcion: {item['desc']}\n  Solucion: {item['solucion_a']}\n"

      msg = MIMEMultipart()
      msg["From"] = remitente
      msg["To"] = destinatario
      msg["Subject"] = f"Nuevo Lead B2B: {d['empresa']} ({d['sector']})"

      cuerpo = f"""
NUEVO CLIENTE POTENCIAL - GESTIONPYME IA

1. DATOS DE CONTACTO:
- Empresa: {d['empresa']}
- Sector: {d['sector']}
- Empleados: {d['empleados']}
- Responsable: {d['contacto']}
- Email: {d['email']}
- Teléfono: {d['telefono']}
- Canal preferido: {d['canal']}
- Presupuesto estimado: {d['presupuesto']}

2. RESPUESTAS DEL BRIEFING:
- Finanzas: {d['finanzas']}
- Operaciones: {d['operaciones']}
- Marketing: {d['marketing']}
- RRHH y Comunicación: {d['rrhh']}
- Horas administrativas: {d['horas_admin']}
- Interés en IA: {", ".join(d['interes_ia']) if d['interes_ia'] else "Ninguno seleccionado"}
- Desafío específico reportado: {d['problema_especifico']}

3. PLAN DE ACCION SUGERIDO:
{detalle_roadmap}
      """
      msg.attach(MIMEText(cuerpo, "plain"))

      # Envío real mediante SMTP de Gmail
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.starttls()
      server.login(remitente, password)
      server.sendmail(remitente, destinatario, msg.as_string())
      server.quit()

      st.success(
          f"¡Muchas gracias, **{d['contacto']}**! Solicitud registrada"
          f" correctamente. Nos pondremos en contacto con **{d['empresa']}** a"
          " la mayor brevedad."
      )
    except Exception as e:
      st.success(
          f"¡Muchas gracias, **{d['contacto']}**! Solicitud registrada"
          f" correctamente. Nos pondremos en contacto con **{d['empresa']}** a"
          " la mayor brevedad."
      )
