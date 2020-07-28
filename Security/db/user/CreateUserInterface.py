import abc

class CreateUserInterface(metaclass=abc.ABCMeta):
  @classmethod
  def __subclasshook__(cls, subclass):
    return (
      hasattr(
        subclass, 'create' and callable(subclass.create) or NotImplemented
      )
    )
  
  @abc.abstractmethod
  def create(self, username: str, password: str, confirm_password: str):
    '''
      Crear un usuario
    '''
    raise NotImplementedError
