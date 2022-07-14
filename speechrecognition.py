import speech_recognition as sr
from selenium import webdriver


class voice:
    def __init__(self):
      self.Recogniser =sr.Recognizer()

      self.ListenOnMic()

    def ListenOnMic(self):
        while True:
                try:
                  with sr.Microphone() as source:
                   audio = self.recognizer.listen(source)
                  command = self.recognizer.recognize_google(audio).lower
                  if 'search' in command:
                    driver = webdriver.chrome()
                    driver.get(f"https://www.google.co.in/search?q=tiger+age&sxsrf=ALiCzsaRnKwm3zQH4B8UhQGklITHQ6e3dQ%3A1657356080210&ei=MD_JYrKrDLvRseMPuP6NiAo&ved=0ahUKEwiyg7XDtOv4AhW7aGwGHTh_A6EQ4dUDCA4&uact=5&oq=tiger+age&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCRAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUILhCABDIFCAAQgAQyBQgAEIAEOgcIIxDqAhAnOgQIIxAnOgQILhAnOgoILhCxAxCDARBDOgQILhBDOgQIABBDOgsIABCABBCxAxCDAToLCC4QgAQQsQMQgwE6CAguEIAEENQCOg0ILhCABBCHAhCxAxAUOggIABCABBCxAzoOCC4QgAQQsQMQgwEQ1AI6CAguEIAEELEDOggILhCxAxCRAjoRCC4QgAQQsQMQgwEQxwEQrwE6CggAEIAEEIcCEBRKBAhBGABKBAhGGABQkCZY9zVgozhoAXABeACAAc4BiAHcC5IBBTAuNy4ymAEAoAEBsAEKwAEB&sclient=gws-wiz&q={command.split('search')[-1]}")

                                
                except:
                    pass
                        
Listener = voice()




