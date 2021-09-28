from setuptools import setup, find_packages

setup(
    name                        =   "todobackend",
    version                     =   "0.1.0",
    description                 =   "Todobackend Django REST service",
    packages                    =   find_packages(),
    include_package_data        =   True,
    scripts                     =   ["manage.py"],
    install_requires            =   ["Django==1.9",
                                     "django-cors-headers==1.1.0",
                                     "djangorestframework==3.3.0",
                                     "mysql-connector-python==8.0.26",
                                     "mysqlclient==2.0.3",
                                     "uwsgi>=2.0"],
    extras_require              =   {
                                        "test": [
                                            "colorama==0.4.4",
                                            "coverage==5.5",
                                            "django-nose==1.4.7",
                                            "nose==1.3.7",
                                            "pinocchio==0.4.3",
                                            "protobuf==3.17.3",
                                            "PyMySQL==1.0.2",
                                            "six==1.16.0"
                                        ]

                                    }

)