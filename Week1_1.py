"""class TaxBand:
    def __init__(self):
        self.rules = []

    def addRules(self, condition, statement):
        self.rules.append((condition, statement))
    
    def FindYourTaxBand(self, income):
        for condition, result in self.rules:
            if condition(income):
                return result
        return "Falls under personal allowence. You are taxed 0% on your income."
    

Taxer = TaxBand()
Taxer.addRules(lambda x: x > 125140, "Falls under Additionall rate. Yor are taxed 45% on your income.")
Taxer.addRules(lambda x: x>50271 and x < 125140, "Falls under Higher rate. You are taxed 40% on your income.")
Taxer.addRules(lambda x: x > 12570 and x < 50271, "Falls under Basic rate. You are taxed 20% on your income.")

print(Taxer.FindYourTaxBand())"""

class ChatBot:
    def __init__(self):
        self.rules = []

    def addRules(self, condition, response):
        self.rules.append((condition, response))

    def applyRules(self, input):
        for condition, result in self.rules:
            if condition(input):
                return result
        return "Sorry I don't understand"
    
bot = ChatBot()
bot.applyRules("hello", "Hi there!")
bot.applyRules("goodbye", "Goodbye!")

print("Bot: Hello, how are you.")

while True:
    user_input = input("You: ")
    response = bot.applyRules(user_input)
    if response.lower() == "bye":
        print("Byee!")
        break
    print(f"Bot: {response}")


