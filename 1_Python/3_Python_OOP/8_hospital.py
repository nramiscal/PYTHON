# 070717 nramiscal@gmail.com

class Patient(object):
    def __init__(self, patient_name, allergies):
        self.id = id(self)
        self.patient_name = patient_name
        self.allergies = allergies
        self.bed_number = None
    def __str__(self):
        return "{}|{}|{}|{}".format(self.id, self.patient_name, self.allergies, self.bed_number)


class Hospital(object):
    def __init__(self, hosp_name, capacity):
        self.patients = [] # an array of patient objects
        self.hosp_name = hosp_name
        self.capacity = capacity # which should be equal to the number of beds
        self.open_beds = [] # which starts as all beds being open from #1 to capacity
        for i in range(1, capacity + 1):
            self.open_beds.append("#" + str(i))
        self.occupied_beds = [] # which starts as an empty array

    def info(self):
        print self.hosp_name + " HOSPITAL"
        print "Open beds:", self.open_beds
        print "Occupied beds:", self.occupied_beds
        print "Current patients:"
        for patient in self.patients:
            print patient
        return self



    def admit(self, patient_name, allergies):
        if len(self.patients) >= self.capacity:
            print "---------------------------------------------"
            print "HOSPITAL IS FULL. PATIENT CANNOT BE ADMITTED."
            print "---------------------------------------------"
            return self
        else:
            new_patient = Patient(patient_name, allergies)
            self.patients.append(new_patient)
            # for patient in self.patients:
            #     print patient
            new_patient.bed_number = self.open_beds[0]
            print "----------------------"
            print "***PATIENT ADMITTED***"
            print "Current patients:"
            print "----------------------"
            for patient in self.patients:
                print patient
            self.occupied_beds.append(new_patient.bed_number)
            self.open_beds.remove(self.open_beds[0])
            # print "Bed Number:" + patient.bed_number
            # print "occupied:"
            # print self.occupied_beds
            # print "open:"
            # print self.open_beds

            return self

    def discharge(self, bed_number):
        print "Patient in bed number " + bed_number + " is waiting to be discharged."
        for patient in self.patients:
            if patient.bed_number == bed_number:
                self.patients.remove(patient)
                print "------------------------"
                print "***PATIENT DISCHARGED***"
                print "------------------------"
        print "Current patients:"
        for patient in self.patients:
            print patient
        for item in self.occupied_beds:
            if item == bed_number:
                self.open_beds.append(bed_number)
                self.occupied_beds.remove(bed_number)
                print "Open beds:", self.open_beds
                print "Occupied beds:", self.occupied_beds
        return self



# p1 = Patient("Joe Shmoe", ["aspirin", "penicillin"])
# print p1
hosp1 = Hospital("SIBLEY", 5)
hosp1.info()
hosp1.admit("Joe Shmoe", ["aspirin", "penicillin"])
hosp1.admit("Tooth Fairy", ["pollen"])
hosp1.admit("Adam", ["alcohol"])
hosp1.admit("Eve", ["apples"])
hosp1.admit("Snoopy", ["cats"])
hosp1.admit("Woodstock", ["tylenol", "advil"])
hosp1.discharge("#2")
hosp1.admit("Woodstock", ["tylenol", "advil"])
hosp1.admit("Tooth Fairy", ["pollen"])
hosp1.discharge("#5")
