from tkinter import *

# Initialisation de la fenêtre
window = Tk()
window.title("Calculatrice")

# Ajouter un champ de saisie
e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Fonction pour ajouter un chiffre dans le champ de saisie
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Fonction pour effacer le champ de saisie
def button_clear():
    e.delete(0, END)


# Fonction pour effectuer les opérations mathématiques
def button_equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except ZeroDivisionError:
        e.delete(0, END)
        e.insert(0, "Erreur : division par zéro")
    except:
        e.delete(0, END)
        e.insert(0, "Erreur")


# Ajouter les boutons à la calculatrice
button_list = ['C', '/', '', 'x',
               '7', '8', '9', '-',
               '4', '5', '6', '+',
               '1', '2', '3', '',
               '0', '.', '=', '']

for i, digit in enumerate(button_list):
    if digit == '':
        continue
    button = Button(window, text=digit, padx=40, pady=20, command=lambda x=digit: button_click(x))
    if digit == 'C':
        button.config(command=button_clear)
    elif digit == '=':
        button.config(command=button_equal)
    button.grid(row=1 + i//4, column=i%4)

# Boucle principale
window.mainloop()
