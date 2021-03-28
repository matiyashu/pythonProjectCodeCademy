lass Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker


#first method: estimate insurance cost
    def estimated_insurance_cost(self):
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
       # print("{}'s estimated insurance costs is {} dollars.".format(self.name, estimated_cost))
        print(self.name + "'s estimated insurance cost is " + str(estimated_cost) + " dollars.")

    def update_age(self, new_age):
        self.age = new_age
        print("{} is now {} years old.".format(self.name, str(self.age)))
        self.estimated_insurance_cost()

    def update_bmi(self, new_bmi):
        self.bmi = new_bmi
        print("{}'s BMI is now {}.".format(self.name, str(self.bmi)))
        self.estimated_insurance_cost()

    def update_no_children(self, new_num_children):
    	self.no_of_children = new_num_children
    	# print(self.name + " has " + str(self.no_of_children) + " Children")
    	if self.no_of_children == 1:
    		print(self.name + " has " + str(self.no_of_children) + " child.")
    	else:
    		print(self.name + " has " + str(self.no_of_children) + " Children")
    def patient_profile(self):
    	patient_information = {}
    	patient_information["Name"] = self.name
    	patient_information["Age"] = self.age
    	patient_information["Sex"] = self.sex
    	patient_information["BMI"] = self.bmi
    	patient_information["Number of Children"] = self.num_of_children
    	patient_information["Smoker"] = self.smoker
    	return patient_information

		    # initialize empty dictionary
		#patient_information = {}
		# set name as a key tied with the name value
		#patient_information[“name”] = self.name
		



patient1 = Patient("John Doe", 20, 1, 22.2, 0, 0)
patient1.update_age(26)
patient1.update_bmi(17.2)

patient1.update_no_children(1)

print(f"\n{patient1.patient_profile()}")

