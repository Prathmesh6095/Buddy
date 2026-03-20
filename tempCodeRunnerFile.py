elif "close excel" in self.query:
                    speak("Okay sir, closing excel")
                    os.system("taskkill /f /im CMD.EXE")
                    speak("Done sir.")