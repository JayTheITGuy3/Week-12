from breezypythongui import EasyFrame
from tkinter import PhotoImage
from customcards import CustomDeck


class CardDealing(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, width=420, height=400, title="Random Card Dealing")
        self.card1 = CustomDeck()
        print(self.card1)
        self.cardLabel1 = self.addLabel(text="", row=0, column=0, sticky="NSEW")

        self.refreshImages()

    def refreshImages(self):
        """Updates the images in the window."""
        fileName1 = "1s.gif"
        self.image1 = PhotoImage(file=fileName1)
        self.cardLabel1["image"] = self.image1

    def deal(self):
        """Removes and returns the top card or None 
        if the deck is empty."""
        if len(self) == 0:
           return None
        else:
           return self.card1.pop(0) 


def main():
    CardDealing().mainloop()


if __name__ == "__main__":
    main()
