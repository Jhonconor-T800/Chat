#chat

import tkinter as tk
import webbrowser
 
# Crear la ventana
ventana = tk.Tk()
ventana.geometry("700x600")
ventana.title("Chat")
ventana.configure(bg="#39FF14")  # borde verde

# Frame interior (contenido negro)
contenedor = tk.Frame(ventana, bg="black")
contenedor.pack(padx=3, pady=3, fill="both", expand=True)

# Diccionario de emojis
emojis = {
    "fuego": "🔥",
    "risa": "😂",
    "corazon": "❤️",
    "ok": "👌",
    "triste": "😢",
    "gato": "🐱",
    "perro": "🐶",
    "robot": "🤖",
    "Pc": "💻",
    "Si": "✅",
    "No": "❌"
}

# Crear etiqueta
etiqueta = tk.Label(contenedor, text="", font=("Arial", 15), bg="black", fg="#39FF14", wraplength=650, justify="left")
etiqueta.pack(pady=20)

# Campo de texto
campo_texto = tk.Entry(contenedor, font=("Arial", 20), bg="black", fg="#39FF14", insertbackground="#39FF14")
campo_texto.pack(pady=10, fill="x", padx=10)

# Frame para botones
panel_botones = tk.Frame(contenedor, bg="black")
panel_botones.pack(pady=20)

# Datos
Numeros = [1,2,3,4,5,6,7,8,9,10]
TEXTO = "Lo siento Mario, la princesa está en otro castillo"

# Función principal del chat
def actualizar_etiquetas():
    texto = campo_texto.get()

    # COMANDO GIF
    if texto.startswith("/gif"):
        busqueda = texto.replace("/gif", "").strip()
        url = f"https://www.google.com/search?tbm=isch&q={busqueda}+gif"
        webbrowser.open(url)
        etiqueta.config(text=f"🔎 Buscando GIF de: {busqueda}")

    # COMANDO GOOGLE
    elif texto.startswith("/g"):
        busqueda = texto.replace("/g", "").strip()
        url = f"https://www.google.com/search?q={busqueda}"
        webbrowser.open(url)
        etiqueta.config(text=f"🌐 Buscando en Google: {busqueda}")

    # COMANDO EMOJI
    elif texto.startswith("/emoji"):
        palabra = texto.replace("/emoji", "").strip().lower()
        emojis = emojis.get(palabra, "❓")
        etiqueta.config(text=emojis)

    # TEXTO NORMAL
    else:
        etiqueta.config(text=texto)

    campo_texto.delete(0, tk.END)

# Función auto rellenar números
def auto_rellenar():
    texto = " ".join(str(num) for num in Numeros)
    campo_texto.delete(0, tk.END)
    campo_texto.insert(0, texto)

# Función texto fijo
def poner_texto():
    campo_texto.delete(0, tk.END)
    campo_texto.insert(0, TEXTO)
#Crear minijuego de pin pon
# Crear minijuego de Pong
def juego_pong():
    juego = tk.Toplevel(ventana)
    juego.title("Pong")
    juego.geometry("600x400")
    juego.configure(bg="black")

    canvas = tk.Canvas(juego, width=600, height=400, bg="black", highlightthickness=0)
    canvas.pack()

    
    

    # Jugador
    pala = canvas.create_rectangle(20, 150, 35, 250, fill="white")

    # Pelota
    pelota = canvas.create_oval(290, 190, 310, 210, fill="white")

    dx = 4
    dy = 4

    def mover(event):
        y = canvas.coords(pala)[1]
        if event.keysym == "Up" and y > 0:
            canvas.move(pala, 0, -20)
        elif event.keysym == "Down" and y < 300:
            canvas.move(pala, 0, 20)

    juego.bind("<Up>", mover)
    juego.bind("<Down>", mover)

    def actualizar():
        nonlocal dx, dy

        canvas.move(pelota, dx, dy)
        x1, y1, x2, y2 = canvas.coords(pelota)

        # Rebote arriba y abajo
        if y1 <= 0 or y2 >= 400:
            dy *= -1

        # Rebote en la pala
        px1, py1, px2, py2 = canvas.coords(pala)
        if x1 <= px2 and py1 <= y1 <= py2:
            dx *= -1

        # Rebote pared derecha
        if x2 >= 600:
            dx *= -1

        # Si pierde
        if x1 <= 0:
            canvas.create_text(
                300, 200,
                text="GAME OVER",
                fill="red",
                font=("Arial", 30)
            )
            return

        juego.after(20, actualizar)

    actualizar()

# Botones
boton = tk.Button(panel_botones, text="Mostrar texto", command=actualizar_etiquetas,   font=("Arial", 20), bg="black", fg="white")
boton.pack(side="left", padx=10)

boton_auto = tk.Button(panel_botones, text="Auto Rellenar", command=auto_rellenar,  font=("Arial", 20), bg="black", fg="white")
boton_auto.pack(side="left", padx=10)

boton_texto = tk.Button(panel_botones, text="Texto Mario", command=poner_texto,   font=("Arial", 20), bg="black", fg="white")
boton_texto.pack(side="left", padx=10)
Boton_Juego = tk.Button(panel_botones, text="Juego", command=juego_pong, font=("Arial", 20), bg="black", fg="white")
Boton_Juego.pack(side="left", padx=10)

# Ejecutar
ventana.mainloop()