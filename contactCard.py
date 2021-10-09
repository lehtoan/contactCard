from datetime import datetime, date, time, timezone

class Contact:
    count = 0
    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

        self.favorite = 0
        
        self.phoneNumber = ""
        self.profilePicture = "defaultProfilePicture.jpg"

        self.birthday = ""
        self.zodiacSign = ""
        self.age = ""

        self.favoriteColor = ""
        self.favoriteFood = ""
        self.favoriteDisneyPrincess = ""
        self.favoriteMarvelSuperhero = ""
        self.favoriteStore = ""
        self.favoriteAnimal = ""
        self.favoriteMovie = ""
        self.notes = ""
        Contact.count += 1

    def __repr__(self):
        return id(self)
        
    def updateBirthday(self, date):
        self.birthday = date

        today = datetime.today()
        self.age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        self.zodiacSign = findHorescope(self.birthday)

    def updatePhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def updateProfilePicture(self, imageLink):
        self.profilePicture = imageLink

    def updateFavoriteFood(self, food):
        self.favoriteFood = food

    def updateFavoriteColor(self, color):
        self.favoriteColor = color

    def updateFavoriteStore(self, store):
        self.favoriteStore = store

    def updateFavoriteAnimal(self, animal):
        self.favoriteAnimal = animal

    def updateFavoriteMovie(self, movie):
        self.favoriteMovie = movie
        
    def updateFavoriteDisneyPrincess(self, princess):
        self.favoriteDisneyPrincess = princess

    def updateFavoriteMarvelSuperhero(self, hero):
        self.favoriteMarvelSuperhero = hero

    def updateNotes(self, notes):
        self.notes = notes
        
    def showContact(self):
        return ("{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}\n"
                "{:20}{}").format("First Name:", self.firstName,
                                                        "Last Name:", self.lastName,
                                                        "Phone Number:", self.phoneNumber,
                                                        "Birthday:", self.birthday,
                                                        "Age:", self.age,
                                                        "Zodiac Sign:", self.zodiacSign,
                                                        "Favorite Color:", self.favoriteColor,
                                                        "Favorite Food:", self.favoriteFood,
                                                        "Favorite Store:", self.favoriteStore,
                                                        "Favorite Animal:", self.favoriteAnimal,
                                                        "Favorite Movie:", self.favoriteMovie,                                   
                                                        "Favorite Princess:", self.favoriteDisneyPrincess,
                                                        "Favorite Superhero:", self.favoriteMarvelSuperhero,
                                                        "Notes:", self.notes)

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getPhoneNumber(self):
        return self.phoneNumber
    
    def getBirthday(self):
        return(self.birthday)

    def getAge(self):
        return(self.age)

    def getZodiacSign(self):
        return(self.zodiacSign)

    def getFavoriteColor(self):
        return self.favoriteColor

    def getFavoriteFood(self):
        return self.favoriteFood

    def getFavoriteStore(self):
        return self.favoriteStore
    
    def getFavoriteAnimal(self):
        return self.favoriteAnimal

    def getFavoriteMovie(self):
        return self.favoriteMovie
    
    def getFavoriteDisneyPrincess(self):
        return self.favoriteDisneyPrincess

    def getFavoriteMarvelSuperhero(self):
        return self.favoriteMarvelSuperhero

    def getNotes(self):
        return self.notes
    
    def getProfilePicture(self):
        return(self.profilePicture)

    def __del__(self):
        Contact.count -= 1

    def __str__(self):
        return self.firstName + " " + self.lastName
    
def findHorescope(birthDate):
    if birthDate.month == 1:
        if birthDate.day <= 19:
            return("Capricorn")
        else:
            return("Aquarius")
    elif birthDate.month == 2:
        if birthDate.day <= 18:
            return("Aquarius")
        else:
            return("Pisces")
    elif birthDate.month == 3:
        if birthDate.day <= 20:
            return("Pisces")
        else:
            return("Aries")
    elif birthDate.month == 4:
        if birthDate.day <= 19:
            return("Aries")
        else:
            return("Taurus")
    elif birthDate.month == 5:
        if birthDate.day <= 20:
            return("Taurus")
        else:
            return("Gemini")
    elif birthDate.month == 6:
        if birthDate.day <= 20:
            return("Gemini")
        else:
            return("Cancer")
    elif birthDate.month == 7:
        if birthDate.day <= 22:
            return("Cancer")
        else:
            return("Leo")
    elif birthDate.month == 8:
        if birthDate.day <= 22:
            return("Leo")
        else:
            return("Virgo")
    elif birthDate.month == 9:
        if birthDate.day <= 22:
            return("Virgo")
        else:
            return("Libra")
    elif birthDate.month == 10:
        if birthDate.day <= 22:
            return("Libra")
        else:
            return("Scorpio")
    elif birthDate.month == 11:
        if birthDate.day <= 21:
            return("Scorpio")
        else:
            return("Sagittarius")
    elif birthDate.month == 12:
        if birthDate.day <= 21:
            return("Sagittarius")
        else:
            return("Capricorn") 

