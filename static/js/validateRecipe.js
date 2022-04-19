"use strict"

const $ = selector => document.querySelector(selector);

document.addEventListener("DOMContentLoaded", () => {

    $("#submit_recipe").addEventListener("click", submitRecipe);
});

function submitRecipe() {

    const validExtensions = ["jpg", "jpeg", "png", "bmp"];
    let isValidName, isValidSize, isValidFile, isValidIngredients, isValidInstructions;
    let fileExtension = $("#image_upload").value.split('.').pop();

    if($("#image_upload").value === ""){
        $("#image_upload").nextElementSibling.textContent = "Must include an image file.";
        isValidFile = false;
    }else if (!(validExtensions.includes(fileExtension))){
        $("#image_upload").nextElementSibling.textContent = "Invalid image file. Must use a jpg, png, or bmp file.";
        isValidFile = false;
    }else{
        $("#image_upload").nextElementSibling.textContent = "";
        isValidFile = true;
    }

    if ($("#recipe_name").value === ""){
        $("#recipe_name").nextElementSibling.textContent = "Must include a recipe name.";
        isValidName = false;
    }else{
        $("#recipe_name").nextElementSibling.textContent = "";
        isValidName = true;
    }

    if ($("#servings").value === ""){
        $("#servings").nextElementSibling.textContent = "Must include the number of servings.";
        isValidSize = false;
    } else if (isNaN($("#servings").value) === true){
        $("#servings").nextElementSibling.textContent = "Must be a number.";
        isValidSize = false;
    } else{
        $("#servings").nextElementSibling.textContent = "";
        isValidSize = true;
    }

    if ($("#ingredients").value === "") {
        $("#ingredients").nextElementSibling.textContent = "Must include a list of ingredients.";
        isValidIngredients = false;
    }else{
        $("#ingredients").nextElementSibling.textContent = "";
        isValidIngredients = true;
        $("#ingredients").value.replaceAll(",","").split("\n");
    }

    if ($("#instructions").value === "") {
        $("#instructions").nextElementSibling.textContent = "Must include cooking instructions.";
        isValidInstructions = false;
    }else{
        $("#instructions").nextElementSibling.textContent = "";
        isValidInstructions = true;
    }

    if (isValidFile && isValidName && isValidSize && isValidIngredients && isValidInstructions){
        $("#recipe_form").submit();
    }
}