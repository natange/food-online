Herramientas
GitBash
VScode
Create Virtual Enviroment Python
pip freeze //lista todos los paquetes instalados
pip install virtualenv	//para instalar 
python -m venv env	//crear virtual env
source env/bin/activate	//activar el venv
deactivate 	// desactivar
Install Django and Create Project
pip install django
django-admin startproject foodOnline_main	//create project
python manage.py runserver	//run project
python manage.py migrate		//migrar
********************** 1 *******************************
---------------------  ---------------------------------

--------------- django template setup -------------------

create folder templates
create file /templates/home.html
change on file views.py :
	def home():
		return render(reques, 'home.html')
change on settings.py : 
	templates :[
		{
			'dirs':['name_of_folder=templates']	
	}	
	]
----------------- create superuser ------------------------
on terminal:
	python manage.py createsuperuser
seguir las instrucciones y probar.

*********************** 3 ***********************************

---------------------- 3.3 Homepage --------------------------
copy all code from file index.html from template foodBakery to home.html
create a folder 'static' on 
	foodOnline_main
	--> static
copy all folders assets from template 'foodBakery' dentro de la 
carpeta 'static' dentro de la carpeta code
config on the file settings.py on below line static :
	STATIC_ROOT = BASE_DIR /'static'
	STATICFILES = [
    		'foodOnline_main/static'
	]
add line at begining from file home.html : {% load static %}
configurar el archivo settigns.py para habilitar la carpeta PATH
luego en la vista que queremos renderizar html anadir {% load static %}
----------------------- 3.4 Colle -------------------------------------
setting apply command: python manage.py collectstatic
********************** 4 ********************************
----------------- 4.2 Postgres Config ------------------
Configurar el archivo settings.py en la linea de DATABASE 
	engine -> postgresql
	name -> nombre de la base de datos
	user -> postgres
	password -> contraseña del usuario postgres
	host -> localhost o nube
En caso de error django.core.exception psycopg2 	
	solution: pip install psycopg2 
Do migration : python manage.py migrate
Creación de superusuario:
	python manage.py createsuperuser
	and then full form and verify on that db rows.

----------------- 4.3 Store sensitive info -------------------------
instalar la sgte: pip install python-decouple
crear a file .env to store key secure and variables config from db.

***************************** 5 ************************************ 

---------------------- 5.1 Custom Model -----------------------------
https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-the-polls-app	
https://docs.djangoproject.com/en/4.1/topics/db/models/

python manage.py startapp accounts y quedara la estructura asi:
accounts/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

Anadir accounts en setting.py installed_apps= [ ‘accounts’] para que 
reconozca al user model custom

Declarar el model, tomar mucha atencion en declara el admin y sus clases. 
Luego en settings.py anadir debajo de DB :
	AUTH_USER_MODEL = 'accounts.User'

------------------ 5.2 Recreate Table and register user model ---------------

Para hacer migracion corremos el sgte code y lo que hara es crear un 
archivo con la migration que vamos hacer
	python manage.py makemigrations
	python manage.py migrate
Luego anadir linea en admin.py para editar y registar user.

------------------ 5.3 Make Password Nonenditable ----------------------------

Aumentar este codigo en admin.py
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','role','is_active')
    ordering = ('-date_joined',) //tupla deberia ser
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
------------------ 5.4 Design Profile ----------------

User
	foreignKey(User)
	profile_picture
	cover_photo
	address_line1
	address_line2
	country
	state
	city
	pin_code
	latitude
	longitude
	created_at
	modified_at

------------------------- 5.5 User Profile Model ------------------------------
Create class on accounts/models.py to userprofile
Then run: makemigrations; migrate
Install pip install Pillow
Pillow and its predecessor, PIL, are the original Python libraries for 
dealing with images

----------------------- 5.6 Media Files Configurations ----------------------- 

Configurar el archivo settings.py y anadir la ruta de la carpeta media, debajo 
de static url.
Luego ir urls.py para anadir static settings es decir la carpeta.

------------------------ 5.7. Django Signals To Create User Profile ----------

************************************ 6 ************************************
-User Registration
-django message and error

-------------------------- 6.1 FoodOnline flowchart --------------------------
https://app.diagrams.net/#G1y_iIGmX3dyInenlaGwjII4cOisdyJmEF
------ 6.2 
crear urls


------ 6.3. Template Inheritance Base Html -------------
Documento acerca de los template y como usar:
	https://docs.djangoproject.com/en/4.1/ref/templates/language/

Simplemente hemos dividido el header content y footer para hacer mas facil el
manejo.

---------------- 6.4 

copiar el content de register restaurant
--------------- 6.5 User Registration form implementation -----------

Created an file called forms.py on folder accounts
En ese archivo se habilita las casillas para rellenar el form.
Luego en views.py en la carpeta accounts, hacer el codigo de verificacion y
guardar lo que hace POST.

------------- 6.6. Hash The Password From Form ------------------
get password from form and data cleaned and then set user password.
Para mas informacion : https://docs.djangoproject.com/en/4.1/ref/forms/api/
Se edito en views.py para corregir el password y hay dos alternativas.

------------- 6. 

Add lines on registerUser.html to notice errors on field from form.
And form add a def clean and notice when password dont match.


------------- 6.8 django messages
Only add alert bootstrap on registerUser.html to notice that your account
was created sucessful.

------------- 6.9 messages animation

bootsatrap and css

-------------- 6.10 frontend tweaks
 algunos retoques como arreglar al dirigir a register desde home.html

-------------- 6.11 git push
nada solo push

********* 7. Vendor registration and authentication functionalities *********

------------------ 7.1. Vendor Model ---------------------

user - onetoOneField
user_profile - onetoonefield
vendor_name or restaurant_name
vendor_license or restaurant_license
is approved
created_at
modified_at


Creamos otro app: python manage.py startapp vendor
 
-------- 7.2 vendor registration template -----------------------

Creamos la ruta para registrar vendor

---------------- 7.3. Vendor Registration Feature -------------------- 

Cambiar la href de navabar para redirigir la registerVendor

Crear file called forms.py para los campos del formulario.


---------------- 7.4. Vendor Admin Config --------------------

en admin.py from vendor anadir vista columanas.

--------------  7.5. Login Page Setup -------------------------

Custom of registerUser.html and only two fields: email address and
password, then custom size.

---------------- 7.6 Login Logout feature ---------------------
Se realiza el control de login, si estan correctos se redirecciona 
a dashboard.html caso contrario nuevamente a login pero se notifica
que estan mal sus entradas. Esto se realiza en accounts/views.py
Luego se crea el dashboard.html, se extends de base.html y en el 
content se include el alert.
Luego se arregla las direccions de navbar.html para login and register
and then if just logged in dont should show login and register button
only logout. This modified in navbar.html .Also must be myaccount button
to go dashboard.

7.7 Restrict loggedin user from accessing loginpage and registerpage

Se controla en accounts/views.py before that user was authenticated.
and send a warming message.
Se realiza las configuracion cuando ya esta logged, entonces no tiene
que ir a la url registerUser o login.

-- 7.8. Detectuser And Redirect Him To Respective Dashboard --------
 Necesitamos redirigir a los user ya sea customer or vendor a sus
dashboard correspondiente.
Se crea un def in accounts/models.py

---------------- 7.9 restric the user to access ----------------
se crear nuevas def en view.py para restringir y se crea un 403.html

************** 8. Token verification & Email configuration *********

---------------------- 1. Email Configuration -------------------

Configurar en setting.py para email. 
Solucion para habilitar email.
Because you use 2 factor authentication, you must create a password for this application to access your Google account without the 2 factor auth.

Perform all the steps on the Google support page to generate an 
application password, and then update your EMAIL_HOST_PASSWORD to 
use that, rather than your regular account password.

On this page: support.google.com/accounts/answer/185833 follow the 
steps under the heading "How to generate an App password". 
After you generate it, you need to use that password in your 
configuration.

------------------ 2 
se crea una funcion send_notofication al email del user que 
desae crearse para confirmar.

----------------- 7.3. Activating The User

Add line on setting.py default_email
Add lines on views.py para activate def.

-------------- 7.4 Forgot password










Referencias
https://omes-va.com/virtualenv-python/



