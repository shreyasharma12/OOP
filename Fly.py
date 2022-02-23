import Insect as i

def main():

    my_insect = {

        i.Insect() 
    }

mosquito = i.Insect()
housefly = i.Insect()

mosquito.flight_length()
housefly.flight_length()


print("How many miles does the mosquito fly?: ",mosquito.get_miles(),"miles")
print("How many miles does the housefly fly?: ",housefly.get_miles(),"miles")

main()