import reflex as rx

from rxconfig import config

class TextAreaFeedbackState(rx.State):
                feedback: str = ""
                submitted: bool = False

                @rx.event
                def submit_feedback(self, form_data: dict):
                    self.submitted = True

                @rx.event
                def reset_form(self):
                    self.feedback = ""
                    #self.attach_screenshot = True
                    self.submitted = False

class DynamicFormState(rx.State):
    form_data: dict = {}
    form_fields: list[str] = [
        "Nombre",
        "Apellido",
        "correo",
        "Comentario"

    ]

    @rx.var(cache=True)
    def form_field_placeholders(self) -> list[str]:
        return [
            " ".join(
                w.capitalize() for w in field.split("_")
            )
            for field in self.form_fields
        ]

    @rx.event
    def add_field(self, form_data: dict):
        new_field = form_data.get("new_field")
        if not new_field:
            return
        field_name = (
            new_field.strip().lower().replace(" ", "_")
        )
        self.form_fields.append(field_name)

    @rx.event
    def handle_submit(self, form_data: dict):
        self.form_data = form_data


def dynamic_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.foreach(
                    DynamicFormState.form_fields,
                    lambda field, idx: rx.input(
                        placeholder=DynamicFormState.form_field_placeholders[
                            idx
                        ],
                        name=field,
                    ),
                ),
                rx.button("Enviar", type="submit"),
            ),
            on_submit=DynamicFormState.handle_submit,
            reset_on_submit=True,
        ),
        
        rx.divider(),
        rx.heading("Último comentario", color= "Purple"),
        rx.text(DynamicFormState.form_data.to_string()),
    )
#Definimos la pagina principal
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text(
            "¡Bienvenido a encuentra bibliotecas!",
            font_size='3em',
            color='blue'
        ),

            
            rx.text('Aqui encontrarás información acerca de la disponibilidad de las bibliotecas que frecuentas dentro de la universidad', style={'color': 'Green','font_size': '2.5em'}),

            rx.text("Listado de bibliotecas:\n", style={'color': 'Orange','font_size': '2em'}),
    

            rx.link("Biblioteca Central", href="/biblioteca_central", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Facultad de Administración y Economía", href="/fae", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Facultad de Arquitectura y Ambiente Construido", href="/ARQUITECTURA", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Facultad de Ciencias Médicas", href="/CIENCIAS_MEDICAS", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Facultad de Derecho", href="/derecho", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Facultad de Humanidades", href="/HUMANIDADES", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Facultad de Química y Biología", href="/QUIMICA_Y_BIOLOGIA", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Departamento de Física", href="/D_FISICA", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Departamento de Ingeniería Eléctrica", href="/D_ELECTRICA", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Departamento de Ingeniería GeoEspacial y Ambiental", href="/D_GEOESPACIAL", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Departamento de Ingeniería Industrial", href="/D_INDUSTRIAL", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Departamento de Ingeniería Informática", href="/D_INFORMATICA", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Departamento de Ingeniería Mecánica", href="/D_MECANICA", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Departamento de Ingeniería en Minas", href="/D_MINAS", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Departamento de Matemáticas y Ciencias de la Computación", href="/D_MATEMATICAS", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Escuela de Periodismo", href="/PERIODISMO", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Facultad Tecnológica", href="/TECNOLOGICA", style={"color": "sky blue", "text-decoration": "underline"})

        
            
            )
        )



#Definimos paginas para las bibliotecas():
def pagina_nueva() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text('Biblioteca', font_size = "2em", font_weight="bold", color="yellow"),
            #feedback_form(),
            rx.text('Avisos', font_size= '1.5em', font_weight='bold', color='yellow'),
            dynamic_form(),

            rx.link("Volver a la página principal", href="/", style={"color": "sky blue", "text-decoration": "underline"}),
        
        )
    )

app = rx.App()
app.add_page(index)
app.add_page(pagina_nueva, route="/BIBLIOTECA_CENTRAL") 
app.add_page(pagina_nueva, route="/FAE")
app.add_page(pagina_nueva, route="/ARQUITECTURA")
app.add_page(pagina_nueva, route="/CIENCIAS_MEDICAS")
app.add_page(pagina_nueva, route="/DERECHO")
app.add_page(pagina_nueva, route="/HUMANIDADES")
app.add_page(pagina_nueva, route="/QUIMICA_Y_BIOLOGIA")
app.add_page(pagina_nueva, route="/D_FISICA")
app.add_page(pagina_nueva, route="/D_ELECTRICA")
app.add_page(pagina_nueva, route="/D_GEOESPACIAL")
app.add_page(pagina_nueva, route="/D_INDUSTRIAL") 
app.add_page(pagina_nueva, route="/D_INFORMATICA")
app.add_page(pagina_nueva, route="/D_MECANICA")
app.add_page(pagina_nueva, route="/D_MINAS")
app.add_page(pagina_nueva, route="/D_MATEMATICAS")
app.add_page(pagina_nueva, route="/PERIODISMO")
app.add_page(pagina_nueva, route="/TECNOLOGICA")
