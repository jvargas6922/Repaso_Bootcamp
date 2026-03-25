1) Fundamentos del desarrollo Web.
    - Visual  -> HTML5 -> Lenguaje de Etiquetas -> Su estructura es de etiquetas de apertura y cierre
        Algunas etiquetas más utilizadas:
        <head></head> -> Contiene los metadatos de la página, como el título, enlaces a hojas de estilo, scripts, etc.
        <body></body> -> Contiene el contenido visible de la página, como texto
        <img src="ruta_recurso" alt="descripción"> -> Se utiliza para insertar imágenes en la página. El atributo "src" especifica la ruta de la imagen, mientras que el atributo "alt" proporciona una descripción alternativa de la imagen.
        <a href="url">Texto del enlace</a> -> Se utiliza para crear enlaces a otras páginas o recursos. El atributo "href" especifica la URL del destino del enlace.
        <table> -> etiqueta para la creacion de tablas en HTML
        <thead> -> Contiene la fila de encabezado de la tabla
        <th></th> ->el contenido de las tablas
        </thead>
        <tbody>
        <tr> -> crea una fila en la tabla
        <td></td> -> agreda una celda en esa fila
        </tr>
         </tbody>
         </table>
         <div></div> -> Es un contenedor genérico que se utiliza para agrupar elementos y aplicar estilos o scripts a ellos.
         <nav></nav> -> Se utiliza para definir un bloque de navegación.
         <aside></aside> -> Se utiliza para definir contenido secundario o complementario.
         <footer></footer> -> Se utiliza para definir el pie de página de un documento o sección.
         <main></main> -> Se utiliza para definir el contenido principal del documento.
         <article></article> -> Se utiliza para definir contenido independiente y autocontenido dentro de un documento.
         <p></p> -> Se utiliza para definir un párrafo de texto.
         <link> -> Se utiliza para enlazar recursos externos, como hojas de estilo CSS.
         <span></span>
         <strong></strong> -> Se utiliza para resaltar texto con un estilo de fuente más fuerte.
         <hr> -> Se utiliza para insertar una línea horizontal que actúa como un separador visual entre secciones de contenido. No requiere una etiqueta de cierre.
         <br> -> Se utiliza para insertar un salto de línea en el texto.
         <em></em> -> Se utiliza para resaltar texto con un estilo de fuente en cursiva.
         <center></center> -> Se utiliza para centrar el contenido dentro de un contenedor.
         <iframe></iframe> -> Se utiliza para incrustar otro documento HTML dentro del documento actual. Permite mostrar contenido de otras fuentes, como videos, mapas, etc.
         <form action="la ruta que resolvera la peticion" method="POST <-> GET"></form> -> Se utiliza para crear un formulario que permite a los usuarios enviar datos a un servidor. El atributo "action" especifica la URL a la que se enviarán los datos, y el atributo "method" especifica el método HTTP (GET o POST) que se utilizará para enviar los datos.
         <input> -> Se utiliza para crear campos de entrada en un formulario. El tipo de campo se especifica mediante el atributo "type", como "text" para texto, "password" para contraseñas, "email" para direcciones de correo electrónico, etc.
         <select></select> -> Se utiliza para crear un menú desplegable en un formulario. Contiene elementos <option> que representan las opciones disponibles para el usuario.
         <textarea></textarea> -> Se utiliza para crear un campo de texto de varias líneas en un formulario, permitiendo a los usuarios ingresar texto más extenso.
    - estructural -> CSS -> Lenguaje de Estilos en Cascada -> Se utiliza para definir la apariencia y el diseño de un documento HTML. Permite controlar aspectos como colores, fuentes, márgenes, etc.
        Algunas propiedades más utilizadas:
        font-family: Especifica la familia de fuentes para el texto.
        color: Define el color del texto. hexadecimal, rgb, rgba, hsl, hsla, nombres de colores
        background-color: Define el color de fondo de un elemento.
        formas de aplicar CSS a un archivo HTML:
            - CSS en linea: cuando se aplica en el mismo elemento HTML que se esta utilizando
            - Hoja de Estilos interna: Se aplica dentro de una etiqueta <style></style>
            - Hoja de Estilos Externa: Se aplica a través de un archivo CSS separado que se enlaza al documento HTML mediante la etiqueta <link>.
            - font-size: Define el tamaño del texto.
            - margin: Define el espacio alrededor de un elemento.
            - padding: Define el espacio entre el contenido de un elemento y su borde.
            text-center
            text-left
            text-right
            table > th > td -> para aplicar estilos a las tablas
    - Comportamiento -> JavaScript -> Lenguaje de Programación -> Se utiliza para agregar
    <script></script>