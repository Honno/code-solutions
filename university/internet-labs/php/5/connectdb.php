
<?php
try {
    $db = new PDO("mysql:dbname=carent;host=localhost", "root", "pass");
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    return $db;
} catch(PDOException $e) {
    error_log($e->getMessage());
}
?>
