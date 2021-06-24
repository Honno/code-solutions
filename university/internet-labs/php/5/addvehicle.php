<html>
    <body>
        <form method="POST" action="addvehicle.php">
            <p>reg_no: <input type="text" name="reg_no"/></p>
            <p>category:</p>
	          <p><input type="radio" value="truck" name="category">car</p>
	          <p><input type="radio" value="truck" name="category">truck</p>
            <p>brand: <input type="text" name="brand"/></p>
            <p>daily_rate: <input type="number" step=".01" name="daily_rate"/></p>
            <input type="hidden" name="submitted" value="true" />
            <p><input type="submit" value="Enter"/></p>
            <p><input type="reset" value="Reset"/></p>
        </form>

        <?php
        $db = require 'connectdb.php';

        $reg_no = $_REQUEST['reg_no'];
        $category = $_REQUEST['category'];
        $brand = $_REQUEST['brand'];
        $daily_rate = $_REQUEST['daily_rate'];

        $values="(" . $db->quote($reg_no) . ", " . $db->quote($category) . ", " . $db->quote($brand) . ", " . $db->quote($daily_rate) . ")";
        $db->exec("INSERT INTO vehicles (reg_no, category, brand, daily_rate) VALUES $values");
        ?>
    </body>
</html>
