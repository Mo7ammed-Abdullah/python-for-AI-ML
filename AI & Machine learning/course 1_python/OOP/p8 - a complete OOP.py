# ------ inheritance in OOP ------

# --parent class
class Phone:
  category = "Electronics"

  def __init__(self,model , battery , camera,battery_percentage=100):
    self.model = model
    self.battery = battery
    self.camera = camera
    self.battery_percentage = battery_percentage

  def charge(self,hour):
    print(f"charge completed by {hour}")

  def capture(self,photo):
    if(self.battery_percentage)<=0:
      print("No charge")
    else:
      self.battery_percentage-=photo
      print(f"photo captured in {self.model}")

# another parent class
class Cooling_Mechanism:
  def __init__(self,cooling_method):
    self.cooling_method= cooling_method

  def cooling_on(self):
    print(f"the system is being cool by {self.cooling_method}")



## --creating object
apple = Phone("Iphone17",3000,40)
blueberry = Phone("B-17",4000,30)
motorola = Phone("M-17",3500,35)
apple.capture(10)
print(motorola.battery_percentage)


 

# ---- single inheritance
class SmartPhone(Phone):                                    # child class
  def __init__(self,model , battery , camera,processor):    
    super().__init__(model,battery,camera)                  # calling parent class constructor using super()
    self.processor = processor                              # additional property of child class

  def charge(self,hour):
    print("fast charging in process")
    super().charge(hour)                                    # calling parent class method using super()


# object
pro = SmartPhone("X",5000,100,"SnapDragon")
print(pro.model)
pro.charge(1)
     

# ---- multiple inheritance

class SmartPhone_CoolingMode(SmartPhone,Cooling_Mechanism):
   def __init__(self,model , battery , camera,processor,cooling_method):
    SmartPhone.__init__(self,model,battery,camera,processor) # calling constructor of first parent class , no need super for multiple inheritance
    Cooling_Mechanism.__init__(self,cooling_method)          # calling constructor of second parent class , no need super for multiple inheritance

# object
pro_cooling = SmartPhone_CoolingMode("Y",5000,100,"SD","Nitrogen")

print(pro_cooling.processor) # from SmartPhone class
print(pro_cooling.battery) # from Phone class
print(pro_cooling.cooling_method) # from Cooling_Mechanism class
print(pro_cooling.cooling_on())   # method from Cooling_Mechanism class
print(pro_cooling.charge(1)) # mothod from SmartPhone class which calls method from Phone class using super




# ******************************************************************************

# ------ polymorphism in OOP ------

# class
class Camera:
  def __init__(self , name):
    self.name = name

  def capture(self):
    print("a photo is captured")

# child classes
class Smart_Phone(Camera):
  def __init__(self,name,resolution):
    super().__init__(name)
    self.resolution = resolution

  #method overriding
  def capture(self):
    print("Photo is captured by a Phone")


class DSLR(Camera):
  def __init__(self,name,resolution):
    super().__init__(name)
    self.resolution = resolution

  def capture(self):
    print("Photo is captured  by DSLR")



class Drone(Camera):
  def __init__(self,name,resolution):
    super().__init__(name)
    self.resolution = resolution

  def capture(self):
    print("Photo is captured by Drone")


# objects
phone = Smart_Phone("Phone",30)
dslr = DSLR ("DSLR",200)
drone = Drone("Drone",150)


phone.capture()
dslr.capture()
drone.capture()


# --- encapsulation in OOP ------

# design
class Mobile:
  def __init__(self,name,model,imei):
    self.__name = name
    self.__model = model
    self.__imei = imei # private

  def charge(self):
    print("phone is charging")

  # method imei ta paite pari
  def imei_getter(self):
    return self.__imei
  def model_getter(self):
    return self.__model



  def name_getter(self):
    return self.__name


  def name_setter(self,name):
    self.__name = name




#outside world ( user )

# registration
iphone = Mobile("Phone","17","1xkaf1")

print(iphone.name_getter())

iphone.name_setter("Phitron")


print(iphone.name_getter())


# --- abstraction in OOP ------

from abc import  ABC , abstractmethod

class Telephone(ABC):

  @abstractmethod
  def make_call(self):
    pass



class Sphone(Telephone):
  def make_call(self):
    print("Making a call using SPhone")



class Iphone(Telephone):
   def make_call(self):
    print("Making a call using IPhone")

# object
ip = Iphone()

ip.make_call()