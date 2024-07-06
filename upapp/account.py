class Account:
    def __init__(self, type, id, name, ownership, balance):
        self.type = type
        self.id = id
        self.balance = balance
        self.ownership = ownership
        
        if self.type == "TRANSACTIONAL":
            self.emoji = "$$"
            self.name = name
        else:
            self.emoji = name.split()[0]
            self.name = " ".join(name.split()[1:])
    
    def __repr__(self):
        return f"<Account(id={self.id}, type={self.type}, name={self.name}, emoji={self.emoji}, ownership={self.ownership}, balance={self.balance}>"
    