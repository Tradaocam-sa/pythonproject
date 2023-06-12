class Person:
  def __init__(self, n, a):
    self.name = n
    self.age = a
  def describe(self):
      print("Name:", self.name)
      print("Age:", self.age)
  def __lt__(self, other):
      return self.age < other.age
  def __str__(self):
      return f"My name is {self.name}. I am {self.age}."


class President(Person):
    def set_term(self, term):
        print(f"Setting term to {term}")
        self.term = term
# macron = Person("Emmanuel Macron", 43)
# macron.describe()
# print(macron)
# biden = Person("Joe Biden", 78)
# print(f"Macron is younger: {macron < biden}")

print("Macron is now President")
macron = President("Emmanuel Macron", 43)
macron.set_term(25) # from President
macron.describe()
