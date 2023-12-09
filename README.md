# boat_heater
a bit of code for a raspberry pi which will monitor the temperature and turn on and off a lamp. Usefull for keeping the temperature at the ideal setting for the epoxy to cure while I was building my boat. 

make sure to use an old-school halogen light buld rather than an LED as the LEDs don't put out any heat. 

the get_temp script should be run with crontab I used all *'s to make to test every minute, every hour, every day of week, etc. 
it also needs a bunch of hardware wired into the proper pins of the rasbpi that go to the light. I should have a schematic drawing of those somewhere. 
