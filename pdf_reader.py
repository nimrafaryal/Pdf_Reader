# import pyttsx3
# import PyPDF2

# pdf_file = open(r"C:\Users\PMYLS\Downloads\nn.pdf", 'rb')
# reader = PyPDF2.PdfReader(pdf_file, strict=False)

# number_of_pages = len(reader.pages)

# engine = pyttsx3.init()
# for i in range(0, 1):
    
#     page = reader.pages[i]

#     page_content = page.extract_text()

   
#     new_rate = 200
#     engine.setProperty('rate', new_rate)
#     new_volume = 200
#     engine.setProperty('volume', new_volume)

   
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices', voices[1].id)

#     engine.say(page_content)

   
#     engine.save_to_file(page_content, 'pdf_audio.mp3')
#     engine.runAndWait()
#     engine.stop() 
import pyttsx3
import PyPDF2

# Open the PDF file
pdf_file = open(r"C:\Users\PMYLS\Downloads\Documents\poem.pdf", 'rb')
reader = PyPDF2.PdfReader(pdf_file, strict=False)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

try:
    # Extract text from the first page of the PDF
    page = reader.pages[0]
    page_content = page.extract_text()

    # Set the speech rate
    new_rate = 200
    engine.setProperty('rate', new_rate)

    # Set the volume (range is 0.0 to 1.0)
    new_volume = 1.0
    engine.setProperty('volume', new_volume)

    # Select the voice (0 for male, 1 for female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Convert the text to speech
    engine.say(page_content)

    # Save the audio to a file
    engine.save_to_file(page_content, 'pdf_audio.mp3')

    # Run and wait for the engine to finish processing
    engine.runAndWait()

    print("Text converted to speech successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Stop the engine and close the PDF file
    engine.stop()
    pdf_file.close()
