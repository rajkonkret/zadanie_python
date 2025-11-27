import tkinter as tk

class CalculatorEngine:
    """Klasa odpowiedzialna wyłącznie za logikę obliczeń."""
    def calculate(self, expression):
        try:
            # W bezpiecznej aplikacji produkcyjnej unika się eval(), ale tutaj wystarczy
            return str(eval(expression))
        except Exception:
            return "Błąd"

class CalculatorApp:
    """Klasa odpowiedzialna wyłącznie za interfejs użytkownika."""
    def __init__(self, root, engine):
        self.root = root
        self.engine = engine
        self.root.title("Kalkulator")
        self.root.geometry("400x500")

        self.input_text = tk.StringVar()

        self._setup_ui()
        self._bind_keys()

    def _setup_ui(self):
        # Ekran
        self.display_frame = self._create_display()
        self.display_frame.pack(side=tk.TOP, fill=tk.X)

        # Przyciski
        self.buttons_frame = self._create_buttons()
        self.buttons_frame.pack(fill=tk.BOTH, expand=True)

    def _bind_keys(self):
        self.root.bind('<Return>', lambda event: self.btn_equal())

    def _create_display(self):
        frame = tk.Frame(self.root, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_field = tk.Entry(frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bg="#eee", bd=0, justify=tk.RIGHT, fg="black")
        input_field.pack(fill=tk.BOTH, expand=True, ipady=10)
        return frame

    def _create_buttons(self):
        frame = tk.Frame(self.root, bg="grey")
        
        # Konfiguracja skalowania siatki (grid)
        for i in range(5):  # 5 wierszy
            frame.rowconfigure(i, weight=1)
        for i in range(4):  # 4 kolumny
            frame.columnconfigure(i, weight=1)

        # Definicja układu: (tekst, wiersz, kolumna, szerokość, opcjonalna_funkcja)
        # Jeśli funkcja to None, domyślnie wpisuje znak.
        layout = [
            ("C", 0, 0, 3, self.btn_clear), ("/", 0, 3, 1, None),
            ("7", 1, 0, 1, None), ("8", 1, 1, 1, None), ("9", 1, 2, 1, None), ("*", 1, 3, 1, None),
            ("4", 2, 0, 1, None), ("5", 2, 1, 1, None), ("6", 2, 2, 1, None), ("-", 2, 3, 1, None),
            ("1", 3, 0, 1, None), ("2", 3, 1, 1, None), ("3", 3, 2, 1, None), ("+", 3, 3, 1, None),
            ("0", 4, 0, 2, None), (".", 4, 2, 1, None), ("=", 4, 3, 1, self.btn_equal),
        ]

        for item in layout:
            text, row, col, colspan, cmd = item
            # Jeśli nie podano specjalnej komendy, użyj standardowego kliknięcia
            command = cmd if cmd else lambda t=text: self.btn_click(t)
            self._add_button(frame, text, row, col, colspan, command)

        return frame

    def _add_button(self, frame, text, row, col, colspan, command):
        tk.Button(frame, text=text, fg="black", bd=0, bg="#fff", cursor="hand2", command=command).grid(row=row, column=col, columnspan=colspan, padx=1, pady=1, sticky="nsew")

    def btn_click(self, item):
        current_text = self.input_text.get()
        self.input_text.set(current_text + str(item))

    def btn_clear(self):
        self.input_text.set("")

    def btn_equal(self):
        expression = self.input_text.get()
        result = self.engine.calculate(expression)
        self.input_text.set(result)

if __name__ == "__main__":
    root = tk.Tk()
    # Wstrzykiwanie zależności (Dependency Injection)
    engine = CalculatorEngine()
    app = CalculatorApp(root, engine)
    root.mainloop()
