from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# ============================
#   SISTEMA DE RESPUESTAS
# ============================

def normalizar(mensaje: str) -> str:
    """Convierte el mensaje a minúsculas y elimina espacios extra."""
    return mensaje.lower().strip()


def obtener_respuesta(mensaje):
    mensaje = normalizar(mensaje)

    # =====================
    # MATRÍCULA
    # =====================
    if "matrícula" in mensaje or "matricula" in mensaje:
        return (
            "<b>📚 Requisitos para matrícula 2025:</b><br>"
            "✅ DNI del estudiante (original y copia)<br>"
            "✅ Partida de nacimiento<br>"
            "✅ Ficha Única de Matrícula actualizada<br>"
            "✅ Copia del DNI de los padres o apoderado<br>"
            "✅ Libreta de notas o constancia de estudios anterior<br><br>"

            "<b>🧾 Descarga los formatos oficiales:</b><br>"
            "• <a href='https://cutt.ly/ke52Tsxc' target='_blank'>Inicial</a><br>"
            "• <a href='https://cutt.ly/de52TmBR' target='_blank'>Primaria</a><br>"
            "• <a href='https://cutt.ly/Pe52TIqQ' target='_blank'>Secundaria</a><br><br>"

            "ℹ️ Para más información, dirígete a Secretaría Académica."
        )

    # =====================
    # HIMNOS
    # =====================
    elif "himno" in mensaje:
        return (
            "<b>🎶 Himnos Oficiales</b><br><br>"
            "<b>Himno Nacional del Perú</b><br>"
            "<b>Coro:</b><br>"
        "<i>Somos libres, seámoslo siempre,<br>"
        "y antes niegue sus luces el sol,<br>"
        "que faltemos al voto solemne<br>"
        "que la patria al eterno elevó.<br>"
        "(¡Que faltemos al voto solemne<br>"
        "que la patria al eterno elevó!)</i><br><br>"
        "<b>Estrofa VI:</b><br>"
        "<i>En su cima los Andes sostengan<br>"
        "la bandera o pendón bicolor,<br>"
        "que a los siglos anuncie el esfuerzo<br>"
        "que ser libres, por siempre nos dio.<br>"
        "A su sombra vivamos tranquilos,<br>"
        "y al nacer por sus cumbres el sol,<br>"
        "renovemos el gran juramento<br>"
        "que rendimos al Dios de Jacob.<br>"
        "(¡Renovemos el gran juramento<br>"
        "que rendimos al Dios de Jacob!)</i><br><br>"
            "<b>🌄 Himno a Huánuco</b><br>"
            "<b>Coro:</b><br>"
        "<i>¡Salve oh, Huánuco!<br>"
        "tierra bravía de hidalguía y sin par tradición,<br>"
        "que hoy tus hijos de júbilo henchidos<br>"
        "cantan loas con viva emoción.</i><br><br>"
        "<b>I Estrofa:</b><br>"
        "<i>Torre enhiesta de noble pasado,<br>"
        "que se agitó tu llama y ardor;<br>"
        "Yarowilcas te infunden sus glorias<br>"
        "e Illathupa su férreo valor.<br>"
        "Que perenne en los siglos ostentes<br>"
        "tus blasones, tus galas viril,<br>"
        "y a la patria sus sienes remoces<br>"
        "con diademas de palma y laurel.</i><br><br>"
            "<b>🏫 Himno del Colegio Leoncio Prado</b><br>"
            "<b>Coro:</b><br>"
        "<i>Entonemos el canto de gloria<br>"
        "de esta gran unidad escolar,<br>"
        "cuna excelsa de Leoncio Prado,<br>"
        "fiel antorcha de luz y saber. (bis)</i><br><br>"
        "<b>Estrofas principales:</b><br>"
        "<i>Son los plácidos claustros santuario,<br>"
        "de trabajo de ciencia y de bien,<br>"
        "donde se forja el carácter y el alma,<br>"
        "de la riente y viril juventud.<br><br>"
        "Semillero de nobles virtudes,<br>"
        "de cultura y de honor adalid,<br>"
        "laboriosa colmena de obreros,<br>"
        "de un Perú progresista y feliz.</i>"
        )

    # =====================
    # HISTORIA
    # =====================
    elif "historia" in mensaje:
        return (
            "<b>🏛️ Historia de la Gran Unidad Escolar Leoncio Prado</b><br><br>"
            "La <b>Gran Unidad Escolar Leoncio Prado</b>, ubicada en Huánuco, Perú, tiene una rica historia que se remonta a su creación "
            "por <b>Ley del 25 de febrero de 1828</b> aprobada por el Congreso General Constituyente y promulgada el <b>04 de marzo de 1828</b> "
            "por <b>José de La Mar</b>, iniciando su funcionamiento el <b>24 de mayo de 1829</b>.<br><br>"
            "Se fundó como el <b>Colegio de Ciencias de Huánuco</b>, evolucionando para convertirse en la emblemática institución que es hoy. "
            "Ha sido un crisol de personalidades influyentes en la región y en el país.<br><br>"

            "<b>📜 Antecedentes</b><br>"
            "En <b>1828</b>, se creó el Colegio de Ciencias de Huánuco, el precursor de la actual Gran Unidad Escolar Leoncio Prado, "
            "con la aprobación de una ley del Congreso General Constituyente y la promulgación del presidente José de La Mar.<br><br>"

            "<b>⚙️ Base para la Universidad Nacional de Ingeniería (UNI)</b><br>"
            "El Colegio de Ciencias de Huánuco fue considerado la base para la creación de la <b>Universidad Nacional de Ingeniería (UNI)</b>.<br><br>"
            "Entre <b>1832 y 1833</b> cambió de denominación a <b>Colegio de la Virtud Humana</b> y años más tarde, por ley del <b>8 de julio de 1846</b>, "
            "pasó a llamarse <b>Escuela Central de Minería</b>.<br><br>"
            "En <b>julio de 1848</b> asumió la rectoría <b>Mariano Dámaso Beraún</b>, pasando de categoría de <b>Colegio Mayor o Universidad Menor</b> "
            "a llamarse <b>Colegio Central de Minería</b>.<br><br>"
            "Mediante R.S. Nº 180 del <b>14 de julio de 1933</b> se cambió el nombre de <b>Colegio Nacional de Minería</b> a <b>Colegio Nacional “Leoncio Prado”</b>, "
            "acordándose declarar el <b>24 de mayo</b> de cada año como <b>Día del Colegio</b>.<br><br>"

            "<b>🏛️ Museo de Historia Natural</b><br>"
            "El <b>20 de diciembre de 1947</b> se fundó el <b>Museo de Historia Natural</b> por gestiones del senador <b>Carlos Showing Ferrari</b>. "
            "Dirigido inicialmente por el taxidermista <b>Víctor Cárdenas</b>, funcionó primero en la casa del Dr. Showing Ferrari, "
            "para luego trasladarse al Colegio Nacional “Leoncio Prado”.<br><br>"

            "<b>🏫 Evolución institucional</b><br>"
            "En <b>1957</b> ascendió a la categoría de <b>Gran Unidad Escolar Leoncio Prado</b>.<br>"
            "En <b>1977</b> adoptó el nombre de <b>Centro Base Leoncio Prado</b> y en <b>1983</b> nuevamente pasó a denominarse <b>Colegio Nacional Leoncio Prado</b>.<br>"
            "Finalmente, el <b>24 de mayo de 2007</b> retomó su denominación actual: <b>Gran Unidad Escolar Leoncio Prado</b>.<br><br>"

            "<b>⚔️ Guerra con España (1865–1866)</b><br>"
            "Los estudiantes del <b>Colegio Central de Minería</b> formaron el <b>Batallón “Huánuco”</b>, participando heroicamente en el <b>Combate del 2 de Mayo de 1866</b>.<br><br>"

            "<b>⚔️ Guerra con Chile (1879–1885)</b><br>"
            "Durante la <b>Guerra del Pacífico</b>, el colegio se convirtió en cuartel general formando el <b>Batallón “Cazadores del Huallaga”</b>.<br><br>"

            "<b>🏅 Desarrollo y legado</b><br>"
            "<b>⚽ Club Social y Deportivo:</b> En <b>1929</b> se fundó el <b>Sport Minería</b>, luego <b>Club Leoncio Prado</b> y posteriormente <b>Club León de Huánuco</b>.<br><br>"
            "<b>🌟 Semillero de personalidades:</b> Destacados líderes en política, ciencia, cultura y deporte a nivel regional y nacional.<br><br>"

            "<b>🏆 Impacto y reconocimientos</b><br>"
            "En <b>2012</b>, obtuvo <b>26 premios</b> y su escolta fue reconocida como <b>Guardia de Honor</b>.<br><br>"
            "En <b>2015</b>, primera directora mujer <b>Elisa Camarena Miranda</b>.<br><br>"
            "En <b>2021</b>, reconocida como <b>Institución Educativa Líder del Bicentenario del Perú</b>.<br><br>"

            "<b>📘 Conclusión</b><br>"
            "Con casi <b>dos siglos de historia</b>, la Gran Unidad Escolar Leoncio Prado es símbolo de "
            "<b>disciplina, civismo, conocimiento y orgullo huanuqueño</b>."
        )

    # =====================
    # REGLAMENTO
    # =====================
    elif "reglamento" in mensaje or "normas" in mensaje:
        return (
            "<b>📘 Reglamento Interno</b><br>"
            "📌 Puntualidad obligatoria — 3 tardanzas = 1 falta.<br>"
            "📌 Uniforme completo institucional.<br>"
            "📌 Prohibido bullying o violencia.<br>"
            "📌 Celulares solo con autorización docente.<br>"
            "📌 Cuidado de instalaciones.<br>"
            "📌 Sanciones según gravedad.<br><br>"
            "<i>Reglamento completo disponible en Secretaría.</i>"
        )

    # =====================
    # MISIÓN / VISIÓN
    # =====================
    elif any(x in mensaje for x in ["misión", "mision", "visión", "vision"]):
        return (
            "<b>🎯 MISIÓN</b><br>"
            "Formar ciudadanos responsables y comprometidos con su entorno.<br><br>"

            "<b>🌟 VISIÓN</b><br>"
            "Ser una institución educativa referente en excelencia y valores."
        )

    # =====================
    # VALORES
    # =====================
    elif "valores" in mensaje:
        return (
            "<b>💎 Valores Institucionales</b><br>"
            "• Responsabilidad<br>"
            "• Respeto<br>"
            "• Honestidad<br>"
            "• Tolerancia<br>"
            "• Solidaridad<br>"
            "• Perseverancia"
        )

    # =====================
    # TALLERES
    # =====================
    elif "taller" in mensaje:
        return (
            "<b>🎨 Talleres Extracurriculares 2025</b><br>"
            "🎭 Teatro<br>"
            "🎵 Música y canto<br>"
            "⚽ Fútbol, vóley, básquet<br>"
            "♟️ Ajedrez<br>"
            "👯‍♂️ Danza moderna y folclore<br>"
            "🎨 Dibujo y pintura"
        )

    # =====================
    # SERVICIOS
    # =====================
    elif "servicio" in mensaje:
        return (
            "<b>🏫 Servicios del Colegio</b><br>"
            "✔️ Laboratorios de Ciencia y Computación<br>"
            "✔️ Biblioteca moderna<br>"
            "✔️ Auditorio institucional<br>"
            "✔️ Canchas deportivas<br>"
            "✔️ Psicología, tutoría y enfermería<br>"
            "✔️ Cafetería"
        )

    # =====================
    # BIBLIOTECA
    # =====================
    elif "biblioteca" in mensaje:
        return (
            "<b>📚 Biblioteca Institucional</b><br>"
            "🕐 Lunes a Viernes — 8:00 a 1:00 p.m.<br>"
            "📖 Préstamo de libros, lectura y asesoría."
        )

    # =====================
    # UNIFORME
    # =====================
    elif "uniforme" in mensaje:
        return (
            "<b>👔 Uniforme Escolar</b><br>"
            "👕 Varones: Camisa y pantalón caqui.<br>"
            "👩 Damas: Blusa y falda caqui oscuro.<br>"
            "🎽 Educación Física: Polo blanco y buzo azul."
        )

    # =====================
    # HORARIOS
    # =====================
    elif "horario" in mensaje:
        return (
            "<b>🕐 Horarios de Clases</b><br>"
            "📅 Lunes a Viernes: 7:30 a.m. — 1:30 p.m.<br>"
            "🍎 Recreo: 10:15 a.m. — 10:30 a.m.<br><br>"

            "<b>Turnos académicos:</b><br>"
            "1️⃣ 7:15 a.m. — 12:45 p.m.<br>"
            "2️⃣ 1:00 p.m. — 6:30 p.m."
        )

    # =====================
    # AUTORIDADES
    # =====================
    elif any(x in mensaje for x in ["autoridad", "director"]):
        return (
            "<b>👨‍🏫 Autoridades 2025</b><br>"
            "• Director: Mg. Julio César Chávez Cabrera<br>"
            "• Subdirectora Académica: Lic. Rosa Espinoza Díaz<br>"
            "• Subdirector Administrativo: Prof. Juan Carlos Ramos<br>"
            "• Coordinador de Disciplina: Prof. Luis Huamán"
        )

    # =====================
    # ACTIVIDADES
    # =====================
    elif "actividades" in mensaje:
        return (
            "<b>📅 Actividades Escolares 2025</b><br>"
            "• Inicio de clases — Marzo<br>"
            "• Olimpiadas — Mayo<br>"
            "• Feria de Ciencia — Julio<br>"
            "• Aniversario — Septiembre<br>"
            "• Festival Cultural — Octubre<br>"
            "• Clausura — Diciembre"
        )

    # =====================
    # CONTACTO
    # =====================
    elif any(x in mensaje for x in ["contacto", "teléfono", "telefono", "correo", "ubicación", "direccion", "dirección"]):
        return (
            "<b>☎️ Contacto</b><br>"
            "📍 Jr. Dámaso Beraún s/n, Huánuco<br>"
            "📞 (062) 512103<br>"
            "✉️ guelp@leoncioprado.edu.pe<br>"
            "🌐 leoncioprado.edu.pe<br>"
            "🕐 Atención: 8:00 a.m. — 2:00 p.m."
        )

    # =====================
    # RESPUESTA GENERAL
    # =====================
    respuestas_generales = [
        "🤔 No entendí muy bien, ¿podrías repetirlo?",
        "📘 Puedo ayudarte con matrícula, historia, himnos, horarios, reglamento y más.",
        "🧠 Intenta preguntarme: 'Matrícula', 'Himno', 'Historia', 'Horarios', etc."
    ]
    return random.choice(respuestas_generales)

# ============================
#   RUTAS FLASK
# ============================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    mensaje = request.get_json().get("mensaje", "")
    return jsonify({"respuesta": obtener_respuesta(mensaje)})


@app.route("/bienvenida")
def bienvenida():
    return jsonify({
        "respuesta": (
            "👋 <b>¡Hola! Soy tu asistente escolar virtual.</b><br>"
            "Puedo ayudarte hoy:<br>"
        )
    })


# ============================
# MAIN
# ============================

if __name__ == "__main__":
    app.run(debug=True)
