import interface
import generator
def generate():
    interface.entry.delete(0, "end")
    password = generator.generate_password(interface.lowercase.get(), interface.numbers.get(), interface.uppercase.get(), interface.symbols.get(),)
    interface.entry.insert("end", password)
interface.button.config(command = generate)
interface.window.mainloop()