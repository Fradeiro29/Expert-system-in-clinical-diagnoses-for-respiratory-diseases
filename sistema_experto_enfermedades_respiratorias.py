## Imports
from utils import *
from logic import *

# Función que separa los string en pabras que empiezan con mayúsculas
def splitcap(string_value):
    result = [string_value[0]] 
    for char in string_value[1:]:
        if char.isupper():
            result.extend([' ', char])
        else:
            result.append(char)
    return ''.join(result).lower()

# Función que pregunta al usuario si presenta un síntoma en específico
def pregunta(x, name):
    if (input('¿Presentas {}?\n'.format(splitcap(x))).lower() == 's'):
        kb.tell(expr('Presenta({}, {})'.format(name, x)))
        return 1
    else:
        return 0
    

# Lista de síntomas
ListaSintomas = ['Nada', 'Tos', 'Fiebre', 'DolorDeGarganta', 'CongestiónNasal', 'Estornudos', 'TosPersistente', 'DolorDeCabeza', 'DolorMuscular', 'Fatiga', 'Flemas', 'DificultadParaRespirar', 'DolorDePecho', 'Sudoracion', 'Nauseas', 'Vomito', 'TosConFlemas', 'Sibilancias', 'TosSeca', 'PerdidaDePeso', 'Hinchazon', 'Mareos', 'Desmayos', 'LatidosIrregulares', 'InfeccionesRespiratoriasFrecuentes', 'TosConSangre', 'Ronquera', 'Cansancio', 'DolorEnHuesos', 'HinchazonPies', 'HinchazonTobillos', 'HinchazonPiernas']
# Lista de enfemedades
ListaRecomendaciones = ['LavarManos', 'EvitarContactoEnfermos', 'CubrirBocaNariz', 'VacunarseGripe', 'VacunarseNeumonia', 'EvitarIrritantesPulmonares', 'ControlarAsmaMedico', 'SeguirPlanTratamientoAsma', 'IdentificarEvitarDesencadenantesAsma', 'DejarFumar', 'HacerEjercicioRegularmente', 'VacunarseGripeNeumonía', 'MantenerPesoSaludable', 'ControlarAfeccionesMedicas', 'VacunarseGripeNeumonia', 'DietaSaludable', 'NoFumar', 'Medicamentos', 'Oxigenoterapia', 'Cirugía']



#------------------------------------------------------------------------------------------------------------------------------Clausulas------------------------------------------------------------------------------------------------------------------------------
clauses  = []

### Enfermedades

# Nada
clauses.append(expr("Presenta(x, Nada) ==> Enfermo(x, Gonorrea)"))

# Resfriado
clauses.append(expr("Presenta(x, Tos) & Presenta(x, Fiebre) & Presenta(x, DolorDeGarganta) & Presenta(x, CongestiónNasal) & Presenta(x, Estornudos) ==> Enfermo(x, Resfriado)"))

# Gripe
clauses.append(expr("Presenta(x, TosPersistente) & Presenta(x, Fiebre) & Presenta(x, DolorDeGarganta) & Presenta(x, DolorDeCabeza) & Presenta(x, DolorMuscular) & Presenta(x, Fatiga) ==> Enfermo(x, Gripe)"))

# Neumonia
clauses.append(expr("Presenta(x, Flemas) & Presenta(x, Fiebre) & Presenta(x, DificultadParaRespirar) & Presenta(x, DolorDePecho) & Presenta(x, Sudoracion) & Presenta(x, Fatiga) & Presenta(x, Nauseas) & Presenta(x, Vomito) ==> Enfermo(x, Neumonia)"))

# Bronquitis
clauses.append(expr("Presenta(x, TosConFlemas) & Presenta(x, Sibilancias) & Presenta(x, DificultadParaRespirar) & Presenta(x, DolorDePecho) & Presenta(x, Fiebre) ==> Enfermo(x, Bronquitis)"))

# Asma
clauses.append(expr("Presenta(x, Sibilancias) & Presenta(x, DificultadParaRespirar) & Presenta(x, DolorDePecho) ==> Enfermo(x, Asma)"))

# Fibrosis Pulmonar
clauses.append(expr("Presenta(x, TosPersistente) & Presenta(x, TosSeca) & Presenta(x, DificultadParaRespirar) & Presenta(x, Fatiga) & Presenta(x, DolorDePecho) & Presenta(x, PerdidaDePeso) & Presenta(x, Hinchazon) ==> Enfermo(x, FibrosisPulmonar)"))

# Hipertension Pulmonar
clauses.append(expr("Presenta(x, DificultadParaRespirar) & Presenta(x, Fatiga) & Presenta(x, DolorDePecho) & Presenta(x, Mareos) & Presenta(x, Desmayos) & Presenta(x, Hinchazon) & Presenta(x, LatidosIrregulares) ==> Enfermo(x, HipertensiónPulmonar)"))

# EPOC
clauses.append(expr("Presenta(x, Tos) & Presenta(x, DificultadParaRespirar) & Presenta(x, DolorDePecho) & Presenta(x, Fatiga) & Presenta(x, InfeccionesRespiratoriasFrecuentes) ==> Enfermo(x, EPOC)"))

# Cancer de Pulmon
clauses.append(expr("Presenta(x, TosPersistente) & Presenta(x, TosConSangre) & Presenta(x, DificultadParaRespirar) & Presenta(x, Ronquera) & Presenta(x, DolorDePecho) & Presenta(x, PerdidaDePeso) & Presenta(x, Cansancio) & Presenta(x, DolorEnHuesos)==> Enfermo(x, CancerDePulmon)"))

# Enfisema Pulmonar
clauses.append(expr("Presenta(x, HinchazonPies) & Presenta(x, HinchazonTobillos) & Presenta(x, HinchazonPiernas) ==> Enfermo(x, EnfisemaPulmonar)"))

### Tratamientos

# Resfriado
clauses.append(expr("Enfermo(x, Resfriado) ==> Requiere(x, Liquidos)"))
clauses.append(expr("Enfermo(x, Resfriado) ==> Requiere(x, Reposo)"))
clauses.append(expr("Enfermo(x, Resfriado) ==> Requiere(x, Ibuprofeno)"))
clauses.append(expr("Enfermo(x, Resfriado) ==> Requiere(x, Paracetamol)"))

# Gripe
clauses.append(expr("Enfermo(x, Gripe) ==> Requiere(x, Reposo)"))
clauses.append(expr("Enfermo(x, Gripe) ==> Requiere(x, Liquidos)"))
clauses.append(expr("Enfermo(x, Gripe) ==> Requiere(x, Paracetamol)"))
clauses.append(expr("Enfermo(x, Gripe) ==> Requiere(x, Ibuprofeno)"))
clauses.append(expr("Enfermo(x, Gripe) ==> Requiere(x, Antivirales)"))

# Neumonia
clauses.append(expr("Enfermo(x, Neumonia) ==> Requiere(x, Antibioticos)"))
clauses.append(expr("Enfermo(x, Neumonia) ==> Requiere(x, Hospitalizacion)"))
clauses.append(expr("Enfermo(x, Neumonia) ==> Requiere(x, Oxigeno)"))

# Bronquitis
clauses.append(expr("Enfermo(x, Bronquitis) ==> Requiere(x, Reposo)"))
clauses.append(expr("Enfermo(x, Bronquitis) ==> Requiere(x, Liquidos)"))
clauses.append(expr("Enfermo(x, Bronquitis) ==> Requiere(x, Paracetamol)"))
clauses.append(expr("Enfermo(x, Bronquitis) ==> Requiere(x, Ibuprofeno)"))
clauses.append(expr("Enfermo(x, Bronquitis) ==> Requiere(x, Inhaladores)"))

# Asma
clauses.append(expr("Enfermo(x, Asma) ==> Requiere(x, MedicamentosInhaladosControl)"))
clauses.append(expr("Enfermo(x, Asma) ==> Requiere(x, MedicamentosInhaladosRescate)"))

# Fibrosis Pulmonar
clauses.append(expr("Enfermo(x, FibrosisPulmonar) ==> Requiere(x, MedicamentosRalentizarProgresion)"))
clauses.append(expr("Enfermo(x, FibrosisPulmonar) ==> Requiere(x, Oxigenoterapia)"))
clauses.append(expr("Enfermo(x, FibrosisPulmonar) ==> Requiere(x, TransplantePulmon)"))

# Hipertension Pulmonar
clauses.append(expr("Enfermo(x, HipertensionPulmonar) ==> Requiere(x, MedicamentosDilatadores)"))
clauses.append(expr("Enfermo(x, HipertensionPulmonar) ==> Requiere(x, Cirugia)"))
clauses.append(expr("Enfermo(x, HipertensionPulmonar) ==> Requiere(x, TransplantePulmon)"))

# EPOC
clauses.append(expr("Enfermo(x, EPOC) ==> Requiere(x, MedicamentosViasRespiratorias)"))
clauses.append(expr("Enfermo(x, EPOC) ==> Requiere(x, Oxigenoterapia)"))
clauses.append(expr("Enfermo(x, EPOC) ==> Requiere(x, Cirugia)"))

# Cancer de Pulmon
clauses.append(expr("Enfermo(x, CancerDePulmon) ==> Requiere(x, Cirugia)"))
clauses.append(expr("Enfermo(x, CancerDePulmon) ==> Requiere(x, Quimioterapia)"))
clauses.append(expr("Enfermo(x, CancerDePulmon) ==> Requiere(x, Radiación)"))
clauses.append(expr("Enfermo(x, CancerDePulmon) ==> Requiere(x, Terapia)"))

# Enfisema Pulmonar
clauses.append(expr("Enfermo(x, EnfisemaPulmonar) ==> Requiere(x, DejarFumar)"))
clauses.append(expr("Enfermo(x, EnfisemaPulmonar) ==> Requiere(x, Medicamentos)"))
clauses.append(expr("Enfermo(x, EnfisemaPulmonar) ==> Requiere(x, Oxigenoterapia)"))
clauses.append(expr("Enfermo(x, EnfisemaPulmonar) ==> Requiere(x, Cirugia)"))

### Recomendaciones

# Resfriado
clauses.append(expr("Enfermo(x, Resfriado) ==> Recomendar(x, LavarManos)"))
clauses.append(expr("Enfermo(x, Resfriado) ==> Recomendar(x, EvitarContactoEnfermos)"))
clauses.append(expr("Enfermo(x, Resfriado) ==> Recomendar(x, CubrirBocaNariz)"))

# Gripe
clauses.append(expr("Enfermo(x, Gripe) ==> Recomendar(x, LavarManos)"))
clauses.append(expr("Enfermo(x, Gripe) ==> Recomendar(x, EvitarContactoEnfermos)"))
clauses.append(expr("Enfermo(x, Gripe) ==> Recomendar(x, CubrirBocaNariz)"))
clauses.append(expr("Enfermo(x, Gripe) ==> Recomendar(x, VacunarseGripe)"))

# Neumonia
clauses.append(expr("Enfermo(x, Neumonia) ==> Recomendar(x, LavarManos)"))
clauses.append(expr("Enfermo(x, Neumonia) ==> Recomendar(x, EvitarContactoEnfermos)"))
clauses.append(expr("Enfermo(x, Neumonia) ==> Recomendar(x, CubrirBocaNariz)"))
clauses.append(expr("Enfermo(x, Neumonia) ==> Recomendar(x, VacunarseGripe)"))
clauses.append(expr("Enfermo(x, Neumonia) ==> Recomendar(x, VacunarseNeumonia)"))

# Bronquitis
clauses.append(expr("Enfermo(x, Bronquitis) ==> Recomendar(x, EvitarIrritantesPulmonares)"))
clauses.append(expr("Enfermo(x, Bronquitis) ==> Recomendar(x, LavarManos)"))

# Asma
clauses.append(expr("Enfermo(x, Asma) ==> Recomendar(x, ControlarAsmaMedico)"))
clauses.append(expr("Enfermo(x, Asma) ==> Recomendar(x, SeguirPlanTratamientoAsma)"))
clauses.append(expr("Enfermo(x, Asma) ==> Recomendar(x, IdentificarEvitarDesencadenantesAsma)"))

# Fibrosis Pulmonar
clauses.append(expr("Enfermo(x, FibrosisPulmonar) ==> Recomendar(x, DejarFumar)"))
clauses.append(expr("Enfermo(x, FibrosisPulmonar) ==> Recomendar(x, EvitarIrritantesPulmonares)"))
clauses.append(expr("Enfermo(x, FibrosisPulmonar) ==> Recomendar(x, HacerEjercicioRegularmente)"))
clauses.append(expr("Enfermo(x, FibrosisPulmonar) ==> Recomendar(x, VacunarseGripeNeumonía)"))

# Hipertension Pulmonar
clauses.append(expr("Enfermo(x, HipertensionPulmonar) ==> Recomendar(x, MantenerPesoSaludable)"))
clauses.append(expr("Enfermo(x, HipertensionPulmonar) ==> Recomendar(x, HacerEjercicioRegularmente)"))
clauses.append(expr("Enfermo(x, HipertensionPulmonar) ==> Recomendar(x, EvitarIrritantesPulmonares)"))
clauses.append(expr("Enfermo(x, HipertensionPulmonar) ==> Recomendar(x, ControlarAfeccionesMedicas)"))

# EPOC
clauses.append(expr("Enfermo(x, EPOC) ==> Recomendar(x, DejarFumar)"))
clauses.append(expr("Enfermo(x, EPOC) ==> Recomendar(x, EvitarIrritantesPulmonares)"))
clauses.append(expr("Enfermo(x, EPOC) ==> Recomendar(x, VacunarseGripeNeumonia)"))
clauses.append(expr("Enfermo(x, EPOC) ==> Recomendar(x, HacerEjercicioRegularmente)"))
clauses.append(expr("Enfermo(x, EPOC) ==> Recomendar(x, DietaSaludable)"))

# Cancer de Pulmon
clauses.append(expr("Enfermo(x, CancerDePulmon) ==> Recomendar(x, NoFumar)"))

# Enfisema Pulmonar
clauses.append(expr("Enfermo(x, EnfisemaPulmonar) ==> Recomendar(x, DejarFumar)"))
clauses.append(expr("Enfermo(x, EnfisemaPulmonar) ==> Recomendar(x, Medicamentos)"))
clauses.append(expr("Enfermo(x, EnfisemaPulmonar) ==> Recomendar(x, Oxigenoterapia)"))
clauses.append(expr("Enfermo(x, EnfisemaPulmonar) ==> Recomendar(x, Cirugía)"))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#----------------------------------------------------------------

# Base de conocimientos
kb = FolKB(clauses)

# Función que extrae las constantes de una clausula de la kb
def SintomasConst(cls):
    const = []
    isplit = str(kb.clauses[cls]).split('Presenta(x, ')
    for i in range(1, len(isplit)):
        const.append(isplit[i].split(')')[0])
    return const

# Pregunta al usuario por su nombre
name =  input('¿Cuál es tu nombre? \n')


# Pregunta al usuario la presencia de una lista de síntomas. **El orden de las preguntas es dinámico y se basa en las respuestas del usuario**.
sintomas_agente = [ListaSintomas[0]]
noOmitir = True

for i in range(0, len(ListaSintomas)):

    sintoma = sintomas_agente[i]
    if pregunta(sintoma, name) == 1:
        for j in range(0, 11):
            if sintoma in SintomasConst(j):
                sintomas_agente = sintomas_agente + SintomasConst(j)
                sintomas_agente = list(dict.fromkeys(sintomas_agente))
    
    if i == len(sintomas_agente)-1:
        for k in ListaSintomas:
            if k not in sintomas_agente:
                sintomas_agente.append(k)
                break
    if noOmitir:
        hay_enfermedad = False
        if not hay_enfermedad:
            hay_enfermedad = len(list(fol_fc_ask(kb, expr('Enfermo({}, x)'.format(name))))) >= 1

        if hay_enfermedad:
            seguir = input('Se ha diagnosticado una enfermedad, ¿cuentas con más síntomas?\n')
            if seguir != 's':
                break
            else:
                noOmitir = False


# Lista de síntomas del paciente
sintomas = list(fol_fc_ask(kb, expr('Presenta({}, x)'.format(name))))

if len(sintomas) > 0:
    print('\n\n\n-----Síntomas del paciente {}:-----\n'.format(name))
    for sintoma in sintomas:
        print(sintoma[x])
else:
    print('\n\n\nPaciente {} no presenta síntomas\n'.format(name))


# Enfermedad del paciente
enfermedades = list(fol_fc_ask(kb, expr('Enfermo({}, x)'.format(name))))

if len(enfermedades) > 0:
    print('\n\n\n-----Paciente {} padece de:-----\n'.format(name))
    for enfermedad in enfermedades:
        print(enfermedad[x])
else:
    print('\n\n\nPaciente {} no presenta ninguna enfermedad\n'.format(name))


# Requerimientos del paciente
requerimientos = list(fol_fc_ask(kb, expr('Requiere({}, x)'.format(name))))

if len(requerimientos) > 0:
    print('\n\n\n-----Paciente {} requiere de:-----\n'.format(name))
    for requerimiento in requerimientos:
        print(requerimiento[x])
else:
    print('\n\n\nPaciente {} no requiere de nada\n'.format(name))


# Recomendaciones al paciente
recomendaciones = list(fol_fc_ask(kb, expr('Recomendar({}, x)'.format(name))))

if len(recomendaciones) > 0:
    print('\n\n\n-----A {} se le recomienda:-----\n'.format(name))
    for recomendacion in recomendaciones:
        print(recomendacion[x])
else:
    print('\n\n\nA {} no se le recomienda nada\n'.format(name))