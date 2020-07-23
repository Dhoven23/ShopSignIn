import datetime
import mongoengine
import cv2


# ----------------------------------------------------------------------------------------------------
# This is the individual Student class that stores all non-time-sensitive information about a student
# It is meant to be an easy document to interact with, as it is mostly static, except for the boolean
# that indicates to the login service that a student is in the shop
# ----------------------------------------------------------------------------------------------------


class Student(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    keys_trained = mongoengine.ListField(required=False)
    studentID = mongoengine.StringField(required=True)
    Is_signedIn = mongoengine.BooleanField(default=False)
    profile = mongoengine.ImageField(size=(800,600,True), thumbnail_size=(200,150,True))
    capstoneID = mongoengine.StringField(required=False)

    # switches the signed in status of the student when called. Only call when you really mean to
    def event(self):
        self.Is_signedIn = not self.Is_signedIn
        self.save()
    def train(self, key):
        if key not in self.keys_trained:
            self.keys_trained.append(key)
            self.save()
        else:
            pass
    def add_profile_image(self):
        pass
        #self.profile = cv2.imread('3.png')
        #self.save()


    # alias to the current document collection. If you plan to edit this class, rename the 'Students' collection
    # to some temporary collection until you are ready to port over all the students in the current collection
    meta = {
        'db_alias': 'core',
        'collection': 'Students'
    }
