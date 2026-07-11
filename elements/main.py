import interface
import zodiac
def chewbacca ():
    day = int(interface.day_entry.get())
    month = int(interface.month_entry.get())
    index = zodiac.define(day, month)
    name = interface.zodiac_names[index]
    file = interface.zodiac_files[index]
    interface.name.config(text = name)
    interface.gif.config(file = f"img/{file}")
interface.Reveal_symbol.config(command = chewbacca)
interface.window.mainloop()