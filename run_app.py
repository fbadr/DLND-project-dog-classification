def run_app(img_path):
    orig_img = Image.open(img_path)
    ## handle cases for a human face, dog, and neither
    if dog_detector(img_path):
       
        breed = predict_breed_transfer(img_path)
        
        plt.figure()
        plt.imshow(orig_img)
        plt.title('Dog detected!')
        plt.suptitle("Predicted Dog breed: {}".format(breed), y=-0.001)
        
    elif face_detector(img_path):
        
        breed = predict_breed_transfer(img_path)
        
        plt.figure()
        plt.imshow(orig_img)
        plt.title('Human detected!')
        plt.suptitle("You look like a {} !".format(breed), y=-0.001)
    
    else:
        plt.figure()
        plt.imshow(orig_img)
        plt.title('Could not detect a Human nor Dog!')