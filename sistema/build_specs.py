"""Parrilla NuByA 1 oct – 29 oct 2026: specs de render + paquetes de publicación (piezas 2–10)."""
import json, re, pathlib, html

OUT = pathlib.Path(__file__).parent
H = "@nutritionbyannie"
TAGS = {
 'base': "#nutriologacdmx #nutricionclinica #nutricionpersonalizada",
}
# esquinas para doodles: (x, y)
TL, TR, BL, BR = (80, 100), (790, 95), (90, 1000), (800, 985)
def d(name, pos, w=210, r=0, dx=0, dy=0): return [name, pos[0]+dx, pos[1]+dy, w, r]
def S(a, b): return [[a, b[0]], [b[1] if False else ('menta' if a == 'rosa' else 'rosa'), b[1]]]
def st(first, c1, c2): return [[first, c1], ['menta' if first == 'rosa' else 'rosa', c2]]

CTA_STYLE = "justify-content:flex-start;padding-top:200px;padding-right:120px"
def cta(kicker, title, whisper, doodles, first='menta', size=None):
    c = {"type": "cta", "kicker": kicker, "title": title, "whisper": whisper, "inner_style": CTA_STYLE,
         "stains": st(first, 'tr', 'bl'), "doodles": doodles}
    if size: c["size"] = size
    return c

P = []

# ---------- 2 · Jue 1 oct 7:30 · Educación C · El desayuno que te saltas ----------
P.append(dict(n=2, slug="p02-desayuno-que-te-saltas", title="El desayuno que te saltas", pillar="Educación", arc="C · Denuncia educativa",
  at="2026-10-01T07:30:00-06:00", cta_type="Guardar",
  cards=[
    {"type":"hook","title":"Así es como tú conviertes un “hoy me porto bien” en las papitas de las 5&nbsp;de&nbsp;la&nbsp;tarde.","size":84,
     "whisper":"[[u]]Sin darte cuenta.[[/u]]","swipe":"desliza →","stains":st('rosa','tr','bl'),
     "doodles":[d('cafe',TL,220,-8),d('reloj',BR,200,8)]},
    {"type":"statement","title":"Anoche cenaste de&nbsp;más.","whisper":"Entonces hoy, con toda la buena intención, te saltas el desayuno para “compensar”.",
     "stains":st('menta','tl','br'),"doodles":[d('luna-zzz',TR,210,6),d('cubiertos',BL,190,-10)]},
    {"type":"list","title":"Y el día se ve así:","bullet":"→","panel":"salvia","washi":"",
     "items":["11 am · dolor de cabeza","1 pm · de malas","5 pm · lo primero que encuentras… y otra vez la culpa"],
     "stains":st('rosa','tl','br'),"doodles":[d('reloj',TR,190,10),d('nube-pensamiento',BL,200,-6)]},
    {"type":"statement","title":"No es falta de voluntad.","whisper":"Tu cuerpo llegó con tanta hambre que ya no pudo elegir.",
     "paren":"Entonces vamos a [[u]]desayunar normal, con proteína.[[/u]]",
     "stains":st('menta','tr','bl'),"doodles":[d('huevo',TL,210,-10),d('aguacate',BR,200,8)]},
    {"type":"statement","title":"Lo de anoche no estuvo&nbsp;mal.<br><span class=\"mark\">Y el día de hoy no tiene por qué pagarlo.</span>","size":80,
     "stains":st('rosa','tl','br'),"doodles":[d('corazon',TR,170,10),d('hojita',BL,180,-12)]},
    cta("Guárdalo","La próxima vez que quieras “compensar” una cena…","…vuelve a verlo antes de saltarte el [[u]]desayuno[[/u]].",
        [d('check',(90,790),140,-8),d('huevo',(300,770),170,6),d('sandia',TR,190,-8)]),
  ],
  caption="""Así es como un “hoy me porto bien” termina en las papitas de las 5 de la tarde.

Anoche cenaste de más. Entonces hoy te saltas el desayuno para “compensar”. A las 11 te duele la cabeza, a la 1 andas de malas y a las 5 comes lo primero que encuentras… y otra vez la culpa.

No es falta de voluntad: tu cuerpo llegó con tanta hambre que ya no pudo elegir. Lo de anoche no estuvo mal, y el día de hoy no tiene por qué pagarlo. Desayuna normal, con proteína.

Guárdalo para la próxima vez que quieras “compensar” una cena 📌

Nutrición clínica · CDMX y online

#nutriologacdmx #nutricionclinica #desayunosaludable #nutricionpersonalizada #sinculpa"""))

# ---------- 3 · Mar 6 oct 20:30 · Atracción D · Días ocupados ----------
def pair(top, bottom, i, pos1, pos2, dd1, dd2, size=None):
    first = 'rosa' if i % 2 else 'menta'
    c = {"type":"split","label":"Hoy te quejas","top":top,"note":"y hace unos años decías…","bottom":bottom,
         "panel":"salvia" if i % 2 else "","washi":"" if i % 2 else "mint",
         "stains":st(first, pos1, pos2),"doodles":[dd1,dd2]}
    if size: c["size"] = size
    return c
P.append(dict(n=3, slug="p03-dias-ocupados", title="Días ocupados", pillar="Atracción", arc="D · Contraste pasado/presente",
  at="2026-10-06T20:30:00-06:00", cta_type="Comentar",
  cards=[
    {"type":"hook","title":"Tu agenda está llena de todo lo que un día soñaste…","whisper":"[[u]]menos de tu comida.[[/u]]","swipe":"desliza →",
     "stains":st('rosa','tr','bl'),"doodles":[d('calendario',TL,220,-8),d('cafe',BR,200,8)]},
    pair("“Ya ni desayuno, salgo corriendo a la oficina.”","¿Me dieron el trabajo?!",1,'tl','br',d('cafe',TR,190,8,dy=10),d('estrella',BL,160,-10)),
    pair("“Como lo que sea frente a la compu, entre junta y junta.”","¿Voy a trabajar desde casa?!",2,'tr','bl',d('celular',TR,160,10,dy=20),d('tupper',BR,200,-6)),
    pair("“No me da la vida para el súper, todo lo pido por app.”","¿Tengo mi propio depa?!",3,'tl','br',d('bolsa-super',TR,190,8,dy=10),d('destellos',BL,170,-8)),
    pair("“Ceno a las 11, después de dormir a los niños.”","¿Vamos a tener hijos?!",4,'tr','bl',d('luna-zzz',TR,190,8,dy=10),d('corazones-mini',BR,190,-6)),
    cta("Cuéntame","Lograste todo lo que soñabas. Ahora vamos a hacer que tu comida quepa en esa vida.",
        "¿Cuál de estas te tocó más? [[u]]Dímelo en comentarios.[[/u]]",
        [d('globo',(90,800),160,-8),d('plato',(310,790),160,6),d('sandia',TR,190,-8)], size=72),
  ],
  caption="""Tu agenda está llena de todo lo que un día soñaste… menos de tu comida.

Hoy te quejas de no desayunar porque sales corriendo a la oficina, de comer frente a la compu, de pedir todo por app, de cenar a las 11. Y hace unos años eso era exactamente lo que soñabas: el trabajo, el depa, los hijos.

Lograste la vida que querías. Ahora vamos a hacer que tu comida quepa en ella, sin que tengas que cambiar de vida para comer bien.

¿Cuál de estas te tocó más? Cuéntame en comentarios 👇

Nutrición clínica · CDMX y online

#nutriologacdmx #nutricionclinica #nutricionpersonalizada #mamastrabajadoras #comerbien"""))

# ---------- 4 · Jue 8 oct 20:30 · Autoridad A · La carpeta de dietas (caso identificable, sin afirmar paciente real) ----------
P.append(dict(n=4, slug="p04-carpeta-de-dietas", title="La carpeta de dietas", pillar="Autoridad", arc="A · Punto de inflexión (2ª persona)",
  at="2026-10-08T20:30:00-06:00", cta_type="Seguir",
  cards=[
    {"type":"hook","title":"Si tienes una carpeta con 8&nbsp;dietas…","whisper":"[[u]]aunque sea en capturas del celular,[[/u]] esto es para ti.","swipe":"desliza →",
     "stains":st('rosa','tr','bl'),"doodles":[d('portapapeles',TL,220,-8),d('celular',BR,170,10)]},
    {"type":"list","title":"Keto, ayuno, la de la piña, la del doctor de TikTok.","size":72,"bullet":"→","panel":"","washi":"mint",
     "items":["Empiezas el lunes y el jueves ya la dejaste","Comes con culpa hasta la fruta","En tu casa ya ni te preguntan “¿cómo vas?”"],
     "stains":st('menta','tl','br'),"doodles":[d('tache',TR,160,8,dy=10),d('nube-pensamiento',BL,190,-6)]},
    {"type":"statement","title":"No te faltan dietas.<br><span class=\"mark rosa\">Te sobran.</span>",
     "whisper":"Ninguna empezó por preguntarte qué trae tu cuerpo.",
     "stains":st('rosa','tl','br'),"doodles":[d('globo-ojo',TR,200,8),d('espiral',BL,160,-10)]},
    {"type":"list","title":"Entonces guardamos la carpeta y empezamos por&nbsp;ti:","size":70,"bullet":"✓","panel":"salvia","washi":"",
     "items":["Tus estudios antes de cualquier menú","Un plan con la comida que ya hay en tu casa","Revisión cada mes, para ajustar, no para regañar"],
     "stains":st('menta','tr','bl'),"doodles":[d('estetoscopio',TR,190,6,dy=5),d('lapiz',BR,180,-8)]},
    {"type":"statement","title":"Así trabajo en consulta.","whisper":"Con cada persona que llega “habiéndolo intentado todo”.",
     "paren":"Medidas, estudios y [[u]]tu plan del mes,[[/u]] no una hoja de dieta más.",
     "stains":st('rosa','tl','br'),"doodles":[d('cinta-metrica',TR,200,8),d('calendario',BL,180,-8)]},
    cta("Sígueme","Si tú también tienes tu carpeta de dietas…","aquí vamos a hablar de todo lo que [[u]]ninguna te preguntó.[[/u]]",
        [d('flecha-rizo',(90,800),190,-4),d('lentes',(330,790),170,6),d('sandia',TR,190,-8)]),
  ],
  caption="""Si tienes una carpeta con 8 dietas (aunque sea en capturas del celular), esto es para ti.

Keto, ayuno, la de la piña, la del doctor de TikTok. Empiezas el lunes, el jueves ya la dejaste, y comes con culpa hasta la fruta.

No te faltan dietas. Te sobran. Ninguna empezó por preguntarte qué trae tu cuerpo.

Por eso en consulta guardamos la carpeta y empezamos por ti: estudios antes de cualquier menú, un plan con la comida que ya hay en tu casa y una revisión cada mes para ajustar, no para regañar.

Si tú también tienes tu carpeta, sígueme: aquí vamos a hablar de todo lo que ninguna de esas dietas te preguntó 💚

Nutrición clínica · CDMX y online

#nutriologacdmx #nutricionclinica #nutricionpersonalizada #dietasquenofuncionan #resistenciaalainsulina"""))

# ---------- 5 · Mar 13 oct 13:30 · Atracción E · El detox más caro ----------
P.append(dict(n=5, slug="p05-el-detox-mas-caro", title="El detox más caro", pillar="Atracción", arc="E · Frase compartible (4 cards)",
  at="2026-10-13T13:30:00-06:00", cta_type="Compartir",
  cards=[
    {"type":"hook","title":"El detox más caro es el que compras cada&nbsp;mes…","whisper":"[[u]]porque el anterior no funcionó.[[/u]]","swipe":"desliza →",
     "stains":st('menta','tr','bl'),"doodles":[d('botella',TL,200,-8),d('smoothie',BR,200,8)]},
    {"type":"statement","title":"Tés, malteadas, gomitas, pastillas “desinflamatorias”.","size":76,
     "whisper":"Entonces, si ninguno funcionó, no es que no hayas [[u]]encontrado el bueno.[[/u]]",
     "stains":st('rosa','tl','br'),"doodles":[d('tache',TR,160,8,dy=10),d('gotas',BL,180,-6)]},
    {"type":"statement","title":"Es que ninguno empezó por preguntarte <span class=\"mark\">qué trae tu cuerpo.</span>","size":78,
     "whisper":"Tu tiroides, tu insulina, cómo comes un martes real.",
     "stains":st('menta','tl','br'),"doodles":[d('estetoscopio',TR,200,8),d('plato',BL,180,-8)]},
    cta("Compártelo","Mándaselo a quien tenga la alacena llena de tés detox.","Sin juzgar, [[u]]eh.[[/u]]",
        [d('celular',(90,790),150,-10),d('corazones-mini',(320,760),160,-6),d('sandia',TR,190,-8)], first='rosa'),
  ],
  caption="""El detox más caro es el que compras cada mes porque el anterior no funcionó.

Tés, malteadas, gomitas, pastillas “desinflamatorias”. Si ninguno funcionó, no es que no hayas encontrado el bueno. Es que ninguno empezó por preguntarte qué trae tu cuerpo: tu tiroides, tu insulina, cómo comes un martes real.

Antes de gastar en el siguiente, revisa lo que de verdad está pasando.

Mándaselo a quien tenga la alacena llena de tés detox. Sin juzgar, eh 💌

Nutrición clínica · CDMX y online

#nutriologacdmx #nutricionclinica #nutricionpersonalizada #sindetox #resistenciaalainsulina"""))

# ---------- 6 · Jue 15 oct 13:30 · Educación C · El "me lo gané" del viernes ----------
P.append(dict(n=6, slug="p06-me-lo-gane", title="El “me lo gané” del viernes", pillar="Educación", arc="C · Denuncia educativa",
  at="2026-10-15T13:30:00-06:00", cta_type="Guardar",
  cards=[
    {"type":"hook","title":"Así es como tú conviertes tu “me lo gané” del viernes…","size":88,"whisper":"[[u]]en el lunes más difícil de la semana.[[/u]]","swipe":"desliza →",
     "stains":st('rosa','tr','bl'),"doodles":[d('calendario',TL,210,-8),d('estrella',BR,170,8)]},
    {"type":"statement","title":"Te portaste bien de lunes a&nbsp;jueves.","whisper":"Entonces el viernes te das permiso: pizza, pan dulce, “total, ya me lo gané”.",
     "stains":st('menta','tl','br'),"doodles":[d('cubiertos',TR,190,8),d('corazon',BL,160,-10)]},
    {"type":"statement","title":"El lunes amaneces inflamada, con más antojo que&nbsp;nunca…","size":76,
     "whisper":"sintiendo que empiezas desde cero. [[u]]Otra vez.[[/u]]",
     "stains":st('rosa','tl','br'),"doodles":[d('reloj',TR,190,8),d('nube-pensamiento',BL,190,-6)]},
    {"type":"statement","title":"El problema no es el sábado.","whisper":"Es un lunes a jueves tan estricto que necesitas escaparte de él.",
     "stains":st('menta','tr','bl'),"doodles":[d('globo-ojo',TL,190,-8),d('espiral',BR,160,10)]},
    {"type":"statement","title":"Entonces vamos a meter tus antojos dentro de la semana, <span class=\"mark\">planeados.</span>","size":74,
     "paren":"Comer pizza no está mal; lo que cansa es [[u]]sentir que te escapas.[[/u]]",
     "stains":st('rosa','tl','br'),"doodles":[d('calendario',TR,180,8),d('check',BL,140,-8)]},
    cta("Guárdalo","Guárdalo para el viernes…","antes de tu próximo “[[u]]me lo gané[[/u]]”.",
        [d('banderin',(90,800),170,-6),d('sandia-mordida',(320,780),170,8),d('sandia',TR,190,-8)]),
  ],
  caption="""Así es como tu “me lo gané” del viernes se convierte en el lunes más difícil de la semana.

Te portaste bien de lunes a jueves. El viernes: pizza, pan dulce, “total, ya me lo gané”. Y el lunes amaneces inflamada, con más antojo que nunca, sintiendo que empiezas desde cero. Otra vez.

El problema no es el sábado. Es un lunes a jueves tan estricto que necesitas escaparte de él. Por eso vamos a meter tus antojos dentro de la semana, planeados. Comer pizza no está mal; lo que cansa es sentir que te escapas.

Guárdalo para el viernes 📌

Nutrición clínica · CDMX y online

#nutriologacdmx #nutricionclinica #nutricionpersonalizada #sinculpa #antojos"""))

# ---------- 7 · Mar 20 oct 20:30 · Atracción D · Las quejas que ojalá tengas (aspiracional, sin atribuir frases a pacientes) ----------
def pair2(top, bottom, i, pos1, pos2, dd1, dd2, size=None):
    first = 'menta' if i % 2 else 'rosa'
    c = {"type":"split","label":"Tu queja en un año","top":top,"note":"cuando hoy te preguntas…","bottom":bottom,
         "panel":"" if i % 2 else "salvia","washi":"mint" if i % 2 else "",
         "stains":st(first, pos1, pos2),"doodles":[dd1,dd2]}
    if size: c["size"] = size
    return c
P.append(dict(n=7, slug="p07-quejas-aburridas", title="Las quejas más aburridas", pillar="Atracción", arc="D · Contraste presente/futuro",
  at="2026-10-20T20:30:00-06:00", cta_type="Comentar",
  cards=[
    {"type":"hook","title":"Las quejas que ojalá tengas dentro de un&nbsp;año…","whisper":"[[u]]hoy suenan a sueño.[[/u]]","swipe":"desliza →",
     "stains":st('menta','tr','bl'),"doodles":[d('calendario',TL,210,-8),d('destellos',BR,180,8)]},
    pair2("“Qué flojera preparar mi lunch cada domingo.”","¿De verdad voy a saber qué comer sin contar calorías?!",1,'tl','br',d('tupper',TR,190,8,dy=10),d('lapiz',BL,170,-8),size=70),
    pair2("“Ya no se me antoja el pan dulce de la tarde, qué aburrido.”","¿Voy a poder pasar por la panadería sin detenerme?!",2,'tr','bl',d('cafe',TR,170,8,dy=15),d('corazon',BR,150,-8),size=70),
    pair2("“Salgo del trabajo con energía y no sé qué hacer con ella.”","¿Voy a volver a tener energía después de las 5?!",3,'tl','br',d('tenis',TR,200,6,dy=10),d('sol',BL,170,-8),size=70),
    pair2("“Ahora en mi casa me preguntan a mí qué cocinar.”","¿Algún día van a dejar de comentar lo que hay en mi plato?!",4,'tr','bl',d('plato',TR,180,8,dy=15),d('corazones-mini',BR,180,-6),size=70),
    cta("Cuéntame","Si hoy te da miedo volver a intentarlo…","¿qué queja te gustaría tener [[u]]dentro de un año?[[/u]]",
        [d('globo',(90,800),160,-8),d('estrella',(320,790),150,8),d('sandia',TR,190,-8)], first='rosa'),
  ],
  caption="""Las quejas que ojalá tengas dentro de un año… hoy suenan a sueño.

“Qué flojera preparar mi lunch cada domingo.” “Ya no se me antoja el pan dulce de la tarde, qué aburrido.” “Salgo del trabajo con energía y no sé qué hacer con ella.”

Suenan a quejas. Pero si hoy te preguntas si algún día vas a saber qué comer sin contar calorías, o si vas a volver a tener energía después de las 5, esas quejas son exactamente a donde quieres llegar.

Si hoy te da miedo volver a intentarlo: eso que te asusta puede terminar siendo tu queja más aburrida.

¿Qué queja te gustaría tener tú dentro de un año? Escríbela en comentarios 👇

Nutrición clínica · CDMX y online

#nutriologacdmx #nutricionclinica #nutricionpersonalizada #habitossaludables #comerbien"""))

# ---------- 8 · Jue 22 oct 20:30 · Autoridad A · 3 meses antes de la cirugía (2ª persona) ----------
P.append(dict(n=8, slug="p08-antes-de-la-cirugia", title="3 meses antes de la cirugía", pillar="Autoridad", arc="A · Punto de inflexión (2ª persona)",
  at="2026-10-22T20:30:00-06:00", cta_type="Compartir",
  cards=[
    {"type":"hook","title":"Tienes 3 meses antes de tu cirugía bariátrica para llegar lista…","size":84,"whisper":"[[u]]o te la reprograman.[[/u]]","swipe":"desliza →",
     "stains":st('rosa','tr','bl'),"doodles":[d('calendario',TL,210,-8),d('estetoscopio',BR,200,8)]},
    {"type":"list","title":"Tu cirujano te pidió llegar en mejores condiciones. Y lo intentas sola:","size":64,"bullet":"→","panel":"","washi":"mint",
     "items":["Dejas de cenar para “adelantar”","A las 11 pm terminas en el refri igual","Cada revisión te da más miedo"],
     "stains":st('menta','tl','br'),"doodles":[d('luna-zzz',TR,180,8,dy=5),d('reloj',BL,170,-8)]},
    {"type":"statement","title":"“Si no puedo con esto antes de operarme…","whisper":"[[u]]¿cómo voy a poder después?”[[/u]]",
     "stains":st('rosa','tl','br'),"doodles":[d('nube-pensamiento',TR,210,8),d('interrogacion',BL,150,-10)]},
    {"type":"list","title":"Entonces no hacemos una dieta de emergencia. Hacemos tu preparación:","size":62,"bullet":"✓","panel":"salvia","washi":"",
     "items":["Horarios que aguanten tu trabajo","Proteína primero, como vas a comer después","Revisiones coordinadas con tu cirujano"],
     "stains":st('menta','tr','bl'),"doodles":[d('portapapeles',TR,180,6,dy=5),d('huevo',BR,180,-8)]},
    {"type":"statement","title":"Para que llegues a tu fecha sabiendo comer como vas a comer <span class=\"mark\">el resto de tu vida.</span>","size":70,
     "whisper":"Así acompaño a cada paciente, antes y después de su cirugía.",
     "stains":st('rosa','tl','br'),"doodles":[d('corazon',TR,160,8),d('cinta-metrica',BL,190,-8)]},
    cta("Compártelo","¿Conoces a alguien que ya tiene fecha de cirugía?","Mándaselo, para que llegue preparada y [[u]]no a dieta de emergencia.[[/u]]",
        [d('celular',(90,810),140,-10),d('corazones-mini',(300,790),150,-6),d('sandia',TR,190,-8)], size=74),
  ],
  caption="""Tienes 3 meses antes de tu cirugía bariátrica para llegar lista… o te la reprograman.

Tu cirujano te pidió llegar en mejores condiciones y lo intentas sola: dejas de cenar para “adelantar”, a las 11 pm terminas en el refri igual y cada revisión te da más miedo. Y te preguntas: “si no puedo con esto antes de operarme, ¿cómo voy a poder después?”.

La preparación no es una dieta de emergencia. Son horarios que aguanten tu trabajo, proteína primero (como vas a comer después) y revisiones coordinadas con tu cirujano. Para que llegues a tu fecha sabiendo comer como vas a comer el resto de tu vida.

¿Conoces a alguien que ya tiene fecha de cirugía? Mándaselo 💌

Nutrición clínica · Bariátrica · CDMX y online

#nutriologacdmx #nutricionclinica #cirugiabariatrica #mangagastrica #nutricionpersonalizada"""))

# ---------- 9 · Mar 27 oct 13:30 · Educación C · Lo que nadie te ha revisado ----------
P.append(dict(n=9, slug="p09-lo-que-nadie-te-ha-revisado", title="Lo que nadie te ha revisado", pillar="Educación", arc="C · Denuncia educativa",
  at="2026-10-27T13:30:00-06:00", cta_type="Guardar",
  cards=[
    {"type":"hook","title":"Así es como tú le echas la culpa a tu fuerza de voluntad…","size":86,"whisper":"de algo que [[u]]nadie te ha revisado.[[/u]]","swipe":"desliza →",
     "stains":st('menta','tr','bl'),"doodles":[d('lentes',TL,220,-8),d('globo-ojo',BR,190,8)]},
    {"type":"statement","title":"La dieta no funcionó.","whisper":"Entonces, con toda la buena intención, la haces más estricta: menos tortillas, menos fruta, cero cena.",
     "stains":st('rosa','tl','br'),"doodles":[d('tortillas',TR,200,8),d('plato',BL,180,-8)]},
    {"type":"list","title":"Y aun así:","bullet":"→","panel":"salvia","washi":"",
     "items":["Cansancio a media tarde","Antojo de dulce justo después de comer","Y nada se mueve"],
     "stains":st('menta','tl','br'),"doodles":[d('reloj',TR,180,8,dy=5),d('nube-pensamiento',BL,190,-6)]},
    {"type":"list","title":"Entonces, antes de apretar más, vamos a revisar:","size":70,"label":"Estudios","panel":"","washi":"mint",
     "items":["tiroides","glucosa","insulina","hormonas"],
     "stains":st('rosa','tr','bl'),"doodles":[d('portapapeles',TR,180,6,dy=5),d('estetoscopio',BR,190,-8)]},
    {"type":"statement","title":"Si sale algo, no significa que esté mal contigo.","size":78,
     "whisper":"Significa que por fin sabemos [[u]]con qué estamos trabajando.[[/u]]",
     "stains":st('menta','tl','br'),"doodles":[d('corazon',TR,160,8),d('hojita',BL,180,-12)]},
    cta("Guárdalo","Guarda esta lista…","y llévala a tu próxima cita [[u]]con tu médico.[[/u]]",
        [d('check',(90,800),140,-8),d('calendario',(300,790),160,6),d('sandia',TR,190,-8)], first='rosa'),
  ],
  caption="""Así es como le echas la culpa a tu fuerza de voluntad de algo que nadie te ha revisado.

La dieta no funcionó, así que la haces más estricta: menos tortillas, menos fruta, cero cena. Y aun así: cansancio a media tarde, antojo de dulce justo después de comer, y nada se mueve.

Antes de apretar más, vale la pena revisar tiroides, glucosa, insulina y hormonas. Si sale algo, no significa que esté mal contigo. Significa que por fin sabemos con qué estamos trabajando.

Guarda esta lista y llévala a tu próxima cita con tu médico 📌

Nutrición clínica · CDMX y online

#nutriologacdmx #nutricionclinica #resistenciaalainsulina #hipotiroidismo #nutricionpersonalizada"""))

# ---------- 10 · Jue 29 oct 20:30 · Venta B · Lo caro no es la consulta ----------
def pc(label, top, bottom, i, dd1, dd2):
    first = 'rosa' if i % 2 else 'menta'
    return {"type":"split","label":label,"top":top,"note":"porque nadie te dijo…","bottom":bottom,"size":80,
            "panel":"salvia" if i % 2 else "","washi":"" if i % 2 else "mint",
            "stains":st(first,'tl' if i % 2 else 'tr','br' if i % 2 else 'bl'),"doodles":[dd1,dd2]}
P.append(dict(n=10, slug="p10-lo-caro-no-es-la-consulta", title="Lo caro no es la consulta", pillar="Venta", arc="B · Problema → Solución",
  at="2026-10-29T20:30:00-06:00", cta_type="Comentar",
  cards=[
    {"type":"hook","title":"No es cara la consulta…","whisper":"lo caro son los años repitiendo dietas que [[u]]no fueron hechas para tu cuerpo.[[/u]]","swipe":"desliza →",
     "stains":st('rosa','tr','bl'),"doodles":[d('cinta-metrica',TL,220,-8),d('bolsa-super',BR,200,8)]},
    pc("Lo que ya pagaste","Pagaste la app de ayuno…","que tu horario no la aguantaba.",1,d('celular',TR,150,8,dy=15),d('reloj',BL,170,-8)),
    pc("Lo que ya pagaste","Compraste las malteadas…","qué comer cuando se acabaran.",2,d('smoothie',TR,180,8,dy=10),d('tache',BR,150,-8)),
    {"type":"statement","title":"Entonces la verdad es simple: no estás fallando tú, <span class=\"mark\">está fallando el plan.</span>","size":72,
     "whisper":"Y eso tiene arreglo.",
     "stains":st('rosa','tl','br'),"doodles":[d('globo-ojo',TR,190,8),d('hojita',BL,180,-12)]},
    {"type":"statement","title":"Por eso mi consulta empieza por medirte y revisarte.","size":74,
     "whisper":"Y sales con tu plan del mes, no con una hoja de dieta.",
     "paren":"Consulta $1,000 · medidas + [[u]]plan mensual[[/u]] · CDMX y online",
     "stains":st('menta','tr','bl'),"doodles":[d('estetoscopio',TL,190,-8),d('calendario',BR,180,8)]},
    cta("Cuéntame","¿Cuántas dietas crees que llevas pagadas que no eran para ti?","Aquí [[u]]nadie juzga.[[/u]]",
        [d('globo',(90,800),160,-8),d('corazon',(310,790),140,6),d('sandia',TR,190,-8)], size=74),
  ],
  caption="""No es cara la consulta… lo caro son los años repitiendo dietas que no fueron hechas para tu cuerpo.

Pagaste la app de ayuno, porque nadie te dijo que tu horario no la aguantaba. Compraste las malteadas, porque nadie te dijo qué comer cuando se acabaran. Hiciste la dieta de tu amiga, porque nadie había revisado lo que trae tu cuerpo. Y cada intento te costó dinero, tiempo y un poco de confianza en ti.

No estás fallando tú, está fallando el plan. Y eso tiene arreglo.

Mi consulta empieza por medirte y revisarte, y sales con tu plan del mes, no con una hoja de dieta. Consulta $1,000 · medidas + plan mensual · CDMX y online.

¿Cuántas dietas crees que llevas pagadas que no eran para ti? Cuéntame en comentarios, aquí nadie juzga 👇

#nutriologacdmx #nutricionclinica #nutricionpersonalizada #dietasquenofuncionan #resistenciaalainsulina"""))

def plain(s):
    s = re.sub(r'\[\[/?u\]\]', '', s); s = re.sub(r'<br>', ' ', s); s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s).replace('\xa0', ' ').strip()

def alt(c):
    k = c['type']
    if k == 'split':
        txt = f'{c["label"]}: {c["top"]} {c["note"]} {c["bottom"]}'
    elif k == 'list':
        txt = ' '.join([c.get('title',''), c.get('body',''), c.get('label','')] + c['items'] + [c.get('paren','')])
    elif k == 'cta':
        txt = f'{c["kicker"]}. {c["title"]} {c["whisper"]}'
    else:
        txt = ' '.join([c.get('title',''), c.get('whisper',''), c.get('paren','')])
    pre = ('Tarjeta de cierre con la ilustración de la nutrióloga Annie y el logo Anaeli Álvarez. ' if k == 'cta'
           else 'Tarjeta con fondo de libreta y dibujos a mano. ')
    return pre + 'Texto: ' + re.sub(r'\s+', ' ', plain(txt))

from datetime import datetime, timezone
cal = [{"n":1,"slug":"p01-dieta-de-tu-amiga","title":"La dieta de tu amiga","at":"2026-09-29T13:30:00-06:00","status":"published",
        "media_id":"17910494430510355","permalink":"https://www.instagram.com/p/Dd4hO_wnXio/"}]
for p in P:
    spec = {"slug": p['slug'], "handle": H, "cards": p['cards']}
    (OUT/'specs'/f'p{p["n"]:02d}.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    at = datetime.fromisoformat(p['at'])
    date = p['at'][:10]
    pkg = {"piece": p['n'], "slug": p['slug'], "title": p['title'], "pillar": p['pillar'], "arc": p['arc'],
           "cta_type": p['cta_type'], "publish_at_local": p['at'],
           "publish_at_utc": at.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           "folder": f"posts/{date}-p{p['n']:02d}", "status": "pending_approval",
           "caption": p['caption'], "alt_text": [alt(c) for c in p['cards']]}
    assert len(pkg['caption']) < 2200, p['n']
    (OUT/'specs'/f'p{p["n"]:02d}.package.json').write_text(json.dumps(pkg, ensure_ascii=False, indent=1))
    cal.append({"n": p['n'], "slug": p['slug'], "title": p['title'], "at": p['at'], "status": "pending_approval"})
(OUT/'specs'/'calendario.json').write_text(json.dumps(cal, ensure_ascii=False, indent=1))
print('ok', len(P))
