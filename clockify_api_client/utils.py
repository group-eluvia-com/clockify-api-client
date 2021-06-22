class Singleton(type):
    """Singleton metaclass. Creates **singleton** instead of normal class when used as metaclass of class

    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
