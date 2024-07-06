class Account:
    def __init__(self, type, id, name, ownership, balance):
        self.type = type
        self.id = id
        self.name = name
        self.balance = balance
        self.ownership = ownership
        self.emoji = name.split(' ')[0]
    
    def __repr__(self):
        return f"<Account(id={self.id}, type={self.type}, name={self.name}, emoji={self.emoji}, ownership={self.ownership}, balance={self.balance}>"
    