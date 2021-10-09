import contactCard
import sys
import os.path
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

contactListDisplay = {}
contactList = []

class entryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder = "...", color = 'grey', **kwargs):
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.placeholderColor = color
        self.defaultColor = 'black'

        self.bind("<FocusIn>", self.focusIn)
        self.bind("<FocusOut>", self.focusOut)

        self.setPlaceholder()

    def setPlaceholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholderColor

    def focusIn(self, *args):
        if self['fg'] == self.placeholderColor:
            self.delete(0, END)
            self['fg'] = self.defaultColor

    def focusOut(self, *args):
        if not self.get():
            self.setPlaceholder()

def updateContactListDisplay(newContact):
    contactList.append(newContact)
    contactListDisplay[newContact] = []
    contactListDisplay[newContact].append(Label(homeTab, text = newContact, height = 1, width = 23))
    contactListDisplay[newContact][0].grid(row = len(contactListDisplay) + 1, column = 1)
    contactListDisplay[newContact].append(Button(homeTab, text = "view", command = lambda: clickView(newContact)))
    contactListDisplay[newContact][1].grid(row = len(contactListDisplay) + 1, column = 2)    

def clickSave():
    firstName = firstNameEntry.get()
    lastName = lastNameEntry.get()
    phoneNumber = phoneNumberEntry.get()

    name = firstName + "" + lastName

    firstNameEntry.delete(0, END)
    lastNameEntry.delete(0, END)
    phoneNumberEntry.delete(0, END)

    if lastName == "" or firstName == "":
        messagebox.showerror("Contact Card", "cannot leave first name or last name blank")
    elif name in contactList:
        messagebox.showerror("Contact Card", "unable to create new contact, contact already exists")
    else:
        contactList.append(name)
        newContact = contactCard.Contact(firstName, lastName)
        newContact.updatePhoneNumber(phoneNumber)
        updateContactListDisplay(newContact)
        messagebox.showinfo("Contact Card", "contact created")
        
def clickView(entry):
    newWindow = Toplevel(root)
    newWindow.geometry("250x500")
    newWindow.resizable(False, False)
    newWindow.title(entry)

    img = Image.open(entry.getProfilePicture())
    img = img.resize((250,250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    panel = Label(newWindow, image = img)
    panel.pack(side = "top", fill = "both")

    contactInfoContent = Text(newWindow, height = 16)
    contactInfoContent.insert(END, entry.showContact())
    contactInfoContent.config(state=DISABLED)
    contactInfoContent.pack()

    editButton = ttk.Button(newWindow, text = "edit", command = lambda: [newWindow.destroy(),edit(entry)])
    editButton.pack()

    newWindow.mainloop()

def edit(entry):
    editWindow = Toplevel(root)
    editWindow.geometry("250x500")
    editWindow.resizable(False, False)
    editWindow.title(str(entry) + " (EDIT)")

    first_name = Label(editWindow, text = "First Name").grid(row = 1, sticky = 'w')
    last_name = Label(editWindow, text = "Last Name").grid(row = 2, sticky = 'w')
    phone_number = Label(editWindow, text = "Phone Number").grid(row = 3, sticky = 'w')
    birthday = Label(editWindow, text = "Birthday").grid(row = 4, sticky = 'w')
    favoriteColor = Label(editWindow, text = "Favorite Color").grid(row = 5, sticky = 'w')
    favoriteFood = Label(editWindow, text = "Favorite Food").grid(row = 6, sticky = 'w')
    favoriteStore = Label(editWindow, text = "Favorite Store").grid(row = 7, sticky = 'w')
    favoriteAnimal = Label(editWindow, text = "Favorite Animal").grid(row = 8, sticky = 'w')
    favoriteMovie = Label(editWindow, text = "Favorite Movie").grid(row = 9, sticky = 'w')
    favoritePrincess = Label(editWindow, text = "Favorite Princess").grid(row = 10, sticky = 'w')
    favoriteSuperhero = Label(editWindow, text = "Favorite Superhero").grid(row = 11, sticky = 'w')    
    profilePicture = Label(editWindow, text = "Profile Picture").grid(row = 12, sticky = 'w')
    notes = Label(editWindow, text = "Notes").grid(row = 13, sticky = 'w')

    firstNameEntry = Entry(editWindow, width = 12)
    firstNameEntry.insert(END, entry.getFirstName())
    firstNameEntry.grid(row = 1, column = 1, sticky = 'w')
    lastNameEntry = Entry(editWindow, width = 12)
    lastNameEntry.insert(END, entry.getLastName())
    lastNameEntry.grid(row = 2, column = 1, sticky = 'w')
    phoneNumberEntry = Entry(editWindow, width = 12)
    phoneNumberEntry.insert(END, entry.getPhoneNumber())
    phoneNumberEntry.grid(row = 3, column = 1, sticky = 'w')
    birthdayEntry = Entry(editWindow, width = 12)
    birthdayEntry.insert(END, entry.getBirthday())
    birthdayEntry.grid(row = 4, column = 1, sticky = 'w')
    favoriteColorEntry = Entry(editWindow, width = 12)
    favoriteColorEntry.insert(END, entry.getFavoriteColor())
    favoriteColorEntry.grid(row = 5, column = 1, sticky = 'w')
    favoriteFoodEntry = Entry(editWindow, width = 12)
    favoriteFoodEntry.insert(END, entry.getFavoriteFood())
    favoriteFoodEntry.grid(row = 6, column = 1, sticky = 'w')
    favoriteStoreEntry = Entry(editWindow, width = 12)
    favoriteStoreEntry.insert(END, entry.getFavoriteStore())
    favoriteStoreEntry.grid(row = 7, column = 1, sticky = 'w')
    favoriteAnimalEntry = Entry(editWindow, width = 12)
    favoriteAnimalEntry.insert(END, entry.getFavoriteAnimal())
    favoriteAnimalEntry.grid(row = 8, column = 1, sticky = 'w')
    favoriteMovieEntry = Entry(editWindow, width = 12)
    favoriteMovieEntry.insert(END, entry.getFavoriteMovie())
    favoriteMovieEntry.grid(row = 9, column = 1, sticky = 'w')
    favoritePrincessEntry = Entry(editWindow, width = 12)
    favoritePrincessEntry.insert(END, entry.getFavoriteDisneyPrincess())
    favoritePrincessEntry.grid(row = 10, column = 1, sticky = 'w')
    favoriteSuperheroEntry = Entry(editWindow, width = 12)
    favoriteSuperheroEntry.insert(END, entry.getFavoriteMarvelSuperhero())
    favoriteSuperheroEntry.grid(row = 11, column = 1, sticky = 'w')
    uploadProfilePictureEntry = Entry(editWindow, width = 12)
    uploadProfilePictureEntry.insert(END, entry.getFavoriteFood())
    uploadProfilePictureEntry.grid(row = 12, column = 1, sticky = 'w')
    notesEntry = Entry(editWindow, width = 12)
    notesEntry.insert(END, entry.getNotes())
    notesEntry.grid(row = 13, column = 1, sticky = 'w')
    
    saveButton = Button(editWindow, text = "save", command = lambda: [saveEdit(birthdayEntry, favoriteFoodEntry, favoriteColorEntry,
                                                                              favoriteStoreEntry, favoriteAnimalEntry, favoriteMovieEntry,
                                                                              favoritePrincessEntry, favoriteSuperheroEntry,
                                                                              uploadProfilePictureEntry, notesEntry, entry), editWindow.destroy()])
    saveButton.grid(row = 14, column = 0, sticky = 'e')    
    deleteButton = Button(editWindow, text = "delete", command = lambda: [deleteContact(entry), editWindow.destroy()])
    deleteButton.grid(row = 14, column = 1, sticky = 'w')
        
    editWindow.grab_set()
    editWindow.mainloop()

def saveEdit(birthdayEntry, favoriteFoodEntry, favoriteColorEntry, favoriteStoreEntry, favoriteAnimalEntry, favoriteMovieEntry, favoritePrincessEntry, favoriteSuperheroEntry, uploadProfilePictureEntry, notesEntry, entry):
    if birthdayEntry.get() != "":
        try:
            contactCard.datetime.strptime(birthdayEntry.get(), '%Y-%m-%d')
            entry.updateBirthday(contactCard.datetime.strptime(birthdayEntry.get(), "%Y-%m-%d").date())
        except ValueError:
            messagebox.showerror("Contact Card", "invalid birthday entry, birthay must be in the following format: YYYY-MM-DD")    
    if uploadProfilePictureEntry.get() != "":
        if os.path.exists(uploadProfilePictureEntry.get()):
            entry.updateProfilePicture(uploadProfilePictureEntry.get())
        else:
            messagebox.showerror("Contact Card", "unable to upload picture, file does not exist")                
    entry.updateFavoriteFood(favoriteFoodEntry.get())
    entry.updateFavoriteColor(favoriteColorEntry.get())
    entry.updateFavoriteStore(favoriteStoreEntry.get())
    entry.updateFavoriteAnimal(favoriteAnimalEntry.get())
    entry.updateFavoriteMovie(favoriteMovieEntry.get())
    entry.updateFavoriteDisneyPrincess(favoritePrincessEntry.get())
    entry.updateFavoriteMarvelSuperhero(favoriteSuperheroEntry.get())
    entry.updateNotes(notesEntry.get())
    messagebox.showinfo("Contact Card", "information saved")

def deleteContact(entry):
    contactList.remove(entry)
    contactListDisplay[entry][0].destroy()
    contactListDisplay[entry][1].destroy()
    del contactListDisplay[entry]
    del entry
    messagebox.showinfo("Contact Card", "contact deleted")

if __name__ == "__main__":    
    root = Tk()
    root.geometry("350x700")
    root.title("Contact Card")

    master = ttk.Notebook(root)
    master.pack()

    homeTab = ttk.Frame(master)
    createContactTab = ttk.Frame(master)

    homeTab.pack(fill='both', expand=True)
    createContactTab.pack(fill='both', expand=True)

    master.add(homeTab, text='Home')
    master.add(createContactTab, text='Create Contact')

    first_name = Label(createContactTab, text = "First Name").grid(row = 1, sticky = 'w')
    last_name = Label(createContactTab, text = "Last Name").grid(row = 2, sticky = 'w')
    phone_number = Label(createContactTab, text = "Phone Number").grid(row = 3, sticky = 'w')

    firstNameEntry = entryWithPlaceholder(createContactTab, width = 15, placeholder = "Peter")
    firstNameEntry.grid(row = 1, column = 1)
    lastNameEntry = entryWithPlaceholder(createContactTab, width = 15, placeholder = "Anteater")
    lastNameEntry.grid(row = 2, column = 1)
    phoneNumberEntry = entryWithPlaceholder(createContactTab, width = 15, placeholder = "800-273-8255")
    phoneNumberEntry.grid(row = 3, column = 1)

    saveButton = Button(createContactTab, text = "save", command = clickSave).grid(row = 4, column = 1)

    root.mainloop()
