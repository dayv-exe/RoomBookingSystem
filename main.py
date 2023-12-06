from classes.place import Place
from classes.booking import Booking
from classes.enquiry import Enquiry
from functions.sort import quick_sort
from functions.search import binary_search
import storage

storage.init_db()
Place.search_by_name()
