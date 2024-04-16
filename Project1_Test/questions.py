# questions databese. Format = list of dictionaries. Dictionary keys: subject, qeustion, answer

def question(n,k):
    questions_list=[]

#math
    questions_list.append({'subject': 'Math', 'question': 'Square root of 169: ', 'answer': 13})
    questions_list.append({'subject': 'Math', 'question': '2x + 18 = 84. x = : ', 'answer': 33})
    questions_list.append({'subject': 'Math', 'question': 'Internal angle of equilateral triangle is (degrees) : ', 'answer': 60})
    questions_list.append({'subject': 'Math', 'question': '5! = ', 'answer': 120})
    questions_list.append({'subject': 'Math', 'question': 'How many vertice does tetrahedron have: ', 'answer': 4})
    questions_list.append({'subject': 'Math', 'question': 'How many points do you need to determine Euclidean plane: ', 'answer': 3})
    questions_list.append({'subject': 'Math', 'question': 'Sin 90 u"\N{DEGREE SIGN}: ', 'answer': 1})
    questions_list.append({'subject': 'Math', 'question': 'What if the biggest prime number under 1000: ', 'answer': 997})
    questions_list.append({'subject': 'Math', 'question': 'What is the root of x*x - 8x + 16 = 0: ', 'answer': 4})
    questions_list.append({'subject': 'Math', 'question': 'What is radius of  curcle with circumference of 314.5 (round it): ', 'answer': 50})

# physics
    questions_list.append({'subject': 'Physics', 'question': 'Boiling temperature of water (degC): ', 'answer': 100})
    questions_list.append({'subject': 'Physics', 'question': 'How many known planets does Solar system contain: ', 'answer': 8})
    questions_list.append({'subject': 'Physics', 'question': 'An athlete covers 3 rounds on a circular track of radius 50 m. What is the displacement covered by him?: ', 'answer': 0})
    questions_list.append({'subject': 'Physics', 'question': 'How many fundamental forces are there in the universe: ', 'answer': 4})
    questions_list.append({'subject': 'Physics', 'question': 'What is the voltage of a battery that powers a light with 0.5 A and has a resistance of 4 ohms?: ', 'answer': 2})
    questions_list.append({'subject': 'Physics', 'question': 'If the two 10 Ω resistors are connected in parallel, what is their equivalent resistance: ', 'answer': 5})
    questions_list.append({'subject': 'Physics', 'question': '20000J  of heat is used to increase the temperature of 500g of an object from 30u"\N{DEGREE SIGN}C to 70u"\N{DEGREE SIGN}C. What is the specific heat capacity of the object(J/kgu"\N{DEGREE SIGN}C): ', 'answer': 1000})
    questions_list.append({'subject': 'Physics', 'question': 'A car starts off at 5m/s and accelerates at 4m/s2 for 10s. What is its final velocity(m/s)?: ', 'answer': 45})
    questions_list.append({'subject': 'Physics', 'question': 'Calculate the density of mercury if 500 cm3 has a mass of 6.0 kg (g/cm3): ', 'answer': 12})
    questions_list.append({'subject': 'Physics', 'question': 'A man stands two meters away from a plane mirror. How far is it from the man to his image (m): ', 'answer': 4})

#chemistry
    questions_list.append({'subject': 'Chemistry', 'question': 'How many atoms of hydrogen are on the left side of the arrow? 2H2O ---> 2H2 + O2: ', 'answer': 4})
    questions_list.append({'subject': 'Chemistry', 'question': 'How many hydrogen atoms are on the product side? N2 + 3H2 ----> 2NH3: ', 'answer': 6})
    questions_list.append({'subject': 'Chemistry', 'question': 'How many electrons can a hydrogen atom bond with to achieve a stable outer shell: ', 'answer': 1})
    questions_list.append({'subject': 'Chemistry', 'question': 'What is the atomic number of carbon: ', 'answer': 6})
    questions_list.append({'subject': 'Chemistry', 'question': 'What is the pH value of a neutral solution: ', 'answer': 7})
    questions_list.append({'subject': 'Chemistry', 'question': 'There are ___ naturally occurring elements: ', 'answer': 98})
    questions_list.append({'subject': 'Chemistry', 'question': 'How many noble gases are ib the Peiodic Table?: ', 'answer': 18})
    questions_list.append({'subject': 'Chemistry', 'question': 'What is the percent by volume of a solution made by dissolving 20 ml of ethyl alcohol into 180 ml of water: ', 'answer': 10})
    questions_list.append({'subject': 'Chemistry', 'question': 'How many electrons are there in Helium: ', 'answer': 2})
    questions_list.append({'subject': 'Chemistry', 'question': 'How many atoms are in one particle of FeO: ', 'answer': 2})

#biology
    questions_list.append({'subject': 'Biology', 'question': 'What is the number of chromosomes in a normal human karyotype?: ', 'answer': 46})
    questions_list.append({'subject': 'Biology', 'question': 'How many limbs does spider have? : ', 'answer': 8})
    questions_list.append({'subject': 'Biology', 'question': 'How many lobes does a human brain have?: ', 'answer': 4})
    questions_list.append({'subject': 'Biology', 'question': 'How many chambers is the heart divided into?: ', 'answer': 4})
    questions_list.append({'subject': 'Biology', 'question': 'A newborn has 275 to 300 bones. How much bones do most adults have?: ', 'answer': 206})
    questions_list.append({'subject': 'Biology', 'question': 'How many main kingdoms of living things are generaly known?: ', 'answer': 5})
    questions_list.append({'subject': 'Biology', 'question': 'How many chains create a DNA?: ', 'answer': 2})
    questions_list.append({'subject': 'Biology', 'question': 'How many major types of biomes do exist?: ', 'answer': 5})
    questions_list.append({'subject': 'Biology', 'question': 'Bacterias are one of the smallest orgainsm. How many cells they contain?: ', 'answer': 1})
    questions_list.append({'subject': 'Biology', 'question': 'Glucose contains ___ carbons: ', 'answer': 6})

#geography
    questions_list.append({'subject': 'Geography', 'question': 'About _____  percent of the Earth\'s surface is water-covered, and the oceans hold about 96.5 percent of all Earth\'s water.: ', 'answer': 70})
    questions_list.append({'subject': 'Geography', 'question': 'The place China takes in the list of the largest countries is: ', 'answer': 3})
    questions_list.append({'subject': 'Geography', 'question': 'What is the time difference between longitudes (in minutes)?: ', 'answer': 4})
    questions_list.append({'subject': 'Geography', 'question': 'How many countries are bordering Bulgaria?: ', 'answer': 5})
    questions_list.append({'subject': 'Geography', 'question': 'How many stars are on the Australian flag?: ', 'answer': 6})
    questions_list.append({'subject': 'Geography', 'question': 'How many countries are there in Australia?: ', 'answer': 1})
    questions_list.append({'subject': 'Geography', 'question': 'How many countries are in the European Union?: ', 'answer': 27})
    questions_list.append({'subject': 'Geography', 'question': 'How many time zones are in the world?: ', 'answer': 24})
    questions_list.append({'subject': 'Geography', 'question': 'How many geological continents are?: ', 'answer': 6})
    questions_list.append({'subject': 'Geography', 'question': 'How many primary time zones are within the Europe? : ', 'answer': 7})


    return questions_list[n][k]



