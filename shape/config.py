from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#create 3 sections for different shapes in the config file
config_object["Mono-circle"] = {
    "shape": "circle",
    "connection_type": "wifi",
    "address": "192.168.1.0"
}

config_object["Mono-square"] = {
    "shape": "square",
    "connection_type": "wifi",
    "address": "192.168.1.1"
}

config_object["Multi-shape"] = {
    "shape": "multiShape",
    "connection_type": "wifi",
    "address": "192.168.1.2"
}


#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)