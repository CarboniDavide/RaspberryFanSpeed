# config.py
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
#
# Main project configuration file

# Add new dictionary to use more gpio's pin:
# For example add this at the end of array to have a new gpio pin: 
#  {
#       'gpio_name' : 8,
#       'temp_level' : 58
#  },
#
# In this base configuration four gpio's pin are useds 
GPIO_FAN_SETTINGS = [
    {
        'gpio_name' : 5,
        'temp_level' : 68
    },
    {
        'gpio_name' : 6,
        'temp_level' : 70
    },
    {
        'gpio_name' : 13,
        'temp_level' : 72
    },
    {
        'gpio_name' : 19,
        'temp_level' : 75
    }
]

# Fan refresh state! 
# Use seconds as base unit. For example: 1, 2, 0.5, etc.
FAN_REFRESH_TIME = 5

# Test sleep time between each state.
# Use seconds as base unit. For example: 1, 2, 0.5, etc.
TEST_SLEEP_TIME = 1