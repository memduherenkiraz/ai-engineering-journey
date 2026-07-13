
#------------------------------------------------------------------------------------------------------------------------------------------

# Exercise-1: Hello World
# "Hello, World!" mesajını döndüren metot yaz.

# def hello():
#     return 'Hello, World!'

#------------------------------------------------------------------------------------------------------------------------------------------

# Exercise-2: Guido's Gorgeous Lasagna

#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

# EXPECTED_BAKE_TIME = 40
# PREPARATION_TIME = 2


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
# def bake_time_remaining(elapsed_bake_time):
#     """Calculate the bake time remaining.

#     Parameters:
#         elapsed_bake_time (int): The baking time already elapsed.

#     Returns:
#         int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

#     Function that takes the actual minutes the lasagna has been in the oven as
#     an argument and returns how many minutes the lasagna still needs to bake
#     based on the `EXPECTED_BAKE_TIME`.
#     """

#     return EXPECTED_BAKE_TIME - elapsed_bake_time


# TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers, you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

# def preparation_time_in_minutes(layers):
#     """Calculate the total preparation time based on the numbers of layers int the lasagna.

#     Parameters:
#         layers (int): The number of layers in the lasagna.

#     Returns:
#         int: The total preparation time (in minutes) derived from 'PREPARATION_TIME'.

#     Function that takes the number of layers as a parameter and returns the total preparation time in minutes based on the ‘PREPARATION_TIME'.
#     """
#     return PREPARATION_TIME * layers

# TODO (student): define the 'elapsed_time_in_minutes()' function below.

# def elapsed_time_in_minutes(layers, elapsed_bake_time):
#     """Calculate the total time you spend in the kitchen making this lasagna (prep time + baking time).

#     Parameters:
#         layers (int): The number of layers in the lasagna.
#         elapsed_baked_time (int):The baking time already elapsed.

#     Returns:
#         int: The total time (in minutes) derived from 'layers' and 'elapsed_baked_time'.

#     Function that takes the number of layers and elapsed baked time as parameters and returns the total time in minutes.
#     """
#     return elapsed_bake_time + preparation_time_in_minutes(layers)
    

# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
# las_layer = 15
# elapsed_time = 20

# et = elapsed_time_in_minutes(las_layer, elapsed_time)
# print("Total Elapsed Time (min) :", et) 

#------------------------------------------------------------------------------------------------------------------------------------------

# Exercise3: Ghost Gobble Arcade Game

# İki parametre alan (Pac-Man’in güç hapı aktif mi ve Pac-Man bir hayalete dokunuyor mu) ve 
# Pac-Man’in bir hayaleti yiyip yiyemeyeceğini belirten bir Boole değeri döndüren eat_ghost() işlevini tanımlayın.
# İşlev, yalnızca Pac-Man’in güç hapı aktifse ve bir hayalete dokunuyorsa True değerini döndürmelidir.

# İki parametre alan (Pac-Man’in bir güç hapına dokunup dokunmadığı ve Pac-Man’in bir noktaya dokunup dokunmadığı) ve 
# Pac-Man puan kazandıysa bir Boole değeri döndüren score() işlevini tanımlayın. 
# Pac-Man bir güç hapına veya bir noktaya dokunuyorsa işlev True değerini döndürmelidir.

# İki parametre alan (Pac-Man’in aktif bir güç hapı olup olmadığı ve Pac-Man’in bir hayalete dokunup dokunmadığı) ve 
# Pac-Man kaybederse bir Boole değeri döndüren lose() işlevini tanımlayın. 
# Pac-Man bir hayalete dokunuyorsa ve aktif bir güç hapı yoksa, işlev True değerini döndürmelidir.

# Üç parametre alan (Pac-Man'in tüm noktaları yemiş olması, Pac-Man'in aktif bir güç hapına sahip olması ve 
# Pac-Man'in bir hayalete dokunuyor olması) ve Pac-Man'in kazanması durumunda bir Boole değeri döndüren win() işlevini tanımlayın. 
# İşlev, Pac-Man'in tüm noktaları yemiş olması ve 3. bölümde tanımlanan kurallara göre kaybetmemiş olması durumunda True değerini döndürmelidir.

# """Functions for implementing the rules of the classic arcade game Pac-Man."""


# def eat_ghost(power_pellet_active, touching_ghost):
#     """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

#     Parameters:
#         power_pellet_active (bool): Does the player have an active power pellet?
#         touching_ghost (bool): Is the player touching a ghost?

#     Returns:
#         bool: Can a ghost be eaten?

#     """

#     if power_pellet_active and touching_ghost:
#         return True
#     return False


# def score(touching_power_pellet, touching_dot):
#     """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

#     Parameters:
#         touching_power_pellet (bool): Is the player touching a power pellet?
#         touching_dot (bool): Is the player touching a dot?

#     Returns:
#         bool: Has the player scored or not?

#     """

#     if touching_power_pellet or touching_dot:
#         return True
#     return False


# def lose(power_pellet_active, touching_ghost):
#     """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

#     Parameters:
#         power_pellet_active (bool): Does the player have an active power pellet?
#         touching_ghost (bool): Is the player touching a ghost?

#     Returns:
#         bool: Has the player lost the game?
#     """

#     if not power_pellet_active and touching_ghost:
#         return True
#     return False


# def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
#     """Trigger the victory event when all dots have been eaten.

#     Parameters:
#         has_eaten_all_dots (bool): Has the player "eaten" all the dots?
#         power_pellet_active (bool): Does the player have an active power pellet?
#         touching_ghost (bool): Is the player touching a ghost?

#     Returns:
#         bool: Has the player won the game?
#     """

#     if has_eaten_all_dots:
#         if not (not power_pellet_active and touching_ghost):
#             return True
#     return False

# if eat_ghost(False, True):
#     print("Canavarı Yedin")
# else:
#     print("Canavarı Yiyemedin")

# if score(False, False):
#     print("Score Kazandın")
# else:
#     print("Score Kazanamadın")

# if lose(False, True):
#     print("Kaybettin")

# if win(True, False, True):
#     print("Kazandın")
