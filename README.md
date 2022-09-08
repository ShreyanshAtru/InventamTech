# InventamTech
Using JWT and DRF , Restaurant and customer project.  

Applied JWT and can register through API and getting JSON resposne.
There are 3 types User --> Admin(superuser) , Staff(restaurant owner), customer 
After the sign up when you login the customer can only see the resturant menu, name and price , owner and superuser will redirect to admin page.


To clone the project :
   git clone https://github.com/ShreyanshAtru/InventamTech.git
   
Make a virtual environment :
  pip install virtualenv 
  virtualenv  <env_name>   #windows
  .\<env_name>\Scripts\activate  # to actiavte the env
  
To run the project start the server go in the project file where manage.py file and run this command 
  python manage.py runserver   
