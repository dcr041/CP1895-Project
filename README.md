# CP1895-Project
The project is to create a web app for a collection of cooking recipes.

## Description:
The project web app will have a homepage that introduces the recipe page. To get started with uploading your own new recipes to the server you will have to sign up and create an account. This option can be found in the upper right-hand corner of the homepage. To create an account click Login/Sign up. This will take you to the login page where you will find Sign Up button to the right of the Login button. Fill out the Sign up form and click Submit at the bottom of the form. Once the account is created you will be automatically redirected back to the login page. Fill out your information and then click on Login. The page where recipes are displayed will be accessible with the “Find recipes” link in the toolbar of the homepage. Each collectible item displayed will include at least one image and at least 3 text elements. The text element options will be recipe name, description, ingredients, preparation time, cook time, total time, and serving instructions. The form to upload new recipes to the server will be accessible with the “Create recipe” link in the toolbar of the homepage. The form to upload new recipes to the server will have both javascript validation for the form and server-side validation of the data. You will be able to click on the “Choose file” button at the top of the form to upload at least one image. You must add to at least three of the text elements below. To remove a recipe item, click on your username in the upper right-hand corner and select “Remove recipe item” from the dropdown menu. Once this is clicked you will be brought to the page where your uploaded recipes are displayed and the ability to remove text elements from them.

# Download & Installation
## Step 1:
- Download the files in the git repo https://github.com/dcr041/CP1895-Project or [click here](https://github.com/dcr041/CP1895-Project/archive/refs/heads/main.zip)
- Unzip the downloaded folder and add all of the files to your python project.

## Step 2:
Use the package manager pip to install the required dependencies
```zsh
pip install -r requirements.txt
```

## Step 3:
From the terminal, run these commands to start the flask application.
```console
$env:Flask_APP="application"
$env:Flask_ENV="development"
flask run
```

# Run your Web App
To upload new recipes or remove recipe items, you must first sign up and create an account.
## Step 1:
Click Register. This option can be found in the upper right hand corner of the webpage. Fill out the signup form and submit.

## Step 2:
Once the account is created, you will be automatically redirected to the login page. Fill out your information and click Login.

# Add recipe
## Step 1:
Click Add Recipes. This option can be found in the navigation bar.

## Step 2:
Fill out the form by entering the recipe name, image, ingredients, instructions, and servings. The recipe image must have the file extension .jpeg, .jpg, or .png.

## Step 3:
Once the information has been filled out, click Submit Recipe to add the recipe.

# Delete Recipe
## Step 1:
Click Delete Recipe. This option can be found in the navigation bar.

## Step 2:
Select the recipe you want to delete from the dropdwon menu.

## Step 3:
Once the recipe you want to delete has been selected, click Confirm Recipe.
