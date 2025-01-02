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

def feedback_form():
                return rx.cond(
                    TextAreaFeedbackState.submitted,
                    rx.card(
                        rx.vstack(
                            rx.text("¡Gracias por tu aporte!"),
                            rx.button(
                                "¿Tienes algo más que avisar?",
                                on_click=TextAreaFeedbackState.reset_form,
                            ),
                        ),
                    ),
                    rx.card(
                        rx.form(
                            rx.flex(
                                rx.text("¿Tienes algún aviso por hacer?"),
                                rx.text_area(
                                    placeholder="Escribe aquí...",
                                    value=TextAreaFeedbackState.feedback,
                                    on_change=TextAreaFeedbackState.set_feedback,
                                    resize="vertical",
                                ),
                                rx.button("Enviar", type="submit"),
                                direction="column",
                                spacing="3",
                            ),
                            on_submit=TextAreaFeedbackState.submit_feedback,
                        ),
                    ),
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

            rx.text("Listado de bibliotecas:\n", style={'color': 'Orange'}),
            
            #rx.list(
                #rx.list.item('Biblioteca Central'),
                #rx.list.item('Facultad de Administración y Economía'),
                #rx.list.item('Facultad de Arquitectura y Ambiente Construido'),
                #rx.list.item('Facultad de Ciencias Médicas'),
                #rx.list.item('Facultad de Derecho'),
                #rx.list.item('Facultad de Humanidades'),
                #rx.list.item('Facultad de Química y Biología'),
                #rx.list.item('Departamento de Física'),
                #rx.list.item('Departamento de Ingeniería Eléctrica'),
                #rx.list.item('Departamento de Ingeniería GeoEspacial y Ambiental'),
                #rx.list.item('Departamento de Ingeniería Industrial'),
                #rx.list.item('Departamento de Ingeniería Informática'),
                #rx.list.item('Departamento de Ingeniería Mecánica'),
                #rx.list.item('Departamento de Ingeniería en Minas'),
                #rx.list.item('Departamento de Matemáticas y Ciencias de la Computación'),
                #rx.list.item('Escuela de Periodismo'),
                #rx.list.item('Facultad Tecnológica'),
                #rx.list.item('Instituto de Estudios Avanzados'),

            #),
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
            rx.link("Facultad Tecnológica", href="/TECNOLOGICA", style={"color": "sky blue", "text-decoration": "underline"}),
            rx.link("Instituto de Estudios Avanzados", href="/ESTUDIOS_AVANZADOS", style={"color": "sky blue", "text-decoration": "underline"}),

        
            
            )
        )



#Definimos paginas para las bibliotecas():
def pagina_nueva() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text('Biblioteca', front_size = "2em", front_weight="bold"),
            feedback_form(),
            rx.text('Avisos'),
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
app.add_page(pagina_nueva, route="/ESTUDIOS_AVANZADOS")




