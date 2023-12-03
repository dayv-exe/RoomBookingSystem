from classes.place import Place
from classes.booking import Booking
from classes.enquiry import Enquiry
import storage

storage.init_db()
Enquiry.make()
