
import CellPhoneClass as cpc

def main():
    
#######################################################################
    manu = "Apple"
    mod = "iPhone 13"
    retail = 899 

#######################################################################
    phone = cpc.CellPhone(manu,mod,retail)

    print("This is the car manufacturer:",phone.get_manufact())
    print("This is the car model:",phone.get_model())
    print("This is the car retail price:",phone.get_retail_price())
    print("Retail price: $", format(phone.get_retail_price()))

main()