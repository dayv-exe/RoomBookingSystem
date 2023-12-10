from functions import main_menu
import storage

storage.init_db()

while True:
    main_menu.show()
