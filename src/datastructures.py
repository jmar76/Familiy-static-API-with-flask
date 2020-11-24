
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

    # def __init__(self, last_name, pepito, miedos = 321): 
        # self.abuelos = pepito
        # self.abuelos es un atributo de mi clase y pepito es su valor inicial
        # la convencion es nombrar igual el valor inicial y el atributo de la clase
        # self.miedos = miedos y va a valer 321 si no le paso nada afuera 
        

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["last_name"] = self.last_name

        if 'id' not in member:
            member['id'] = self._generateId()

        self._members.append(member)

    def delete_member(self, id):
        miembro = self.get_member(id) # primero le pedimos que nos busque el miembro con la fn get_members()
        if miembro: # si valida miembro como true, ed., que es NOT NONE, devuelve miembro y lo elimina de self._members
            self._members.remove(miembro)
            return miembro

    def get_member(self, id):
        for miembro in self._members:
            if miembro['id'] == id: #aquí ya tenemos un if, de que si nos devuelve un id que existe nos devuelve un diccionario de la lista, no devuelve nada
                return miembro       

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
