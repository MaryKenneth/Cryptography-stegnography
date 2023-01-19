# Cryptography-stegnography
This is a simple GUI written in Python to perform text encryption and image steganography. All functionality are contained in the single python script (steganography.py)
## first interface
![image](https://user-images.githubusercontent.com/60054434/213454333-a97552bc-eb6a-4354-821a-663081ffc3f2.png)

From the first interface the user can perform message hiding or retrievel from the cover image
## The encoding/steganography interface
![image](https://user-images.githubusercontent.com/60054434/213454760-312c816b-b471-4e2b-9646-5a9c1106dec5.png) 

On this page the user will select any image of their choice from their PC to use as the cover image. After selecting a cover image the user can paste the message/text which they want to hide on the second black frame/text box. The pasted text is then encrypted when the user clicks the encode message button. Then encode message is now hidden in the cover image when the hide message button is clicked. This new image with the secret can then be save for later use. 
Note:: Initially only the select image and exit button is enable while every other button is disabled. These buttons are enabled based on the stage of the steganography.

![image](https://user-images.githubusercontent.com/60054434/213456622-7b0ed4ae-9406-4384-abd2-e8dd8d6e978f.png)
## Decryption and message retrieval interface
![image](https://user-images.githubusercontent.com/60054434/213457225-4ca60fde-b90c-4667-83b2-fe4bfed82342.png)

A user can retrieve the hidden secret message from the stegno-Image on this page. The hidden message will be retrieved encrypted and can only be decrypted using the secret key saved when initially encrypting. The retrieved decrypted message can me be saved by the user.

![image](https://user-images.githubusercontent.com/60054434/213457895-6592cf87-834e-4f67-ad1b-92811cdfe405.png) 
### Interface after retrieiving and decrypting the hidden message
![image](https://user-images.githubusercontent.com/60054434/213458205-9e02ec19-09e1-4d21-bb98-5401892d0b12.png)
