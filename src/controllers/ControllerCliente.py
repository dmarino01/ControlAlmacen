from models import Cliente

class ControllerCliente:

    @classmethod
    def getClientes(cls):
        try:
            clientes = Cliente.query.all()
            return clientes
        except Exception as e:
            print(f"Error fetching clientes: {e}")
            return []
