
/**
 * This represents a class form the HTML element with the class attribute contaning .my-form-control
 * @class
 */

class FormControl
{
    /**
     * Creates a new instance of FormControl
     * @param {HTMLElement} formElement - the HTML element with the class attribute containg .my-form-control
     */
    constructor(form){
        this.isInputHidden = false;
        this.formElement = form;
        this.inputElement = this.formElement.querySelector("input");
        this.labelElement = this.formElement.querySelector("label");
        this.lineMaskerElement = this.formElement.querySelector(".line-masker")
        this.eyeElement = this.formElement.querySelector(".eye");

        // Add some event listener
        this.inputElement.addEventListener("focus", this.onFocus.bind(this));
        this.inputElement.addEventListener("blur", this.outOfFocus.bind(this));
        this.eyeElement.addEventListener("click", this.handleInput.bind(this))
    }

    /**
     * Handles the animation of the labelElement when inputElement is on focus.
     * 
     */
    onFocus() {
        this.labelElement.classList.add("onFocus");
        this.labelElement.classList.remove("outOfFocus");
        this.lineMaskerElement.classList.add("line-masker-active");
    }

    /**
     * Handles the animation of the labelElement when inputElement is anyb longer on focus.
     * 
     */
    outOfFocus() {
        //Check if the input contain text or not
        if(!this.inputElement.value){
            this.labelElement.classList.add("outOfFocus");
            this.labelElement.classList.remove("onFocus");
            this.lineMaskerElement.classList.remove("line-masker-active");
        }
        else{
            ;
        }
    }

    /**
     * Hides the character of the input field
     */
    hideInput() {
        this.inputElement.setAttribute("type", "password");
        this.eyeElement.classList.remove("bi-eye-fill");
        this.eyeElement.classList.add("bi-eye-slash-fill");
    }

    /**
     * Shows the characters of the input field
     */
    showInput() {
        this.inputElement.setAttribute("type", "text");
        this.eyeElement.classList.add("bi-eye-fill");
        this.eyeElement.classList.remove("bi-eye-slash-fill");
    }

    /**
     * Handles the input field: hide and show
     */
    handleInput(){
        if(this.isInputHidden){
            this.showInput();
            this.isInputHidden = false;
        }
        else{
            this.hideInput();
            this.isInputHidden = true;
        }
    }

}

/**
 * Handle forms verification.
 */
class Form
{
    constructor(form){
        this.formElement = form;
        this.newPasswordInputElement = form.querySelector(".new-password");
        this.confirmPasswordInputElement = form.querySelector(".confirm-password");
        this.submitButtonElement = form.querySelector("button");

        // Add some event listeners
        this.submitButtonElement.addEventListener("click", this.submit.bind(this));
    }

    /**
     * Handle the input submition
     */
    submit(){
        let areInputEmpty = (this.newPasswordInputElement.value == "" || this.confirmPasswordInputElement.value == "");
        if(areInputEmpty || this.newPasswordInputElement.value != this.confirmPasswordInputElement.value){
            this.confirmPasswordInputElement.parentElement.classList.add("passDontMatch");
        }
        else{
            this.confirmPasswordInputElement.parentElement.classList.remove("passDontMatch");
            // this.formElement.reset();

            /* Submition operations */
            this.formElement.submit();
        }
    }

    /**
     * Handle the form when the password inputs (new and confirmation) do not match
     */
    passDontMatch(){
        this.confirmPasswordInputElement.classList.add("passDontMatch");
    }
}

/**
 * Handle the operations concerning deleting an account
 */
class DeleteAccountHandler{
    constructor(element){
        this.element = element;
        this.formElement = element.querySelector("form");
        this.triggerElement = document.querySelector(".delete-account-trigger");
        this.checkBoxElement = element.querySelector("input[type='checkbox'");
        this.deleteButtonElement = element.querySelector("button.delete");
        this.cancelButtonElement = element.querySelector("button.cancel");
        
        // Add some event listeners
        this.triggerElement.addEventListener("click", this.show.bind(this));
        this.deleteButtonElement.addEventListener("click", this.deleteAccount.bind(this));
        this.cancelButtonElement.addEventListener("click", this.cancelOperation.bind(this));
        // this.element.addEventListener("click", this.hide.bind(this));
    }

    /**
     * Displays the block element to the screnn
     */
    show(){
        this.element.style.display = 'flex';
    }

    /**
     * Hides the block element to the screnn
     */
    hide(){
        // console.log('NICE');
        this.element.style.display = 'none';     
    }
    /**
     * Handle the prcession of deleting a user account
     */
    deleteAccount(){
        if(this.checkBoxElement.checked){
            /* Handle deletion */
            this.formElement.submit();
        }
        else{
            /* Handle animation of the checkbox here here */
            this.checkBoxElement.classList.add("animated-checkbox");
            setTimeout(() => {
                this.checkBoxElement.classList.remove("animated-checkbox");
            }, 400);
        }
    }

    /**
     * Discards the account deletion process
     */
    cancelOperation(){
        this.element.style.display = 'none';
    }

}

// Create some instances of FormControl
let formControls = document.querySelectorAll(".my-form-control");
for(let formControl of formControls){
    new FormControl(formControl);
}

// Create a instance of form
let form = document.querySelector(".my-form");
form.reset();   // reset the form first
new Form(form);

// Create an instance of DeleteAccountHandler
deleteAccountBlock = document.querySelector(".delete-account-alert");
new DeleteAccountHandler(deleteAccountBlock);

