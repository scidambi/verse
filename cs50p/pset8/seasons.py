from datetime import date
import inflect
import sys
p = inflect.engine()

def main ():
            date_text = input("What is your birthday?")
            parsed_date = input_to_date(date_text)
            delta_date = age_days(parsed_date)
            age_in_minutes = age_minutes(delta_date)
            age_words = age_minutes_to_words(age_in_minutes)
            print(age_words)
            

def input_to_date (date_text):
        try:
            parsed_date = date.strptime(date_text,"%Y-%m-%d")
            return parsed_date
        except ValueError:
            sys.exit("Invalid input")

def age_days(parsed_date):

    #calculate number of days from today to when they were born"
    date_today = date.today()
    delta_date = date_today - parsed_date
    return delta_date.days
     
def age_minutes(delta_date):

    #convert number of days to minutes
    minutes = delta_date*(60*24)
    return minutes

def age_minutes_to_words(age_minutes):
    age_minutes_words = p.number_to_words(age_minutes, andword = "")
    return age_minutes_words

if __name__ == "__main__":
    main()


#implement a program that prompts the user for their date of birth in YYYY-MM-DD format 
# and then sings prints how old they are in minutes, rounded to the nearest integer, 
#   using English words instead of numerals, just like the song from Rent, 
#   without any and between words.