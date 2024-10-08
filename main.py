from tkinter import *
from tkinter import messagebox


class RationalFraction:
    def __init__(self, x, y):
        if y == 0:
            raise ValueError("Знаменатель дроби не может быть равен 0")
        self.x = x
        self.y = y

    @staticmethod
    def commonDivider(t, h):
        while h != 0:
            t, h = h, t % h
        return t

    def printt(self):
        k = self.commonDivider(self.x, self.y)
        return f"{self.x // k}/{self.y // k}"

    def multiply1(self, other):
        xx = self.x * other.x
        yy = self.y * other.y
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def division1(self, other):
        if other.x == 0:
            raise ZeroDivisionError("Нельзя разделить на дробь, числитель которой равен 0")
        xx = self.x * other.y
        yy = self.y * other.x
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def addition1(self, other):
        if self.y == other.y:
            xx = self.x + other.x
            yy = self.y
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"
        else:
            xx = self.x * other.y + other.x * self.y
            yy = self.y * other.y
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"

    def subtraction1(self, other):
        if self.y == other.y:
            xx = self.x - other.x
            yy = self.y
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"
        else:
            xx = self.x * other.y - other.x * self.y
            yy = self.y * other.y
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"

    def multiply2(self, n):
        xx = self.x * n
        yy = self.y
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def division2(self, n):
        xx = self.x
        yy = self.y * n
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def addition2(self, n):
        xx = self.x + n * self.y
        yy = self.y
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def subtraction2(self, n):
        xx = self.x - n * self.y
        yy = self.y
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def power(self, n):
        if n >= 0:
            xx = self.x ** n
            yy = self.y ** n
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"
        else:
            xx = self.y ** (-n)
            yy = self.x ** (-n)
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"


root = Tk()
root.title("Fraction Calculator")
root.geometry("400x400")
root['bg'] = 'light blue'

disp = StringVar()
dis = Entry(root, textvariable=disp, font=("Arial", 18), width=20, borderwidth=2, relief="solid")
dis.pack(side=TOP, pady=10)


def button_click(x):
    res = None
    operan = None
    if x == 'C':
        disp.set('')
    elif x == '=':
        try:
            c = dis.get()
            if '+' in c:
                k, n = c.split('+')
                operan = '+'
            elif '÷' in c:
                k, n = c.split('÷')
                operan = '÷'
            elif '*' in c:
                k, n = c.split('*')
                operan = '*'
            elif '—' in c:
                k, n = c.split('—')
                operan = '—'
            elif '^' in c:
                k, n = c.split('^')
                operan = '^'
                print(k, n)

            if '/' in k:
                a, b = k.split('/')
            else:
                messagebox.showerror("Ошибка", "Первое введенное число должно быть дробью")
                return

            if '/' in n:
                c, d = n.split('/')
                x = RationalFraction(int(a), int(b))
                y = RationalFraction(int(c), int(d))
                if operan == '+':
                    res = x.addition1(y)
                elif operan == '—':
                    res = x.subtraction1(y)
                elif operan == '*':
                    res = x.multiply1(y)
                elif operan == '÷':
                    res = x.division1(y)
            if '/' not in n:
                x = RationalFraction(int(a), int(b))
                y = int(n)
                if operan == '+':
                    res = x.addition2(y)
                elif operan == '—':
                    res = x.subtraction2(y)
                elif operan == '*':
                    res = x.multiply2(y)
                elif operan == '÷':
                    res = x.division2(y)
                elif operan == '^':
                    res = x.power(y)
            disp.set(f'{res}')
        except ZeroDivisionError as e:
            messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")
        except ValueError as e:
            messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неизвестная ошибка: {str(e)}")
    elif x == '+-':
        disp.set(disp.get() + '-')
    else:
        disp.set(disp.get() + x)


buttons = [
    ['7', '8', '9', 'C'],
    ['4', '5', '6', '÷'],
    ['1', '2', '3', '*'],
    ['0', '^', '+', '—'],
    ['+-', '/', '=']
]

frame = Frame(root, bg='light grey')
frame.pack(side=BOTTOM, fill=X, padx=5, pady=5)
frame['bg'] = 'light blue'
rc = 0
for row in buttons:
    cc = 0
    for text_btn in row:
        btn = Button(frame, text=text_btn, bg='grey', width=5, height=2, command=lambda x=text_btn: button_click(x))
        btn.grid(row=rc, column=cc, padx=5, pady=5)
        cc += 1
    rc += 1
root.mainloop()