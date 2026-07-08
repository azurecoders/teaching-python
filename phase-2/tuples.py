configurations = ("localhost", "fast_api_tutorial", "postgres")
# additional_configurations = ("db_configuration_1", "db_configuration_2")

# configurations[0] = "neon.db" # This is not possible in tuple because they are immutable.
# print(configurations)

# print(configurations + additional_configurations)


# def empty_function():
# pass


# def connection():
#     pass
# host_name, db_name, db_password = configurations
# pg.connect({
#     host_name: host_name,
#     db_name: db_name,
#     db_password: db_password
# })
# print(host_name, db_name, db_password)


# connection()

for config in configurations:
    print(config)
