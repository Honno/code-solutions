<html>
    <body>
        <table>
            <tr>
                <th>Reg_no</th>
                <th>Category</th>
                <th>Brand</th>
                <th>Dailyrate</th>
                <th>Description</th>
            </tr>
            <?php
            $db = require 'connectdb.php';

            $vehicles = $db->query("SELECT * FROM vehicles");

            function td($record, $attr) {
            echo "<td>" . $record[$attr] . "</td>";
            }

            foreach($vehicles as $vehicle) {
                echo "<tr>";

                td($vehicle, "reg_no");
                td($vehicle, "category");
                td($vehicle, "brand");
                td($vehicle, "daily_rate");
                td($vehicle, "description");

                echo "</tr>";
            }
            ?>
        </table>
    </body>
</html>
