import turtle  # Importera turtle.

# 80 character line
################################################################################


class Gris:
    """Översatt version av turtle för att elever som inte förstår engelska 
	tillräckligt bra ska kunna använda turtle biblioteket."""
    def __init__(self, rubrik="Gris"):
        """Konstruktor. Sätter upp miljön."""
        self.fonster = turtle.Screen(
        )  # Se till att turtle fyller hela skärmen
        self.rubrik(rubrik)  # Ställ in rubriken
        """Maximera storleken. Ett problem är att om fönstret inte är ordentligt 
		maximerat så att om skärmstorleken ändras så kommer inte 
		fönstret "hänga med". Inte prio 1 men eventuellt vore det bra att 
        fixa."""
        self.fonster.setup(width=1.0, height=1.0, startx=0, starty=0)

        # Skapa en turtle-penna som Gris kan kontrollera.
        self.t = turtle.Turtle()

        turtle.listen()

    # Saker relaterat till fönster.

    def rubrik(self, rubrik):
        """Ställ in fönstrets rubrik till rubrik."""
        self.fonster.title(rubrik)

    def bakgrund_farg(self, r, g, b):
        """Ställ in bakgrundsfärgen till r,g,b."""
        self.fonster.bgcolor("#{:02x}{:02x}{:02x}".format(r, g, b))

    def rensa(self):
        """Rensar skärmen så att alla linjer som ritats försvinner."""
        self.t.clear()

    # Saker relaterat till händelser.

    def musklickad(self, respons):
        """Ställ in så att det händer någonting om användaren trycker på 
        musen."""
        self.fonster.onclick(respons)

    def musdragen(self, respons):
        """Ställ in så att det händer någonting om användaren drar pennan med 
        musen."""
        self.t.ondrag(respons)

    # Saker relaterat till pennan.

    def hastighet(self, speed):
        """Byt pennans hastighet. Hastighetsskala från 1 till 1000. Stäng av 
        animation med 0 (snabbast så)."""
        self.t.speed(speed)

    def fram(self, s):
        """Dra pennan frammåt en sträcka av längden s."""
        self.t.forward(s)

    def bak(self, s):
        """Dra pennan bakåt en sträcka av längden s."""
        self.t.backward(s)

    def sv_vanster(self, v):
        """Vrid pennan åt vänster v grader."""
        self.t.left(v)

    def sv_hoger(self, vinkel):
        """Vrid pennan åt höger v grader."""
        self.t.right(vinkel)

    def penna_up(self):
        """Lyft pennan från pappret."""
        self.t.penup()

    def penna_ner(self):
        """Släpp ner pennan på pappret."""
        self.t.pendown()

    def penna_farg(self, r, g, b):
        """Byt pennans färg."""
        self.t.color("#{:02x}{:02x}{:02x}".format(r, g, b))

    def penna_synlig(self, synlighet=True):
        """Göm pilen med synlighet=False och visa den med synlighet=True. Om 
        inget argument angivits blir pennan synlig."""
        if synlighet == False: self.t.hideturtle()
        if synlighet == True: self.t.showturtle()

    def hem(self):
        """Flyttar tillbaka pennan till där den började på x=0, y=0 (mitt i 
        skärmen från början)."""
        self.t.home()

    def flytta(self, x, y):
        """Flytta pennan till koordinaterna x,y."""
        self.t.goto(x, y)

    def riktning(self):
        """Svarar med vilken riktning pennan pekar i."""
        return self.t.heading()

    def xkoordinat(self):
        """Svarar med vilken x-koordinat pennan har."""
        return self.t.xcor()

    def ykoordinat(self):
        """Svarar med vilken y-koordinat pennan har."""
        return self.t.ycor()

    def penna_storlek(self, bredd=None):
        """Ställ in pennans bredd till värdet i variabeln bredd eller ange 
        ingen bredd så lämnas pennans storlek tillbaka."""
        if bredd == None:
            return self.t.pensize()
        else:
            self.t.pensize(bredd)

    def knapp_tryckt(self, respons, tangent):
        self.fonster.onkey(respons, tangent)
