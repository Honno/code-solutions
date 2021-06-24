<?php
if (isset($_POST["balance"])) {
#Get the "id" from the form input and Get balance value of this id into $balance
#you should call the model method call the Model's getAccountById() method and Account's getBalance method to do this
    $account = $this->model->getAccountById($_POST["id"]);
    $balance = $account->balance;

//Display balance
	if ($balance != null) {
		echo "<b><h3>Your balance is: &pound; $balance</h3></b>";
	} else {
		echo "<p>Sorry, there is an error. Please try again.</p>";
	}
}
else { //display the form
?>
<h1>Balance</h1>
<form method="post" action="">
<div>
        Please enter the account ID <input type="text" name="id"/>
        <input type="submit" name="balance" value="balance">
</div>
</form>

<?php 
}
?>
