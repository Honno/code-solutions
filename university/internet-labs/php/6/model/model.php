<?php

include_once("model/account.php");

class Model {

    private $server;
    private $dbname;
    private $username;
    private $password;
    private $pdo;
	  # define the constructor which has four arguments for $server, $dbname, $username, $password. 
	  # The $pdo field should be assigned as null
    public function __construct($server, $dbname, $username, $password) {
        $this->server = $server;
        $this->dbname = $dbname;
        $this->username = $username;
        $this->password = $password;
        $this->pdo = null;
    }

    #Define a Connect() function to create the $pdo as a PDO object based on the four fields $server, $dbname, $username, $password.
	  #Using the try/catch structure to handle the database connection error
    public function Connect() {
        try {
            $dsn = "mysql:dbname=" . $this->dbname . ";host=" . $this->server;
            $this->pdo = new PDO($dsn, $this->username, $this->password);
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $e) {
            error_log($e->getMessage());
        }
    }

    #method to get an account by id, returns an account object
	  #it querys database and create an object account if the id exists in database; 
	  #return null otherwise
    public function getAccountById($id) {
        try {
            $results = $this->pdo->query("SELECT * FROM savings WHERE id=" . $id);
            if ($results) {
                $record = $results->fetch();
                $account = new Account($record["id"], $record["balance"]);
                return $account;
            } else return null;
        } catch (PDOException $e) {
            error_log($e->getMessage());
        }
	  }

	  #method to withdraw money from account
	  #returns the new balance after withdraw amount from account; return null if failure
	  #it update balance of user id in the database
	  #should check whether amount is less than or equal to current balance
    public function withdraw($id, $amount) {
        try {
            $results = $this->pdo->query("SELECT * FROM savings WHERE id=" . $id);
            if ($results) {
                $record = $results->fetch();

                $balance = $record["balance"] - $amount;
                if ($balance >= 0) {
                    $result = $this->pdo->exec("UPDATE savings SET balance=$balance where id=$id");

                    if ($result) return $balance;
                }
            }
            return null;
        } catch (PDOException $e) {
            error_log($e->getMessage());
        }
    }

	  #method to deposit amount to account id
	  #returns the new balance after depositing amount to account; return null if failure
	  #it update balance of user id in the database
    public function deposit($id, $amount) {
        try {
            $results = $this->pdo->query("SELECT * FROM savings WHERE id=" . $id);
            if ($results) {
                $record = $results->fetch();

                $balance = $record["balance"] + $amount;
                $result = $this->pdo->exec("UPDATE savings SET balance=$balance WHERE id=$id");

                if ($result) return $balance;
            }
            return null;
        } catch (PDOException $e) {
            error_log($e->getMessage());
        }
	  }
}
?>
