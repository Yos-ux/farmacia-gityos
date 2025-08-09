class Doctor:
    def __init__(self,medico_id,nombre,especialidad):
        self.medico_id = medico_id
        self.nombre = nombre
        self.especialidad = especialidad

    def presentar(self):
        return f"Doctor {self.nombre} (ID: {self.medico_id}), especidalidad: {self.especialidad}"
    
if __name__ == "__main__":
    doc = Doctor (101,"García","Cardiología")
    print(doc.presentar())