# Project using string concatination method (f'string')

college = input('College: ')
first_name = input('First Name: ')
last_name = input('Last Name: ')
father_name = input("Father's Name: ")
joined_date = input('Joined Date: ')
finished_date = input('Until: ')
programme = input('Programme: ')
graduted_year = input('Graduated Year: ')
birth_day = input('Birth Date: ')
registration_number = input('Registration Number: ')
cgpa = input('CGPA: ')


certificate = f"This is to certify that Mr./Ms {first_name} {last_name} \
                son/daughter of {father_name}  was  \
                a bonafide student of this college from {joined_date} to {finished_date} \
                He/She has successfully passed the {programme} of Pokhara University in \
                year {graduted_year} and has secured a CGPA of {cgpa} in four point scale.\
            \
                According to the college records, his/her date of birth is {birth_day} and University Reg.no is \
                {registration_number}.To the best of my knowledge he/she bears Best moral character"


print(certificate)