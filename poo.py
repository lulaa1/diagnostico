class Vehiculo:
def__init__( self, patente, marca, modelo, kilometraje):
self.patente= patente
self.marca= marca
self.modelo= modelo
self.kilometraje= kilometraje

def get_patente (self)
return self.patente

def set_kilometraje ( self, nuevo_kilometraje):
  self.kilometraje = nuevo_kilometraje
  print ("El kilometraje ha sido actualizado.")
