#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import re
from db.models import Instrument, Locker, Student
from helpers import (print_combo_by_locker_number, print_combo_by_last_name, 
                     print_student_instruments, find_by_last_name, print_students_by_grade, 
                     count_students_by_grade, add_instrument, add_student, count_instruments, 
                     assign_locker, assign_instrument, update_student_info, 
                     increase_grade_levels, delete_student_record, delete_instrument_record, 
                     delete_students_by_grade)

class Cli:
    def __init__(self):
        self.students = [student for student in session.query(Student)]
        self.lockers = [locker for locker in session.query(Locker)]
        self.instruments = [instrument for instrument in session.query(Instrument)]
        self.session = session
        self.main_menu()

    def main_menu(self):
        print(" ")
        user_name = input("Enter Your Name: ")
        while user_name:
            print(" ")
            print(f"~~ Welcome to Bando, {user_name}! ~~")
            print(" ")
            print("Please select from the following options:")
            print(" ")
            print("Press S to search the database.")
            print("Press P to print records.")
            print("Press C to create new data entries.")
            print("Press U to update database entries.")
            print("Press D to delete database entries.")
            print(" ")
            print("Press Q to quit.")
            print(" ")
            user_choice = input("What would you like to do next? ")
            if user_choice == "S":
                Cli.function1(self, user_choice)
            elif user_choice == "P":
                Cli.function2(self, user_choice)
            elif user_choice == "C":
                Cli.function3(self, user_choice)
            elif user_choice == "U":
                Cli.function4(self, user_choice)
            elif user_choice == "D":
                Cli.function5(self, user_choice)
            elif user_choice == "Q":
                break
            else:
                print("Invalid option entered. Please select from the list of options or press Q to exit.")
                
    def function1(self, user_choice):
        while user_choice == "S":
            print(" ")
            print("SEARCH QUERIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Search for locker combinations by locker number or student last name.")
            print("b: Search for instrument assignments by student last name.")
            print("c: Search for individual students by student last name.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                Cli.function1a(self, session, search_option)
            elif search_option == "b":
                Cli.function1b(self, session, search_option)
            elif search_option == "c":
                Cli.function1c(self, session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, c, or press Q to quit.")

    def function1a(self, session, search_option):
        print(" ")
        print("Search for locker combinations by locker number or student last name.")
        while search_option == "a":
            print(" ")
            combo_search = input("Enter locker number or student last name: ")
            print(" ")
            int_pattern = r'\d'
            regex = re.compile(int_pattern)
            match = regex.search(combo_search)
            if combo_search == "Q":
                break
            elif match:
                print_combo_by_locker_number(session, locker_number=combo_search)
            elif not match:
                print_combo_by_last_name(session, last_name=combo_search)
    
    def function1b(self, session, search_option):
        print(" ")
        print("Search for instrument assignments by student last name.")
        while search_option == "b":
            print(" ")
            record = input("Enter student last name: ")
            print(" ")
            if record == "Q":
                break
            else:
                print_student_instruments(session, last_name=record)

    def function1c(self, session, search_option):
        print(" ")
        print("Search for individual students by student last name.")
        while search_option == "c":
            print(" ")
            record = input("Enter student last name: ")
            print(" ")
            if record == "Q":
                break
            else:
                find_by_last_name(session, last_name=record)
    
    def function2(self, user_choice):
        while user_choice == "P":
            print(" ")
            print("PRINT QUERIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Print a list of students by grade level including a final count of students.")
            print("b: Count the number of instruments in inventory.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                Cli.function2a(self, session, search_option)
            elif search_option == "b":
                Cli.function2b(self, session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, or press Q to quit.")

    def function2a(self, session, search_option):
        print(" ")
        print("Print a list of students by grade level including a final count of students.")
        print(" ")
        print("Press Q to exit to main menu.")
        while search_option == "a":
            print(" ")
            grade = input("Enter grade level: ")
            if grade == "9" or grade == "10" or grade == "11" or grade == "12":
                print_students_by_grade(session, grade=grade)
                print(" ")
                count_students_by_grade(session, grade=grade)
            elif grade == "Q":
                break
            else:
                print(f"You entered: {grade}, which is invalid. Please enter 9, 10, 11, or 12 to print students by grade level.")

    def function2b(self, session, search_option):
        print(" ")
        print("Count the number of instruments in inventory.")
        print(" ")
        print("Press Q to exit to main menu.")
        while search_option == "b":
            print(" ")
            instrument = input("Enter instrument type: ")
            instrument_types = ["Flute", "Oboe", "Clarinet", "Alto Saxophone", "Tenor Saxophone", "Bari Saxophone", "French Horn", "Bassoon", "Bass Clarinet", "Trumpet", "Trombone", "Euphonium", "Tuba"]
            if instrument in instrument_types:
                print(" ")
                count_instruments(session, instrument=instrument)
            elif instrument == "Q":
                break
            else:
                print(f"You entered: {instrument}, which is invalid. Please select from the following list of instruments: {instrument_types}")

    def function3(self, user_choice):
        while user_choice == "C":
            print(" ")
            print("CREATE NEW DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Add new student to database.")
            print("b: Add new instrument to database.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                Cli.function3a(self, session, search_option)
            elif search_option == "b":
                Cli.function3b(self, session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, or press Q to quit.")

    def function3a(self, session, search_option):
        print(" ")
        print("Add new student to database.")
        while search_option == "a":
            print(" ")
            first_name = input("Enter student first name: ")
            if first_name == "Q":
                break
            else:
                last_name = input("Enter student last name: ")
                grade_level = input("Enter student grade level: ")
                print(" ")
                print(f"First Name: {first_name} | Last Name: {last_name} | Grade Level: {grade_level}")
                print(" ")
                confirm = input("Confirm add above student to database? n/Y: ")
                if confirm == "n":
                    print(" ")
                    print("Student NOT added to database.")
                elif confirm == "Y":
                    add_student(session, Student(first_name=first_name, last_name=last_name, grade_level=grade_level))
                    print(" ")
                    print("New student successfully added to database!")
                elif confirm == "Q":
                    break
                else:
                    print (" ")
                    print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")

    def function3b(self, session, search_option):
        print(" ")
        print("Add new instrument to database.")
        while search_option == "b":
            print(" ")
            type = input("Enter instrument type: ")
            if type == "Q":
                break
            else:
                print(" ")
                print(f"Type: {type}")
                print(" ")
                confirm = input("Confirm add above instrument to database? n/Y: ")
                if confirm == "n":
                    print(" ")
                    print("Instrument NOT added to database.")
                elif confirm == "Y":
                    add_instrument(session, Instrument(type=type))
                    print(" ")
                    print("New instrument successfully added to database!")
                elif confirm == "Q":
                    break
                else:
                    print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")
    
    def function4(self, user_choice):
        while user_choice == "U":
            print(" ")
            print("UPDATE DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Assign or reassign locker to student.")
            print("b: Assign or reassign instrument to student.")
            print("c: Update student information.")
            print("d: Increase student grade levels.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                Cli.function4a(self, session, search_option)
            elif search_option == "b":
                Cli.function4b(self, session, search_option)
            elif search_option == "c":
                Cli.function4c(self, session, search_option)
            elif search_option == "d":
                Cli.function4d(self, session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, c, or press Q to quit.")

    def function4a(self, session, search_option):
        print(" ")
        print("Assign or reassign locker to student.")
        while search_option == "a":
            print(" ")
            last_name = input("Enter student last name: ")
            if last_name == "Q":
                break
            else:
                assign_locker(session, last_name)
    
    def function4b(self, session, search_option):
        print(" ")
        print("Assign or reassign instrument to student.")
        while search_option == "b":
            print(" ")
            last_name = input("Enter student last name: ")
            if last_name == "Q":
                break
            else:
                assign_instrument(session, last_name)

    def function4c(self, session, search_option):
        print(" ")
        print("Update student information.")
        while search_option == "c":
            print(" ")
            last_name = input("Enter student last name: ")
            if last_name == "Q":
                break
            else:
                update_student_info(session, last_name)
    
    def function4d(self, session, search_option):
        print(" ")
        print("Increase all student grade levels by one year.")
        while search_option == "d":
            print(" ")
            confirm = input("Confirm update ALL student grade levels to increase by one year? n/Y: ")
            if confirm == "Y":
                print(" ")
                confirm_confirm = input("WARNING: Selecting Y will update ALL student grade levels to increase by one year. Press n/Y to confirm: ")
                if confirm_confirm == "Y":
                    increase_grade_levels(session)
                    print(" ")
                    print("Successfully increased all student grade levels by one year.")
                    break
                else: 
                    print("Student records NOT updated.")
                    break
            else:
                print("Student records NOT updated.")
                break

    def function5(self, user_choice):
        while user_choice == "D":
            print(" ")
            print("DELETE DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Delete individual student from database.")
            print("b: Delete individual instrument from database.")
            print("c: Delete students by grade level.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                Cli.function5a(self, session, search_option)
            elif search_option == "b":
                Cli.function5b(self, session, search_option)
            elif search_option == "c":
                Cli.function5c(self, session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, c, or press Q to quit.")

    def function5a(self, session, search_option):
        print(" ")
        print("Delete individual student from database.")
        while search_option == "a":
            print(" ")
            last_name = input("Enter student last name: ")
            delete_student_record(session, last_name)

    def function5b(self, session, search_option):
        print(" ")
        print("Delete individual instrument from database.")
        while search_option == "b":
            print(" ")
            instrument_id = input("Enter instrument ID: ")
            delete_instrument_record(session, instrument_id)

    def function5c(self, session, search_option):
        print(" ")
        print("Delete students by grade level.")
        while search_option == "c":
            print(" ")
            grade = input("Enter grade level to delete: ")
            delete_students_by_grade(session, grade)

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/band_lockers.db")
    session = Session(engine, future=True)
    Cli()
