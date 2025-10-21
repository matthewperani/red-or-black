import socketserver
from deck import CardDeck, Card

class CardDealerServer(socketserver.StreamRequestHandler):

    def __init__(self, request, client_address, server):
        self.deck = CardDeck()
        super().__init__(request, client_address, server)

    def handle(self):
        try:
            while True:
                self.data = self.rfile.readline(10000).rstrip()
                print(f"{self.client_address[0]} sent: ")
                print(self.data.decode("utf-8"))

                card = self.deck.draw()

                print(card)
                if card == None:
                    self.deck.shuffle()
                    card = self.deck.draw()
                    self.wfile.write(f"Deck is empty.  Starting new deck.  Your card is the {card.value} of {card.suit}.  {len(self.deck.deck)} cards remain.".encode("utf-8"))
                else:    
                    self.wfile.write(f"Your card is the {card.value} of {card.suit}.  {len(self.deck.deck)} cards remain.".encode("utf-8"))

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), CardDealerServer) as server:
        server.serve_forever()