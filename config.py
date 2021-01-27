FILE_NAME = 1 # Імя файла для запису даних
SHOW_INFO = True

DISPLAY_POSITION = (50,30)
DISPLAY_SIZE = (1700, 1030)
DISPLAY_COLOR = (48, 189, 221)
FPS = 240

MAX_COUNTER = 3000 # Кількість циклів в 1 еопосі
MAX_EPOCH = 1000 # Кількість епох
START_POPULATION = 100 # Кількість осіб взагалі

COUNT_OF_ALIVE_AFTER_EPOCH = 5 # Кількість виживших пісял того як закінчився минулий раунд
MUTATION_POWER = 0.01 # Ймовірність мутації гена межі [0 до 1]
CROSSOVER_POINT_NUMBER = 2 # Кількість точко кросовера, зазвичай 1, можна до 10
NUMBER_OF_PARENTS_COUPLES = START_POPULATION
WEB_LAYERS = [5,4]


#----------------- CAR ------------------
CAR_CAMERA_MOVE_SPEED = [2, 0]
CAR_FLOOR_POSITION = 100
CAR_CEILING_POSITION = 900

CAR_LAZER_OF_DEATH_POSITION = 50
CAR_LAZER_OF_DEATH_POSITION_REVERSE = 50

CAR_ENEMIES_NUMBER = 20
CAR_BALL_POSITION_DEFAULT = [800,500]
#----------------------------------------