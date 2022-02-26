from database import Base,engine
from models import Paciente
from models import Especialidade
from models import Indece_diario
from models import Comunidade
from models import Receita
from models import Medico
from models import Tipo
from models import Estrutura

print("Creating database ....")

Base.metadata.create_all(engine)