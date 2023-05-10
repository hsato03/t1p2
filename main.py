from controllers.main_controller import SistemaController
from model.cachorro import Cachorro

if __name__ == "__main__":
    cachorro = Cachorro(None, None, None, None)
    print(isinstance(cachorro, Cachorro))
    sc = SistemaController()
    sc.inicializa_sistema()
